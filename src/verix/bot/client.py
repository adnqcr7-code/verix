"""Discord bot — minimum permissions, no DMs, message content treated as untrusted input. Token only from env."""
import discord
from ..config import settings
from ..logging_config import setup_logging
log = setup_logging(settings.log_level)
class VerixBot(discord.Client):
    async def on_ready(self):
        log.info("VERIX connected as %s", self.user)
def build_bot() -> VerixBot:
    intents = discord.Intents.default()
    intents.message_content = True  # needed to read message text for detection; no other privileged intents
    return VerixBot(intents=intents)
def run() -> None:
    if not settings.has_discord_token:
        raise SystemExit("DISCORD_TOKEN is not set. Set it in .env (never commit it) and run again.")
    build_bot().run(settings.discord_token)
if __name__ == "__main__":
    run()
