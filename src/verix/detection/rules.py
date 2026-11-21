"""Deterministic rule engine — reproducible checks, no AI, no network."""
import re
from .urls import extract_urls, domain_of
SUSPICIOUS_PHRASES = [
    (r"free\s+(nitro|robux|v-bucks|gift)", "free premium currency / gift lure"),
    (r"double\s+(your\s+)?(crypto|bitcoin|eth)", "crypto doubling promise"),
    (r"(steam|discord)\s*gift", "gift-card / account gift lure"),
    (r"verify\s+(your\s+)?account.*(now|immediately|urgent)", "urgent account verification pressure"),
    (r"you('ve| have)\s+(won|been selected)", "prize / winner lure"),
    (r"limited\s+time.*claim", "false urgency to claim"),
    (r"send\s+\d+.*(get|receive)\s+\d+", "send-money-to-get-money pattern"),
]
SUSPICIOUS_TLDS = {".ru", ".tk", ".ml", ".ga", ".cf", ".gq", ".xyz", ".top", ".click", ".buzz"}
KNOWN_BRAND_LOOKALIKES = ["discord-nitro", "discordnitro", "steamcommunity", "discord-app"]
def check_rules(text: str) -> list[dict]:
    findings: list[dict] = []
    low = (text or "").lower()
    for pat, label in SUSPICIOUS_PHRASES:
        if re.search(pat, low):
            findings.append({"rule": "suspicious_language", "detail": label, "weight": 1})
    for url in extract_urls(text or ""):
        d = domain_of(url)
        if any(d.endswith(t) for t in SUSPICIOUS_TLDS):
            findings.append({"rule": "suspicious_tld", "detail": f"domain {d} uses a high-abuse TLD", "weight": 1})
        if any(b in d for b in KNOWN_BRAND_LOOKALIKES):
            findings.append({"rule": "brand_lookalike", "detail": f"domain {d} resembles a known brand", "weight": 2})
        if "discord" in d and not d.endswith("discord.com") and not d.endswith("discordapp.com"):
            findings.append({"rule": "discord_lookalike", "detail": f"domain {d} is not an official Discord domain", "weight": 1})
    return findings
