#!/usr/bin/env python3
"""Validate SubRip subtitles for ordering, timing, density, and optional transcript match."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TIMESTAMP = re.compile(r"^(\d{2,}):([0-5]\d):([0-5]\d)[,.](\d{3})$")
TIMING_LINE = re.compile(r"^(\S+)\s+-->\s+(\S+)(?:\s+.*)?$")


def to_ms(value: str) -> int:
    match = TIMESTAMP.fullmatch(value)
    if not match:
        raise ValueError(f"invalid timestamp {value!r}; expected HH:MM:SS,mmm")
    hours, minutes, seconds, millis = map(int, match.groups())
    return (((hours * 60) + minutes) * 60 + seconds) * 1000 + millis


def normalize(value: str) -> str:
    return " ".join(value.split()).strip()


def parse_srt(content: str) -> list[dict]:
    content = content.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n[ \t]*\n", content.strip())
    cues: list[dict] = []
    for block_number, block in enumerate(blocks, start=1):
        lines = block.split("\n")
        if len(lines) < 3:
            raise ValueError(f"block {block_number}: expected sequence number, timing line, and subtitle text")
        if not lines[0].strip().isdigit():
            raise ValueError(f"block {block_number}: sequence number is not an integer")
        timing = TIMING_LINE.fullmatch(lines[1].strip())
        if not timing:
            raise ValueError(f"block {block_number}: invalid timing line")
        text_lines = [line.rstrip() for line in lines[2:] if line.strip()]
        if not text_lines:
            raise ValueError(f"block {block_number}: subtitle text is empty")
        cues.append({
            "number": int(lines[0].strip()),
            "start": to_ms(timing.group(1)),
            "end": to_ms(timing.group(2)),
            "lines": text_lines,
            "text": normalize(" ".join(text_lines)),
        })
    return cues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("srt", type=Path, help="SRT subtitle file")
    parser.add_argument("--expected-duration", type=float, help="expected total duration in seconds")
    parser.add_argument("--transcript", type=Path, help="plain text with one exact spoken cue per line")
    parser.add_argument("--max-cps", type=float, default=17.0, help="characters per second review threshold (default: 17)")
    parser.add_argument("--max-line-chars", type=int, default=42, help="maximum visible characters per subtitle line (default: 42)")
    parser.add_argument("--strict-cps", action="store_true", help="make subtitle density above max-cps fail instead of warn")
    parser.add_argument("--require-contiguous", action="store_true", help="reject gaps between subtitle cues")
    args = parser.parse_args()

    try:
        cues = parse_srt(args.srt.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"SRT validation failed: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    for index, cue in enumerate(cues, start=1):
        if cue["number"] != index:
            errors.append(f"cue {index}: expected sequence number {index}, got {cue['number']}")
        if cue["end"] <= cue["start"]:
            errors.append(f"cue {index}: end must be later than start")
        if index == 1 and cue["start"] != 0:
            warnings.append(f"cue 1: starts at {cue['start']} ms instead of 0 ms")
        if index > 1:
            previous = cues[index - 2]
            if cue["start"] < previous["end"]:
                errors.append(f"cue {index}: overlaps previous cue by {previous['end'] - cue['start']} ms")
            elif args.require_contiguous and cue["start"] != previous["end"]:
                errors.append(f"cue {index}: gap of {cue['start'] - previous['end']} ms before this cue")

        duration = max(1, cue["end"] - cue["start"])
        cps = len(cue["text"]) / (duration / 1000)
        if cps > args.max_cps:
            message = f"cue {index}: {cps:.1f} chars/sec exceeds review threshold {args.max_cps:.1f}"
            (errors if args.strict_cps else warnings).append(message)

        for line_number, line in enumerate(cue["lines"], start=1):
            if len(line) > args.max_line_chars:
                warnings.append(f"cue {index}, line {line_number}: {len(line)} characters exceeds {args.max_line_chars}")

    if args.expected_duration is not None:
        expected_ms = round(args.expected_duration * 1000)
        if cues and cues[-1]["end"] != expected_ms:
            errors.append(f"last cue ends at {cues[-1]['end']} ms; expected {expected_ms} ms")
        if cues and cues[0]["start"] > 0:
            errors.append("first cue must start at 0 when expected duration is specified")

    if args.transcript:
        try:
            transcript_lines = [
                normalize(line)
                for line in args.transcript.read_text(encoding="utf-8-sig").splitlines()
                if line.strip()
            ]
        except (OSError, UnicodeError) as exc:
            errors.append(f"could not read transcript: {exc}")
        else:
            if len(transcript_lines) != len(cues):
                errors.append(f"transcript has {len(transcript_lines)} non-empty lines for {len(cues)} subtitle cues")
            else:
                for index, (cue, spoken) in enumerate(zip(cues, transcript_lines), start=1):
                    if cue["text"] != spoken:
                        errors.append(f"cue {index}: subtitle text does not exactly match transcript line")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"SRT validation failed: {len(errors)} error(s), {len(warnings)} warning(s).", file=sys.stderr)
        return 1

    total = cues[-1]["end"] if cues else 0
    print(f"SRT validation passed: {len(cues)} cue(s), ends at {total / 1000:.3f}s, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
