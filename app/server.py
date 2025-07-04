import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mcp import FastApiMCP
from starlette.responses import JSONResponse

from apis import mcp_router, app_router
from configs import settings

logger = logging.getLogger("main service")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(app_router)
# 绑定 mcp 服务
mcp = FastApiMCP(app)
mcp.mount(mcp_router)


# Global exception handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logging.error(f"HTTPException: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


# Global exception handler for all uncaught exceptions
@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    logging.error(f"Generic Exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error, please try again later."},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app=app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
        log_level=settings.LOGGING_LEVEL,
    )
