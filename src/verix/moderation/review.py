def review_queue_entry(detection_id: int, risk_level: int) -> dict:
    return {"detection_id": detection_id, "risk_level": risk_level, "status": "pending_review" if risk_level >= 3 else "no_action"}
