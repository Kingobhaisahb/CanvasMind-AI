from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str

    hf_token: str

    hf_image_model: str = "black-forest-labs/FLUX.1-dev"

    hf_analysis_model: str = "Qwen/Qwen3-32B"

    jwt_secret: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()