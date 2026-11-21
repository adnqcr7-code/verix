SCHEMA = """
CREATE TABLE IF NOT EXISTS guilds (guild_id TEXT PRIMARY KEY, configuration TEXT, enabled_modules TEXT, created_at TEXT);
CREATE TABLE IF NOT EXISTS detections (detection_id INTEGER PRIMARY KEY AUTOINCREMENT, guild_id TEXT, channel_id TEXT, message_id TEXT, indicator_type TEXT, risk_level INTEGER, explanation TEXT, created_at TEXT);
CREATE TABLE IF NOT EXISTS indicators (indicator_id INTEGER PRIMARY KEY AUTOINCREMENT, indicator_type TEXT, indicator_value_hash TEXT, status TEXT, source TEXT, confidence REAL, first_seen TEXT, last_seen TEXT);
CREATE TABLE IF NOT EXISTS reports (report_id INTEGER PRIMARY KEY AUTOINCREMENT, detection_id INTEGER, report_status TEXT, reviewer_decision TEXT, created_at TEXT);
CREATE TABLE IF NOT EXISTS audit_logs (event_id INTEGER PRIMARY KEY AUTOINCREMENT, actor_type TEXT, action TEXT, timestamp TEXT);
"""
