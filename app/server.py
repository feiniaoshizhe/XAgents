from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from configs import settings
from controllers import mcp_router, app_router

app = FastAPI()
app.include_router(app_router)
# 绑定 mcp 服务
mcp = FastApiMCP(app)
mcp.mount(mcp_router)

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
