"""Cloud AI adapter — disabled by default. When enabled, only redacted text may be sent, never tokens or raw personal info."""
def classify_cloud(text: str, enabled: bool = False) -> dict:
    if not enabled:
        return {"provider": "cloud", "disabled": True, "note": "Cloud AI is disabled."}
    raise NotImplementedError("Cloud provider not configured — wire an opt-in provider here, with redaction first.")
