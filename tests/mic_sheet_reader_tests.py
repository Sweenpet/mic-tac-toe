from pandas import DataFrame
from nose.tools import assert_equal

from mic_tac_toe.resource_converters.excel import MicSheetReader

msr = MicSheetReader('Sheet1')

def test_can_handle_null():
    success, data = msr.read(None)
    assert not success
    assert_equal(len(data), 0)

def test_should_parse_valid_dataframe():
    df = DataFrame()

    numbers = [i for i in range(0,10)]
    text = map(str, numbers)

    df['Some Floats'] = numbers
    df['Some Text'] = text

    success, _ = msr.read(df)

    assert success

def test_should_remove_invalid_date_dataframe():
    df = DataFrame()
    df['Some Floats'] = [float(i if i % 10 == 0 else 'NaN') for i in range(0, 100)]
    df['Some Text'] = [str(i if i % 20 == 0 else '') for i in range(0, 100)]

    _, output = msr.read(df)

    assert 'some-floats' not in output[9]
    assert 'some-text' not in output[19]

def test_should_sanitize_key_names():
    df = DataFrame()
    df['Some Floats'] = [1]
    df['Some Text'] = [str(1)]

    _, output = msr.read(df)

    keys = list(sorted(output[0].keys()))

    assert keys[0] == 'some-floats'
    assert keys[1] == 'some-text'

def test_should_make_text_lowercase():
    df = DataFrame()
    df['Some Text'] = ['MIC','TAC','TOE']

    _, output = msr.read(df)

    values = list(sorted(v['some-text'] for v in output))

    assert values[0] == 'mic'
    assert values[1] == 'tac'
    assert values[2] == 'toe'




