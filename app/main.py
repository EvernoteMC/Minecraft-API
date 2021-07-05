from typing import Any, Dict
import sentry_sdk
from app.api.api_v1.api import api_router
from app.core.config import settings
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

sentry_sdk.init(dsn=settings.SENTRY_DSN)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="This is the API developed by the [Obsidion-dev](https://github.com/Obsidion-dev) team for use by the minecraft community.",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

def custom_openapi() -> Dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://lh6.googleusercontent.com/x2UaZCMiAO_1jYhft4JcXq8aYBOikH67GA6oWABUEsQTESCpjDlqX8vr1XFdLwPG2xd8vhkNyIrbFfHUYRoDckBJ9RQmNdaVK6DC4lckHRheX8OfDMQdSSkKER2C_AgUSw=w1280"
    }
    # openapi_schema["info"]["termsOfService"] = "https://obsidion-dev.com/terms"
    openapi_schema["info"]["contact"] = {
        "name": "API Support",
        "email": "leon@bowie-co.nz",
        "url": "https://obsidion-dev.com",
    }
    openapi_schema["info"]["license"] = {
        "name": "GNU AGPL v3",
        "url": "https://www.gnu.org/licenses/agpl-3.0.html",
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
async def docs_redirect() -> RedirectResponse:
    """Redirect base request to docs."""
    response = RedirectResponse(url="/docs")
    return response


asgi_app = SentryAsgiMiddleware(app)