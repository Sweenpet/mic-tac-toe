from abc import ABC, abstractmethod

class ResourceLocator(ABC):

    @abstractmethod
    def locate(self, path):
        """Accepts resource location and returns tuple of bytes and content_type"""
        pass





