from pydantic_settings import BaseSettings, SettingsConfigDict

class AIConfig(BaseSettings):
    embed_model: str = ""


class Settings(BaseSettings):
    REQ_API_KEY: str = ""
    DATABASE_URL: str = ""
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
ai_config = AIConfig()