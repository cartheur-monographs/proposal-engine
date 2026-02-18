# The Proposal Engine

The Proposal Engine is a focused toolkit for generating persuasive, structured proposals with AI-assisted drafting and human editorial control.

## Vision

- Turn rough ideas into clear, client-ready proposals.
- Keep humans in control of tone, claims, and final messaging.
- Standardize proposal quality across teams and use cases.

## Project Status

Early scaffold. The repository now includes a Python package, a CLI entrypoint, and room for templates, data, and tests.

## Quick Start

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m proposal_engine --help
```

## Repository Layout

```text
proposal-engine/
  proposal_engine/
    __init__.py
    __main__.py
    cli.py
  templates/
  tests/
  requirements.txt
```

## Next Milestones

1. Define proposal schema and validation rules.
2. Add prompt templates for common proposal types.
3. Implement generation and revision workflows.
4. Add end-to-end tests for deterministic sections.

## Pitch Draft

See `PROJECT_PITCH.md` for the collaborative, discovery-first investment pitch synthesized from source materials in `materials/`.

Additional variants:
- `PITCH_ONE_PAGER.md` (concise investor brief)
- `PITCH_VISIONARY.md` (speculative, big-picture narrative)
- `PITCH_FOREST_AG.md` (partner-specific version for forest management and sustainable agriculture)
- `PITCH_SLIDE_DECK.md` (10-slide, meeting-ready outline)
- `PITCH_TALK_TRACK.md` (speaker script, ~30-60 seconds per slide)
- `PITCH_TALK_TRACK_EXEC.md` (executive speaker script, ~20 seconds per slide)
- `PITCH_QA_CHEAT_SHEET.md` (investor Q&A prep: risk, moat, timeline, commercialization)
