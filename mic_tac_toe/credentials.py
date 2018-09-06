import logging
import os

log = logging.getLogger(__name__)


class AwsCredentials:

    def __init__(self, aws_id, key):
        self._id = aws_id
        self._key = key

    @property
    def id(self):
        return self._id

    @property
    def key(self):
        return self._key

    @staticmethod
    def init(path):

        if not os.path.exists(path):
            raise ValueError("settings file doesn't exist")

        try:

            def read(text):
                return text.split('=')[1]

            with open(path) as f:
                lines = f.readlines()

                aws_id = read(lines[1])
                key = read(lines[2])

                return AwsCredentials(aws_id, key)
        except Exception as e:
            log.error("unable to parse credentials file", e)

        return None
