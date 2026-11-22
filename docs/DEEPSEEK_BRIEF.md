# VERIX — Full Project Brief for DeepSeek (Planner Handoff)

> **Copy-paste prompt to give DeepSeek along with this file:**
> You are my planner for VERIX. Read this whole brief, then read the public repo at https://github.com/adnqcr7-code/verix. Your job is to plan — not to write all the code yet. Give me a clear, step-by-step plan to finish Milestone 1 (Foundation), in small steps I can do one at a time. Keep it simple, cheap, and practical. Flag anything risky, ambiguous, or missing, and ask me before assuming. Be direct and honest — if an idea of mine is bad, say so and say why. Keep the tone fun and energetic, but keep the plan serious and precise.

---

## 1. Who I am

- My name is Adnan. I'm 18, from London, Ontario, Canada. I'm a high school student and a builder.
- I work like this: **I direct, AI codes, I own it.** I want to understand how things work, not blindly follow instructions.
- My learning cycle: Learn → Think → Code → Break/Fix → Explain.
- Talk to me direct, smart, practical, and honest. Concise when simple, detailed when needed. Challenge my ideas — tell me when something is stupid, unrealistic, inefficient, or impossible, and why.
- I start a lot of ambitious ideas and struggle with execution, so help me go: idea → validation → MVP → users → improvement → money. Smallest working version first, test it, then improve. No castles around untested buttons.
- Don't push paid subscriptions. Keep everything free or cheap.
- Long-term direction: software engineering, AI engineering, cybersecurity, entrepreneurship. I want to earn my first dollar from building something of my own.

## 2. What VERIX is

**VERIX is a privacy-conscious, AI-assisted threat intelligence platform designed to detect online scams, analyze suspicious activity, preserve relevant evidence, and help communities respond safely.**

- First product: a **Discord bot**.
- Long-term product: a **wider threat intelligence network** (website, browser extension, other platforms later).
- Version: **0.1.0**. Language: **Python**. Architecture: **Hybrid AI**. Cost model: **Free**. License: **to be decided**.
- Repository: **https://github.com/adnqcr7-code/verix** — flipping from private to PUBLIC Nov 21, 2026, so people can audit it and trust it.
- One engineering decision that matters: **VERIX is built as a detection engine first and a Discord bot second.** The engine lives in `src/verix/detection/`, `ai/`, `intelligence/`, `storage/`, `moderation/` and the bot in `src/verix/bot/` is just one client of it. That way a website or browser extension can reuse the same engine later without rewriting the intelligence system.

### The 5 core objectives

1. Detect suspicious messages and URLs.
2. Analyze scam techniques using rules and AI.
3. Correlate suspicious indicators with trusted threat intelligence.
4. Warn Discord communities before users interact with suspicious content.
5. Help moderators prepare accurate, evidence-based reports.

### What VERIX will NOT do (hard rules)

- Hack or access suspected scammers' accounts.
- Collect private Discord conversations.
- Expose private personal information.
- Automatically accuse people of crimes.
- Automatically ban users based on AI predictions.
- Conduct independent investigations against individuals.

### The trust idea (why the repo is public)

People should be able to see HOW it works without us exposing anyone's data. The repo hides data by design:

- No tokens anywhere in the repo. The Discord token lives only in a local `.env` file (gitignored, never committed).
- No real messages or detections in the repo. The SQLite database lives in `data/` (gitignored, local only).
- Indicators are stored as SHA-256 hashes, not raw values.
- The `.gitignore` is the full GitHub Python template plus `.env`, `.venv/`, `data/`, `*.db`.
- So the public repo shows the code, the rules, and the docs — the auditable part — and none of the sensitive part.

## 3. System architecture

Separate deterministic detection from AI interpretation:

```
DISCORD BOT → MESSAGE PROCESSOR → RULE ENGINE → REPUTATION ENGINE → HYBRID AI ANALYZER → RESPONSE ENGINE
              (validate,            (deterministic   (external           (local model     (risk explanation,
               normalize,            checks: URL      intelligence:       first, cloud     alerts, moderator
               redact)               patterns,        domain reputation   model optional)  review, evidence
                                     suspicious       + phishing                           records)
                                     language,        indicators)
                                     known indicators)
```

| Component | Responsibility |
|---|---|
| Local AI | Initial message classification |
| Cloud AI | Optional deeper analysis |
| Rule engine | Reliable, reproducible checks |
| Reputation APIs | External threat intelligence |
| Human moderators | Final decisions — always |

Cloud processing must be **opt-in**, with sensitive information redacted before submission. No API should ever receive Discord tokens, passwords, or unnecessary personal information.

## 4. Risk classification

Four levels. These are **risk classifications, not criminality scores**. A message can contain a suspicious link without its sender being responsible for it.

| Level | Meaning | Response |
|---|---|---|
| 0 | No known indicators | No action |
| 1 | Suspicious | Quiet monitoring |
| 2 | High risk | User warning |
| 3 | Strong evidence | Moderator review |

## 5. Database design (SQLite now, PostgreSQL long-term)

Tables: `guilds` (guild_id, configuration, enabled_modules, created_at), `detections` (detection_id, guild_id, channel_id, message_id, indicator_type, risk_level, explanation, created_at), `indicators` (indicator_id, indicator_type, indicator_value_hash, status, source, confidence, first_seen, last_seen), `reports` (report_id, detection_id, report_status, reviewer_decision, created_at), `audit_logs` (event_id, actor_type, action, timestamp).

Rules: don't store entire conversations. Don't store raw personal information unnecessarily. Keep evidence access restricted. Define retention and deletion policies. Encrypt sensitive evidence. Never store Discord bot tokens in the database.

## 6. Current state — what is DONE (verified Nov 21, 2026)

- Repo created Nov 21, 2026, 1:38 PM EST, private at first, then made public Nov 21 evening.
- Foundation scaffold pushed to `main` at commit `7c660bfc` — 35 files.
- **Tests: 9/9 pass** (`tests/test_urls.py`, `test_rules.py`, `test_scoring.py`, `test_storage.py`).
- Local workspace copy: `~/workspace/verix/` (my assistant's machine — the repo is the source of truth).

### Repository structure (as built)

```
verix/
├── src/verix/
│   ├── bot/            client.py, events.py, commands/
│   ├── detection/      rules.py, urls.py, scoring.py, classifier.py
│   ├── intelligence/   reputation.py, indicators.py
│   ├── ai/             local.py, cloud.py, analyzer.py
│   ├── storage/        database.py, models.py
│   ├── moderation/     alerts.py, review.py
│   └── config.py, logging_config.py
├── tests/              test_urls, test_rules, test_scoring, test_storage
├── docs/               setup.md, security.md, DEEPSEEK_BRIEF.md (this file)
├── scripts/
├── .env.example        (placeholders only — never put a real token here)
├── .gitignore          (full Python template + .env, data/, *.db)
├── pyproject.toml      (Python >= 3.11, discord.py, pydantic, pytest)
└── README.md
```

### What each built piece actually does right now

- `detection/urls.py` — safe URL extraction by regex only. Never fetches or opens a URL.
- `detection/rules.py` — deterministic rules: free Nitro/Robux/V-Bucks lures, crypto-doubling promises, gift-card lures, urgent "verify your account" pressure, prize/winner lures, send-money-to-get-money patterns, high-abuse TLDs (.ru, .tk, .xyz, .top, .click, etc.), brand lookalikes (discord-nitro, steamcommunity), non-official Discord domains.
- `detection/scoring.py` — weight → risk level 0–3, plus plain-English explanations.
- `detection/classifier.py` — `classify(text)` is the entry point: rules first, returns risk level + findings + explanation.
- `ai/local.py` — stub: local model not wired yet, rules are the classifier in v0.1.
- `ai/cloud.py` — disabled by default; raises unless explicitly enabled, and only redacted text may ever be sent.
- `ai/analyzer.py` — combines rule classification + local AI note.
- `intelligence/reputation.py` — stub: no reputation provider wired, no external calls.
- `intelligence/indicators.py` — SHA-256 hashing for indicators.
- `storage/` — SQLite schema for all 5 tables + `record_detection()`.
- `moderation/alerts.py` + `review.py` — alert text (level 2+) and review-queue entries (level 3 = pending review).
- `bot/client.py` — discord.py client, minimum permissions, `message_content` intent only, no DMs. Refuses to run without `DISCORD_TOKEN` in the environment.
- `bot/events.py` — `handle_message_text()`: extract URLs, classify, attach alert text for level 2+. Never auto-bans, never accuses.

## 7. Milestone 1 backlog — Foundation (status)

| # | Task | Status |
|---|---|---|
| 1 | Create GitHub repository: verix | DONE (private → public Nov 21) |
| 2 | Initialize Python project and dependencies | DONE (pyproject.toml) |
| 3 | Configure environment variables and secrets | DONE (.env.example, config.py — no real secrets) |
| 4 | Create logging and configuration modules | DONE |
| 5 | Add pytest and initial test suite | DONE (9/9 pass) |
| 6 | Build Discord bot connection | SKELETON DONE — not yet connected, needs a bot token + test server |
| 7 | Implement message event listener | SKELETON DONE (`handle_message_text`) — not live yet |
| 8 | Implement safe URL extraction | DONE |
| 9 | Build deterministic rule engine | DONE |
| 10 | Implement risk classification | DONE |
| 11 | Add SQLite storage | DONE |
| 12 | Connect local AI classifier | NOT DONE — stub only, rules are the classifier for now |
| 13 | Add optional cloud AI adapter | STUB DONE — disabled by default, no provider wired |
| 14 | Build moderator alert system | SKELETON DONE — alert text + review queue, no live delivery yet |
| 15 | Test false positives and false negatives | PARTIAL — unit tests pass; no live false-positive testing yet |
| 16 | Write setup and security documentation | DONE (docs/setup.md, docs/security.md) |

## 8. MVP acceptance criteria (v0.1 is ready when ALL are true)

- Bot successfully connects to a test Discord server.
- Bot recognizes suspicious URLs.
- Bot detects predefined scam patterns.
- Bot provides understandable explanations.
- Local AI classification works.
- Cloud AI can be disabled entirely.
- Moderators receive detection alerts.
- No automatic punishment occurs.
- Database records detections correctly.
- Tests cover normal messages and malicious-looking inputs.
- Secrets and sensitive information are protected.

## 9. Security requirements (before any deployment)

- Use Discord's minimum required permissions. Never enable unnecessary privileged intents. Don't read DMs.
- Treat message contents as untrusted input. Don't open suspicious URLs automatically. Don't execute downloaded files.
- Protect against prompt injection. Rate-limit submissions and API calls.
- Keep an audit trail of moderator actions.
- Test exclusively in a server where you have permission.

## 10. What I want from DeepSeek (the ask)

1. Read this brief AND the repo. Tell me what you think of the foundation honestly — what's solid, what's weak, what's missing.
2. Make me a step-by-step plan to finish Milestone 1, in the smallest steps possible, in order. Each step should be one thing I can do, test, and confirm before moving on.
3. The immediate blocker: I need a Discord bot token and a test server, and I have neither yet. Include the exact steps to create the bot in the Discord Developer Portal, what permissions/intents to turn on (minimum only), how to invite it to my test server, and how to store the token safely in `.env` — never in chat, never in code, never in the repo.
4. Then plan the local AI classifier: what's the simplest real local option (small, free, runs on CPU — I have no GPU), and how it plugs into `ai/local.py` without replacing the rule engine.
5. Plan the false-positive / false-negative testing: what test messages to use, how to measure it, what "good enough" looks like.
6. Don't add extra features. Don't redesign the architecture. Don't suggest paid services. If something in my spec is wrong or incomplete, say so and propose the fix.
7. End with: the ordered checklist, what I should do first, and what questions you need me to answer.

## 11. Tech facts

- Python 3.11+, `discord.py >= 2.3`, `pydantic >= 2.0`, `pydantic-settings`, `python-dotenv`, `pytest >= 8.0` (dev), `ruff` (dev).
- Install: `python3 -m venv .venv && source .venv/bin/activate`, `pip install -e ".[dev]"`, `cp .env.example .env`, `pytest`.
- My laptop: Dell Latitude 7400, i7-8665U, 16GB RAM, no dedicated GPU, Arch Linux. Local AI must be small and CPU-friendly.
- My other projects (for context, not for this plan): Veltrix Linux, COBALT Security (Roblox anti-cheat), BITON UI library, A9 YouTube channel, AVES model training. VERIX is separate — don't mix them in.
