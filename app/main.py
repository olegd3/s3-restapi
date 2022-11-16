from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.endpoints.api import api_router
from mangum import Mangum

app = FastAPI(title="S3 Buckets Info",description="Simple S3 Buckets uploader",
              openapi_url=f"/openapi.json")

app.include_router(api_router)
# handler = Mangum(app)
