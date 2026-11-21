import hashlib
def hash_indicator(value: str) -> str:
    return hashlib.sha256(value.strip().lower().encode()).hexdigest()
