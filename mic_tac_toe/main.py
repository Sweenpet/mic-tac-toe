import logging
import uuid

from mic_tac_toe.resource_converters import XlsConverter
from mic_tac_toe.resource_locators import UrlResourceLocator

from mic_tac_toe.bucket_client import BucketClient
from mic_tac_toe.resource_converters.excel import SheetReaderFactory
from mic_tac_toe.settings import get_url, get_sheet_reader, get_sheet_name, \
    get_aws_access_key_id, get_aws_secret_access_key, get_bucket

log = logging.getLogger(__name__)

def main():

    locator = UrlResourceLocator()
    content_bytes = locator.locate(get_url())

    if len(content_bytes) == 0:
        return

    bucket_client = BucketClient(get_aws_access_key_id(), get_aws_secret_access_key(),
                                 get_bucket())

    file_name = uuid.uuid4()

    bucket_client.push_to_raw("{}.xls".format(file_name), content_bytes)

    sheet_reader = SheetReaderFactory.create(get_sheet_reader(), get_sheet_name())
    xls_converter = XlsConverter(sheet_reader)

    success, json = xls_converter.convert(content_bytes)

    if not success:
        log.error("There was an issue converting the file to json")

    bucket_client.push_to_processed("{}.json".format(file_name), json)


if __name__ == "__main__":
    main()