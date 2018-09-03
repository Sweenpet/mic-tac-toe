from dateutil.parser import parse

def is_date(text):
    try:
        parse(text)
        return True
    except ValueError:
        pass

    return False


