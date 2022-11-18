from fastapi import APIRouter, Depends

from app.endpoints.deps import s3_auth
from botocore.client import BaseClient


router = APIRouter()


@router.get("/")
@router.get("")
def get_buckets(s3: BaseClient = Depends(s3_auth)):
    response = s3.list_buckets()
    project = 'TestProject'
    result = {
        'project': project,
        'buckets': response['Buckets']
    }
    return result
