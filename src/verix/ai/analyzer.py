from ..detection.classifier import classify
from .local import classify_local
def analyze(text: str, cloud_enabled: bool = False) -> dict:
    result = classify(text)
    result["local_ai"] = classify_local(text)
    result["cloud_enabled"] = cloud_enabled
    return result
