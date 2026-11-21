def alert_text(guild_id: str, channel_id: str, risk_level: int, explanation: str) -> str:
    return f"[VERIX] Risk {risk_level} in <#{channel_id}> (guild {guild_id}): {explanation} No automatic action was taken — moderator review required for level 3."
