from check_filter import __app_name__, __author__, __version__


def test_name():
    assert __app_name__ == "check-filter"


def test_version():
    assert __version__ == "2.0.3"


def test_author():
    assert __author__ == "Arash Hatami <info@arash-hatami.ir>"
