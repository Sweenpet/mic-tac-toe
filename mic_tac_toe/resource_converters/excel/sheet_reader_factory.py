from .mic_sheet_reader import MicSheetReader


class SheetReaderFactory:

    @staticmethod
    def create(method_type, sheet_name):

        if method_type == type(MicSheetReader):
            return MicSheetReader(sheet_name)

        raise ValueError("incorrect method type specified")