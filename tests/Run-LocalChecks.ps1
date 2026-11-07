[CmdletBinding()]
param(
    [switch]$InstallQualityValidator
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Push-Location $repoRoot

try {
    $pythonLauncher = Get-Command py -ErrorAction SilentlyContinue
    $python = Get-Command python -ErrorAction SilentlyContinue

    if ($pythonLauncher) {
        $pythonPath = $pythonLauncher.Source
        $pythonPrefix = @("-3")
    }
    elseif ($python) {
        $pythonPath = $python.Source
        $pythonPrefix = @()
    }
    else {
        throw "Python was not found. Install Python 3.9+ and retry."
    }

    $checks = @(
        @("tests/validate_skills.py"),
        @("tests/validate_benchmark.py"),
        @("tests/show_case.py", "--list"),
        @("tests/show_case.py", "--skill", "bos-viral-content-studio", "--scenario", "happy-path")
    )

    foreach ($check in $checks) {
        Write-Host ""
        Write-Host ("> {0} {1} {2}" -f $pythonPath, ($pythonPrefix -join " "), ($check -join " ")) -ForegroundColor Cyan
        & $pythonPath @pythonPrefix @check
        if ($LASTEXITCODE -ne 0) {
            throw "Check failed with exit code $LASTEXITCODE : $($check -join ' ')"
        }
    }

    if ($InstallQualityValidator) {
        $go = Get-Command go -ErrorAction SilentlyContinue
        if (-not $go) {
            throw "Go was not found. Install Go 1.24+ or run without -InstallQualityValidator."
        }

        Write-Host ""
        Write-Host "> Installing community skill-validator v0.5.0" -ForegroundColor Cyan
        & $go.Source install github.com/agent-ecosystem/skill-validator/cmd/skill-validator@v0.5.0
        if ($LASTEXITCODE -ne 0) {
            throw "Could not install skill-validator."
        }

        $validatorCandidates = @(
            (Join-Path $env:USERPROFILE "go\bin\skill-validator.exe"),
            (Join-Path $env:USERPROFILE "go\bin\skill-validator")
        )
        $validator = $validatorCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
        if (-not $validator) {
            $validatorCommand = Get-Command skill-validator -ErrorAction SilentlyContinue
            if ($validatorCommand) { $validator = $validatorCommand.Source }
        }
        if (-not $validator) {
            throw "skill-validator was installed but could not be located. Check your Go bin directory."
        }

        Write-Host ""
        Write-Host "> Strict Agent Skills structure validation" -ForegroundColor Cyan
        & $validator validate structure --strict skills/
        if ($LASTEXITCODE -ne 0) {
            throw "Strict Agent Skills structure validation failed."
        }

        Write-Host ""
        Write-Host "> Additional content-quality diagnostics" -ForegroundColor Cyan
        & $validator check skills/
        if ($LASTEXITCODE -eq 1 -or $LASTEXITCODE -ge 3) {
            throw "skill-validator reported errors or a command failure."
        }
        if ($LASTEXITCODE -eq 2) {
            Write-Warning "Content-quality warnings were reported. Review them before release."
        }
    }

    Write-Host ""
    Write-Host "All requested local checks completed." -ForegroundColor Green
}
finally {
    Pop-Location
}
