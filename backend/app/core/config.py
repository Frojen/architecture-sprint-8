from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )
    API_V1_STR: str = ""

    PROJECT_NAME: str = "Reports microservice"

    KEYCLOAC_URL: str = "http://localhost:8080"
    KEYCLOAC_REALM: str = "test-realm"
    KEYCLOAC_CLIENT_ID: str = "account"
    KEYCLOAC_CLIENT_SECRET: str = "secret"


settings = Settings()
