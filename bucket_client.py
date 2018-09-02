import boto3
import logging

log = logging.getLogger(__name__)


class BucketClient:

    def __init__(self, aws_id, aws_key, bucket):
        self.s3 = boto3.resource('s3',
                            aws_access_key_id=aws_id,
                            aws_secret_access_key=aws_key)

        self.bucket = bucket
        self.raw = 'raw'
        self.processed = 'processed'

        self._initialize(self.s3)

    def _initialize(self, s3):

        if all(b.name != self.bucket for b in s3.buckets.all()):
            s3.create_bucket(Bucket=self.bucket)

    def push_to_processed(self, file_name, content):
        self._try_push("processed/{}".format(file_name), content, self.bucket)

    def push_to_raw(self, file_name, content):
        self._try_push("raw/{}".format(file_name), content, self.bucket)

    def _try_push(self, file_name, content, bucket):

        try:
            self.s3.meta.client.put_object(Body=content, Bucket=bucket,Key=file_name)
        except Exception as e:
            log.error("Error pushing file to s3, {}".format(e))

