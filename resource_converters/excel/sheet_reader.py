from abc import ABC, abstractmethod

class SheetReader(ABC):

    def __init__(self, sheet):
        self.sheet = sheet

    @abstractmethod
    def read(self, df):
        """Accepts a Dataframe representation of the sheet
        and returns the json version"""


    def can_read(self, sheet_name):
        return self.sheet == sheet_name

    @property
    def sheet_name(self):
        return  self.sheet

