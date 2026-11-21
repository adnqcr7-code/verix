"""Message events: extract URLs, classify, record, alert. Never auto-ban, never accuse."""
from ..ai.analyzer import analyze
from ..detection.urls import extract_urls
from ..moderation.alerts import alert_text
async def handle_message_text(text: str, guild_id: str, channel_id: str, message_id: str) -> dict:
    result = analyze(text)
    result.update({"guild_id": guild_id, "channel_id": channel_id, "message_id": message_id, "urls": extract_urls(text)})
    if result["risk_level"] >= 2:
        result["alert"] = alert_text(guild_id, channel_id, result["risk_level"], result["explanation"])
    return result
