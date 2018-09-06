from nose.tools import assert_equal

from mic_tac_toe.resource_locators import UrlResourceLocator

resource_locator = UrlResourceLocator()


def test_should_handle_invalid_url():
    resource_bytes = resource_locator.locate("not a valid url")
    assert_equal(len(resource_bytes), 0)


def test_should_handle_valid_url():
    incorrect_url = ''.join(['a' for i in range(0, 100)])
    resource_bytes = resource_locator.locate("www.{}.com".format(incorrect_url))
    assert_equal(len(resource_bytes), 0)


def test_should_handle_actual_url():
    resource_bytes = resource_locator.locate("www.example.com")
    assert len(resource_bytes) > 0

