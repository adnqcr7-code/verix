"""Local AI adapter — stub for v0.1. Local-first: no message leaves the machine unless cloud is explicitly opted in."""
def classify_local(text: str) -> dict:
    return {"provider": "local-stub", "risk_level": None, "note": "Local model not wired yet — rule engine is the classifier in v0.1."}
