from fastapi import FastAPI
# from fastapi.responses import RedirectResponse
# from fastapi.requests import Request
# from fastapi.staticfiles import StaticFiles
# from fastapi.security import OAuth2PasswordBearer, SecurityScopes
# from fastapi.security.utils import get_authorization_scheme
# from fastapi.openapi.docs import get_swagger_ui_html
# from fastapi.openapi.routers import get_openapi
# from fastapi.openapi.security import get_security_scheme
# from fastapi.openapi.security.oauth2 import get_bearer_jsw_token_credentials
# from fastapi.security.oauth2 import SecurityScopes
# from starlette.requests import Request
# from starlette.responses import JSONResponse, RedirectResponse
# from starlette.status import HTTP_302_FOUND
# from starlette.types import Receive, Scope, Send
# from fastapi.middleware.cors import CORSMiddleware


from auth import login, registration
from api import dashboard, healthcheck

app = FastAPI(
    title="FastAPI Job Suggestion API",
    description="This API provides a job suggestion feature based on the user's interests",
    version="1.0.0",
    
)

# app.include_router(login.router)
# app.include_router(registration.router)
app.include_router(dashboard.router)
app.include_router(healthcheck.router)

# app.mount("/static", StaticFiles(directory="static"), name="static")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
