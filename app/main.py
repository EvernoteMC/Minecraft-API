from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.routes.api import router as api_router
from app.core import config
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from fastapi.openapi.utils import get_openapi
from functools import lru_cache
from app.core.tags import OPENAPI_TAGS
from ratelimit import RateLimitMiddleware
from ratelimit.backends.redis import RedisBackend

# from app.core.rate_limit import rate_auth, rate_limit_config

# from app.core.events import create_start_app_handler, create_stop_app_handler


@lru_cache()
def get_settings():
    return config.Settings()


def get_application() -> FastAPI:
    application = FastAPI(
        debug=config.settings.debug,
        openapi_url=config.settings.openapi_url,
        docs_url=config.settings.docs_url,
        redoc_url=config.settings.redoc_url,
    )

    application.include_router(api_router, prefix=config.settings.api_prefix)

    def custom_openapi():
        if application.openapi_schema:
            return application.openapi_schema
        openapi_schema = get_openapi(
            title=config.settings.project_name,
            version=config.settings.version,
            routes=application.routes,
            tags=OPENAPI_TAGS,
            description=config.settings.description,
            servers=[
                # remove for production
                {"url": "http://localhost", "description": "Local"},
                {
                    "url": "https://development.obsidion-dev.com",
                    "description": "Development server",
                },
                {
                    "url": "https://staging.obsidion-dev.com",
                    "description": "Staging server",
                },
                {
                    "url": "https://api.obsidion-dev.com",
                    "description": "Production server",
                },
            ],
        )
        openapi_schema["info"]["contact"] = {
            "name": "API Support",
            "email": "leon@bowie-co.nz",
            "url": "https://discord.gg/invite/7BRD7s6",
        }
        openapi_schema["info"]["license"] = {
            "name": "GNU AGPL v3",
            "url": "https://www.gnu.org/licenses/agpl-3.0.html",
        }
        openapi_schema["info"]["termsOfService"] = "https://api.obsidion-dev.com/terms"
        application.openapi_schema = openapi_schema
        return app.openapi_schema

    application.openapi = custom_openapi

    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    # application.add_middleware(
    #     RateLimitMiddleware,
    #     authenticate=rate_auth,
    #     backend=RedisBackend(config.settings.cache_host),
    #     config=rate_limit_config,
    # )

    return application


app = get_application()
