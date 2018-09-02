import logging
import uuid

from resource_locators import UrlResourceLocator
from resource_locators import ContentType
from resource_converters.excel import SheetReaderFactory
from resource_converters import XlsConverter
from bucket_client import BucketClient

from settings import get_url, get_sheet_reader, get_sheet_name, \
    get_aws_access_key_id, get_aws_secret_access_key, get_bucket

log = logging.getLogger(__name__)

def main():

    locator = UrlResourceLocator()
    content_type, content_bytes = locator.locate(get_url())

    if len(content_bytes) == 0:
        return

    content_type = ContentType(content_type)

    if content_type != ContentType.XLSX:
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