"""Reputation engine — external intelligence goes here. v0.1: no external calls, no URL fetching."""
def check_domain(domain: str) -> dict:
    return {"domain": domain, "reputation": "unknown", "source": "none", "note": "No reputation provider wired in v0.1."}
