import requests
import logging

from .resource_locator import ResourceLocator
from .content_type import ContentType

log = logging.getLogger(__name__)

class UrlResourceLocator(ResourceLocator):

    def locate(self, url):

        try:
            response = requests.get(url)

            if not response.ok:
                log.error("Response returned invalid status code: ({})".format(response.status_code))
                return self._default_value()

            if response.content is None or len(response.content) == 0:
                log.error("Content is none or empty")
                return self._default_value()

            return ContentType.XLSX, response.content

        except Exception as e:
            log.error("Error sending request: {}".format(e))

        return self._default_value()

    @staticmethod
    def _default_value():
        return ContentType.XLSX, []

