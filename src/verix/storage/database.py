import sqlite3
from pathlib import Path
from .models import SCHEMA
def connect(path: str) -> sqlite3.Connection:
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(p)); conn.executescript(SCHEMA); conn.commit(); return conn
def record_detection(conn, guild_id, channel_id, message_id, indicator_type, risk_level, explanation, created_at):
    cur = conn.execute("INSERT INTO detections (guild_id, channel_id, message_id, indicator_type, risk_level, explanation, created_at) VALUES (?,?,?,?,?,?,?)", (guild_id, channel_id, message_id, indicator_type, risk_level, explanation, created_at))
    conn.commit(); return cur.lastrowid
