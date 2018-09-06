aws s3 cp app/dist.zip s3://$BUCKET
aws lambda update-function-code --function-name $LAMBDA --s3-bucket $BUCKET --s3-key dist.zip --publish