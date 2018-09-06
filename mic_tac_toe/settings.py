import os
from mic_tac_toe.credentials import AwsCredentials


def get_sheet_name():
    return 'MICs List by CC'


def get_sheet_reader():
    from mic_tac_toe.resource_converters.excel import MicSheetReader
    return type(MicSheetReader)


def get_url():
    return 'https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls'


def get_bucket():

    if 'bucket' in os.environ:
        return os.environ['bucket']

    return 'steeleye-test'


def get_aws_access_credentials():
    import os

    if all(item in os.environ for item in ['aws_id', 'aws_key']):
        return AwsCredentials(os.environ['aws_id'], os.environ['aws_key'])

    home = os.environ['HOME']
    path = os.path.join(home, '.aws', 'credentials')

    return AwsCredentials.init(path)
