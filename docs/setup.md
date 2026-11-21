# Setup
1. Python 3.11+
2. `python3 -m venv .venv && source .venv/bin/activate`
3. `pip install -e ".[dev]"`
4. `cp .env.example .env` and set DISCORD_TOKEN
5. `pytest` — should pass before any bot run
6. Test only in a Discord server where you have permission.
