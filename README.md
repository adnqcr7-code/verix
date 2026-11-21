# VERIX

A privacy-conscious, AI-assisted threat intelligence platform for detecting scams, analyzing suspicious activity and protecting online communities.

First product: a Discord bot. Long-term: a wider threat intelligence network.

## What it does
- Detects suspicious messages and URLs
- Analyzes scam techniques with deterministic rules first, AI second
- Correlates indicators with trusted threat intelligence
- Warns communities before users interact with suspicious content
- Helps moderators prepare accurate, evidence-based reports

## What it will NOT do
- Hack or access suspected scammers' accounts
- Collect private Discord conversations
- Expose private personal information
- Automatically accuse people of crimes
- Automatically ban users based on AI predictions

Risk levels 0–3 are risk classifications, not criminality scores. A suspicious link does not make its sender a scammer.

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # add DISCORD_TOKEN, never commit it
pytest
```

## Layout
Detection engine first, Discord bot second — `src/verix/detection/`, `ai/`, `intelligence/`, `storage/`, `moderation/`, `bot/`. That way a website or browser extension can reuse the same engine later.

See `docs/setup.md` and `docs/security.md`.
