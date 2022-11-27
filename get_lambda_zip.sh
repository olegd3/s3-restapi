rm lambda_function.zip
cd lib/
zip ../lambda_function.zip -r .
cd ..
zip lambda_function.zip -u app -r
zip lambda_function.zip -u main.py
aws s3 cp lambda_function.zip s3://ipcam-lamba-zips
aws lambda update-function-code \
    --function-name  SaveObjectToBucket \
    --s3-bucket ipcam-lamba-zips \
    --s3-key lambda_function.zip
