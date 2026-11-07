# Creator Production Playbook

This guide shows how the three creator-facing skills work together.

## The workflow

1. **BOS Viral Content Studio** turns a topic or campaign goal into concepts, hooks, a timestamped script, storyboard, voice-over brief, subtitles, edit brief, and publishing assets.
2. **Instagram Growth Agent** adapts the idea to an Instagram audience, account position, Reels/carousel mix, profile journey, and organic calendar.
3. **YouTube Creator Agent** expands the idea into a long-form video or reshapes it into a self-contained Short, then prepares titles, thumbnail concepts, chapters, and metadata.

Use only the parts relevant to the campaign. Do not force every idea onto every platform.

## Creator brief template

Before production, collect:

- Objective: awareness, education, trust, leads, sales, or community.
- Audience: who the content is for and what they need.
- Topic or offer: what the content is about.
- Platform and format: Reels, TikTok, Shorts, long-form, carousel, or story.
- Language and locale.
- Brand voice and required terminology.
- Desired duration and available production resources.
- Call to action and destination.
- Required evidence, disclaimers, or legal review.
- Rights and permissions for images, footage, music, and likeness.

A reusable example is in [creator-brief.md](../examples/creator/creator-brief.md).

## Short-video structure

A useful default structure is:

| Beat | Purpose | Production cue |
|---|---|---|
| 0–3 sec | Honest hook | Strong visual and one clear promise |
| 3–8 sec | Context | Explain why the viewer should care |
| Middle | Useful story or explanation | One idea per beat; visual changes support meaning |
| Payoff | Answer or insight | Deliver what the hook promised |
| End | CTA | One specific next action |

This is a planning framework, not an algorithm rule. Change it to fit the story and platform.

## Trend research

When the user asks for "trending", "viral now", or a timely topic:

- Search current platform or creator signals and trustworthy topical sources.
- Note the date checked and the evidence for the trend.
- Separate platform trend evidence from the creator's own audience evidence.
- Check whether the trend fits the audience and brand.
- Do not copy another creator's script, edit sequence, or distinctive identity.
- Avoid topics where virality depends on misinformation, harassment, dangerous challenges, or privacy violations.

If current research tools are unavailable, provide evergreen ideas and label them as hypotheses rather than current trends.

## Script and storyboard requirements

A production-ready short script should include timestamps, voice-over/dialogue, on-screen text, visual action, B-roll or graphics, sound cues, and transitions. Keep a subtitle-only text track separate from directions.

A storyboard should name each scene and specify framing, subject, action, background, text, and continuity. For motion graphics, define the graphic elements and their movement. Explicitly honor the requested medium (for example, 2D motion graphics rather than 3D animation). Keep scene label, visual, narration, and subtitles semantically aligned; remove brainstorming notes and unresolved self-corrections. For rupiah examples, use Rp notation rather than a dollar symbol.



For subtitle quality, run the repository SRT checker against the master voice-over transcript:

    python tests/validate_srt.py examples/creator/verified-sample-45s.srt --expected-duration 45 --transcript examples/creator/verified-sample-45s-vo.txt --strict-cps --require-contiguous

This checks sequence numbers, valid timecodes, overlap/gaps, total duration, a 17-characters-per-second editorial review threshold, and exact cue text against the transcript. It cannot prove synchronization to a rendered recording; listen to and inspect the final audio/video before claiming that.

## Production handoff

State which parts are complete and which require tools or a human:
- Ready: concept, script, storyboard, subtitle copy, shot list, edit instructions.
- Tool-dependent: generated images, recorded or synthesized voice, music licensing, actual video assembly, rendering, upload, and scheduling.

Never claim a video or audio file exists unless the corresponding production tool returned it and the result was checked.

## Measurement

Use the platform's analytics and compare with the account's own baseline. Track relevant measures such as watch time, audience retention, completion, saves, shares, comments quality, profile actions, link clicks, leads, and sales. Do not optimize one number in isolation.

Run one controlled creative experiment at a time. Write down the hypothesis, the variable changed, the measurement window, and the result.
