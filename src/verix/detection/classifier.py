"""Local classifier entry point — rule engine first. AI adapters plug in here later, never bypassing rules."""
from .rules import check_rules
from .scoring import risk_level, explain
def classify(text: str) -> dict:
    findings = check_rules(text)
    weight = sum(f["weight"] for f in findings)
    level = risk_level(weight, len(findings))
    return {"risk_level": level, "findings": findings, "explanation": explain(level, findings)}
