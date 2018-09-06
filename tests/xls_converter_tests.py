import json

from mic_tac_toe.resource_converters import XlsConverter
from mic_tac_toe.resource_converters.excel import MicSheetReader

msr = MicSheetReader('Sheet1')
xlsc = XlsConverter(msr)


def test_should_handle_invalid_xls_bytes():
    invalid_bytes = bytes([1, 2, 3, 4, 5])
    success, json_output = xlsc.convert(invalid_bytes)

    assert not success
    assert json_output == ""


def test_should_correctly_read_xls_bytes():

    with open('sample.xlsx', 'rb') as f:
        content = f.read()
        success, json_output = xlsc.convert(content)

        assert success

        valid = True

        try:
            json.loads(json_output)
        except Exception:
            valid = False

        assert valid


def test_should_not_read_xls_bytes_if_wrong_sheet_name():

    msr = MicSheetReader('wrong-sheet-name')
    xlsc = XlsConverter(msr)

    with open('sample.xlsx', 'rb') as f:
        content = f.read()
        success, json_output = xlsc.convert(content)

        assert not success


