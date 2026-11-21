"""Configuration. Secrets come only from the environment — never from code, never from the DB."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    discord_token: str = ""
    discord_guild_id: int | None = None
    database_path: str = "data/verix.db"
    log_level: str = "INFO"
    cloud_ai_enabled: bool = False
    cloud_ai_provider: str = ""
    cloud_ai_api_key: str = ""

    @property
    def has_discord_token(self) -> bool:
        return bool(self.discord_token.strip())

settings = Settings()
