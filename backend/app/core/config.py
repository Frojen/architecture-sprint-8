from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )
    API_V1_STR: str = Field("", validation_alias="BACKEND_API_V1_STR")

    PROJECT_NAME: str = Field("Reports microservice", validation_alias="BACKEND_API_V1_STR")

    KEYCLOAC_URL: str = Field(validation_alias="BACKEND_KEYCLOAC_URL")
    KEYCLOAC_REALM: str = Field(validation_alias="BACKEND_KEYCLOAC_REALM")
    KEYCLOAC_CLIENT_ID: str = Field(validation_alias="BACKEND_KEYCLOAC_CLIENT_ID")
    KEYCLOAC_CLIENT_SECRET: str = Field(validation_alias="BACKEND_KEYCLOAC_CLIENT_SECRET")


settings = Settings()
