import logging
import uuid
import json

from mic_tac_toe.resource_converters import XlsConverter
from mic_tac_toe.resource_locators import UrlResourceLocator

from mic_tac_toe.bucket_client import BucketClient
from mic_tac_toe.resource_converters.excel import SheetReaderFactory
from mic_tac_toe.settings import get_sheet_reader, \
    get_aws_access_key_id, get_aws_secret_access_key, get_bucket

log = logging.getLogger(__name__)

def handler(event, context):

    if event['body'] is None:
        log.error("body of request is empty")

    body = json.loads(event['body'])

    url = body['url']
    sheet_name = body['sheet_name']

    locator = UrlResourceLocator()
    content_bytes = locator.locate(url)

    if len(content_bytes) == 0:
        log.error('content bytes empty')


    bucket_client = BucketClient(get_aws_access_key_id(), get_aws_secret_access_key(),
                                 get_bucket())

    file_name = uuid.uuid4()

    bucket_client.push_to_raw("{}.xls".format(file_name), content_bytes)

    sheet_reader = SheetReaderFactory.create(get_sheet_reader(), sheet_name)
    xls_converter = XlsConverter(sheet_reader)

    success, output = xls_converter.convert(content_bytes)

    if not success:
        log.error("There was an issue converting the file to json")

    bucket_client.push_to_processed("{}.json".format(file_name), output)

if __name__ == "__main__":

    from mic_tac_toe.settings import get_sheet_name, get_url

    request = {
        'body': json.dumps({
            'url': get_url(),
            'sheet_name': get_sheet_name()
        })
    }

    handler(request, None)