import logging
import uuid
import json

from mic_tac_toe.resource_converters import XlsConverter
from mic_tac_toe.resource_locators import UrlResourceLocator

from mic_tac_toe.bucket_client import BucketClient
from mic_tac_toe.resource_converters.excel import SheetReaderFactory
from mic_tac_toe.settings import get_settings, get_s3

log = logging.getLogger(__name__)


def handler(event, context):

    settings = get_settings()

    locator = UrlResourceLocator()
    content_bytes = locator.locate(settings.url)

    if len(content_bytes) == 0:
        log.error('content bytes empty')

    bucket_client = BucketClient(get_s3(), settings.bucket)

    file_name = uuid.uuid4()

    bucket_client.push_to_raw("{}.xls".format(file_name), content_bytes)

    sheet_reader = SheetReaderFactory.create(settings.sheet_reader, settings.sheet_name)
    xls_converter = XlsConverter(sheet_reader)

    success, output = xls_converter.convert(content_bytes)

    if not success:
        log.error("There was an issue converting the file to json")

    bucket_client.push_to_processed("{}.json".format(file_name), output)


if __name__ == "__main__":
    handler(None, None)
