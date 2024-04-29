
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    app_name: str = "Adastra"
    pg_user: str
    pg_password: str
    pg_database: str
    pg_host: str

    model_config = SettingsConfigDict(env_file=".env")

    def get_postgres_url(self):
        return f"postgresql://{self.pg_user}:{self.pg_password}@{self.pg_host}:5432/{self.pg_database}"


settings = Settings()
