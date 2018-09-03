import math

from .sheet_reader import SheetReader

class MicSheetReader(SheetReader):

    def __init__(self, sheet_name):
        super().__init__(sheet_name)

    def read(self, df):
        """Reads sheet with mic information and return array"""

        if df is None:
            return False, []

        keys = [self._sanitize_key(k) for k in df.keys()]
        return True, [self._convert(row, keys) for row in df.values]

    @staticmethod
    def _convert(row, keys):

        item = {}

        for index, value in enumerate(row):

            if not MicSheetReader._is_valid(value):
                continue

            item[keys[index]] = MicSheetReader._convert_value(value)

        return item

    @staticmethod
    def _is_valid(value):
        """Checks if value is valid"""
        if isinstance(value, str) and value == '':
            return False

        if isinstance(value, float) and math.isnan(value):
            return False

        return True

    @staticmethod
    def _convert_value(value):

        if isinstance(value, str):
            return value.lower()

        return value

    @staticmethod
    def _sanitize_key(value):
        """Sanitises the keys"""
        return value.replace(' ', '-').lower()