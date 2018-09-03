def get_sheet_name():
    return 'MICs List by CC'

def get_sheet_reader():
    from mic_tac_toe.resource_converters.excel import MicSheetReader
    return type(MicSheetReader)

def get_url():
    return 'https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls'

def get_bucket():
    return ''

def get_aws_access_key_id():
    return ''

def get_aws_secret_access_key():
    return ''