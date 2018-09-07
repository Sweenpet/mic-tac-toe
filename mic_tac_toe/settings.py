class Settings:

    def __init__(self, settings):
        import mic_tac_toe.resource_converters.excel as excel_sheet_reader

        self._url = settings["url"]
        self._sheet_name = settings["sheet_name"]
        self._sheet_reader = type(getattr(excel_sheet_reader, settings["sheet_reader"]))
        self._bucket = settings["bucket"]

    @property
    def url(self):
        return self._url

    @property
    def sheet_name(self):
        return self._sheet_name

    @property
    def sheet_reader(self):
        return self._sheet_reader

    @property
    def bucket(self):
        return self._bucket


def get_settings():
    import json
    import os

    def get_settings_inner(path):
        with open(path) as f:
            json_settings = json.load(f)
            return Settings(json_settings)

    file_path = "settings.json"

    if os.path.exists(file_path):
        return get_settings_inner(file_path)

    # lambda hack

    file_path = os.path.join("mic_tac_toe", file_path)

    if os.path.exists(file_path):
        return get_settings_inner(file_path)

    raise FileNotFoundError("can't find settings.json")


def get_s3():
    import os
    import boto3

    from mic_tac_toe.credentials import AwsCredentials

    if 'HOME' in os.environ:
        home = os.environ['HOME']

        path = os.path.join(home, '.aws', 'credentials')

        cred =  AwsCredentials.init(path)

        print(cred.id)
        print(cred.key)

        if cred is not None:
            return boto3.resource('s3', aws_access_key_id=cred.id, aws_secret_access_key=cred.key)

    return boto3.resource('s3')
