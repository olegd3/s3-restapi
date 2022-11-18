cd app/lib/
zip ../../lambda_function.zip -r .
cd ..
#zip ../lambda_function.zip -u . -r -x
zip ../lambda_function.zip -u main.py
zip ../lambda_function.zip -u settings.py
zip ../lambda_function.zip -u ./endpoints/ -r
