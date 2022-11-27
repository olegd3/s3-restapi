import json
import os
import requests

S3_UPLOAD_URL = "http://127.0.0.1:8000"


# S3_UPLOAD_URL = "https://yxjb2kqpe5qhc46ypxo6zsp6eu0vuubx.lambda-url.us-east-2.on.aws"
# access_token = "sdfJHKsdfjJKHKJsdfJKHJKysdfJKHsdfJKHs"  # TODO: get fresh Token here


def upload_engagement_file(filepath):
    folder = 'test_upl_folder'
    url = S3_UPLOAD_URL + "/upload" + '?folder=' + folder  # add any URL parameters if needed
    with open('/home/oleg/PycharmProjects/s3-restapi/.temp/aws_lambda.txt', "rb") as fobj:
        file_obj = fobj.read()
        file_basename = os.path.basename(filepath)
        file_to_upload = [
            ('file_obj', (file_basename, file_obj, 'text/plain'))
        ]
        payload = {}
        headers = {}
        # headers = {"Authorization": "Bearer %s" % access_token}
        upload_response = requests.post(url=url, headers=headers, files=file_to_upload, data=payload, )
    # TODO logging
    # print(upload_response.json())
    return upload_response


if __name__ == "__main__":
    filepath = '/home/oleg/PycharmProjects/s3-restapi/.temp/aws_lambda.txt'
    upload_engagement_file(filepath)
