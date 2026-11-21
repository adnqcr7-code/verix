"""Safe URL extraction. Never fetches, never opens a URL — extraction only."""
import re
URL_RE = re.compile(r"https?://[^\s<>\")\]]+|www\.[^\s<>\")\]]+", re.IGNORECASE)
def extract_urls(text: str) -> list[str]:
    if not text:
        return []
    out = []
    for m in URL_RE.findall(text):
        u = m.rstrip(".,;:!?")
        if u not in out:
            out.append(u)
    return out
def domain_of(url: str) -> str:
    u = url.lower().removeprefix("https://").removeprefix("http://").removeprefix("www.")
    return u.split("/")[0].split("?")[0].split("#")[0]
