from fastapi import APIRouter, Depends

from app.endpoints.deps import s3_auth
from botocore.client import BaseClient


router = APIRouter()

# https://stackoverflow.com/questions/71984078/fastapi-application-as-an-aws-lambda-function-url-gets-stuck-in-eternal-redirect
@router.get("")
@router.get("/")
def get_buckets(s3: BaseClient = Depends(s3_auth)):
    response = s3.list_buckets()
    project = 'TestProject'
    result = {
        'project': project,
        'buckets': response['Buckets']
    }
    return result
