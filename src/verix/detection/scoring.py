"""Risk classification 0-3. These are risk levels, not criminality scores. A suspicious link does not make its sender a scammer."""
def risk_level(total_weight: int, finding_count: int) -> int:
    if total_weight >= 3 or finding_count >= 3:
        return 3
    if total_weight == 2:
        return 2
    if total_weight == 1:
        return 1
    return 0
RESPONSE = {0: "No action", 1: "Quiet monitoring", 2: "User warning", 3: "Moderator review"}
def explain(level: int, findings: list[dict]) -> str:
    if level == 0:
        return "No known indicators found."
    reasons = "; ".join(f["detail"] for f in findings)
    return f"Risk level {level} ({RESPONSE[level]}): {reasons}."
