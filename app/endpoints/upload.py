from typing import Optional, Union

from botocore.client import BaseClient
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse

from app.settings import settings
from app.endpoints.deps import s3_auth
from app.s3.upload import upload_file_to_bucket

router = APIRouter()


# @router.post("/", status_code=status.HTTP_201_CREATED, summary="Upload files to AWS S3 Buckets",
#              description="Upload a valid file to AWS S3 bucket", name="POST files to AWS S3",
#              response_description="Successfully uploaded file to S3 bucket")
@router.post("/")
@router.post("")
def upload_file(
        *, bucket: Union[str, None] = None,
        folder: str,
        s3: BaseClient = Depends(s3_auth),
        file_obj: UploadFile = File(...)):
    if not bucket:
        bucket = settings.S3_DEFAULT_BUCKET
    upload_obj = upload_file_to_bucket(s3_client=s3, file_obj=file_obj.file,
                                       bucket=bucket,
                                       folder=folder,
                                       object_name=file_obj.filename
                                       )

    if upload_obj:
        return JSONResponse(content=f"{file_obj.filename} has been uploaded to {folder} in bucket {bucket}",
                            status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="File could not be uploaded")
