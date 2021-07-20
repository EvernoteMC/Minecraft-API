import secrets
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import AnyHttpUrl
from pydantic import BaseSettings
from pydantic import EmailStr
from pydantic import HttpUrl
from pydantic import PostgresDsn
from pydantic import validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str
    SENTRY_DSN: Optional[HttpUrl] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            return None
        return v

    POSTGRES_SERVER: Optional[str]
    POSTGRES_USER: Optional[str]
    POSTGRES_PASSWORD: Optional[str]
    POSTGRES_DB: Optional[str]

    DATABASE_URL: Optional[PostgresDsn] = None

    @validator("DATABASE_URL", pre=True)
    def validate_db_url(cls, v) -> Union[HttpUrl, None]:  # noqa: B902,N805
        if v == "":
            return None
        return v
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        if values.get("DATABASE_URL") is not None:
            return "+asyncpg:".join(values.get("DATABASE_URL").split(":", 1))
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str
    FIRST_SUPERUSER_PHONE_NUMBER: str
    FIRST_SUPERUSER_FULL_NAME: str

    class Config:
        case_sensitive = True


settings = Settings()
