from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # HTTP Request API Key
    BEINBOUT_AI_CALL_KEY: str = ""
    SERVICE_MODE: str = ""

    # Database URL
    DATABASE_URL: str = ""

    # Azure Key Credentials
    AZURE_AI_KEY_CREDENTIALS: str = ""
    AZURE_AI_ENDPOINT: str = ""
    AZURE_AI_API_VERSION: str = ""

    AZURE_AI_EMBEDDING_MODEL_NAME: str = ""
    AZURE_AI_EMBEDDING_DEPLOYMENT: str = ""

    AZURE_AI_LLM_MODEL_NAME: str = ""
    AZURE_AI_LLM_DEPLOYMENT: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        case_sensitive=False,
        env_ignore_empty=True,
    )


settings = Settings()
