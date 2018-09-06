from abc import ABC, abstractmethod


class BaseConverter(ABC):

    @abstractmethod
    def convert(self, resource):
        """converts specified resource to json"""
        pass
