from verix.storage.database import connect, record_detection
def test_records_detection(tmp_path):
    conn = connect(str(tmp_path / "test.db"))
    did = record_detection(conn, "g1", "c1", "m1", "url", 2, "test", "2026-11-21T00:00:00Z")
    assert did == 1
    row = conn.execute("SELECT risk_level FROM detections WHERE detection_id=1").fetchone()
    assert row[0] == 2
