from io import BytesIO
import json
import logging
from pandas import ExcelFile

from resource_converters.base_converter import BaseConverter

log = logging.getLogger(__name__)

class XlsConverter(BaseConverter):

    def __init__(self, sheet_reader):
        self.sheet_reader = sheet_reader
        super().__init__()

    def convert(self, file_bytes):
        """Accepts a bytes array and returns a json string """

        excel_file = None

        try:
            excel_file = ExcelFile(BytesIO(file_bytes))
        except Exception as e:
            log.error("Error reading in excel bytes, {}".format(e))

        if excel_file is None:
            return self._default_value()

        if self.sheet_reader.sheet_name not in excel_file.sheet_names:
            return self._default_value()

        try:
            df = excel_file.parse(self.sheet_reader.sheet_name)
            success, output = self.sheet_reader.read(df)

            if not success:
                return self._default_value()

            return True, json.dumps(output, sort_keys=True)
        except Exception as e:
            log.error("Error parsing file: {}".format(e))

        return self._default_value()

    @staticmethod
    def _default_value():
        return False, ""