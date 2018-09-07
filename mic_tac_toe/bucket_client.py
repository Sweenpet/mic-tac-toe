import logging

log = logging.getLogger(__name__)


class BucketClient:

    def __init__(self, s3, bucket):
        self._s3 = s3
        self._bucket = bucket
        self._raw = 'raw'
        self._processed = 'processed'

        self._initialize(self._s3)

    def _initialize(self, s3):

        if all(b.name != self._bucket for b in s3.buckets.all()):
            s3.create_bucket(Bucket=self._bucket)

    def push_to_processed(self, file_name, content):
        self._try_push("processed/{}".format(file_name), content, self._bucket)

    def push_to_raw(self, file_name, content):
        self._try_push("raw/{}".format(file_name), content, self._bucket)

    def _try_push(self, file_name, content, bucket):

        try:
            self._s3.meta.client.put_object(Body=content, Bucket=bucket,Key=file_name)
        except Exception as e:
            log.error("Error pushing file to s3, {}".format(e))

