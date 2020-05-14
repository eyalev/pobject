from pobject import I


def test_to_json_string():
    assert I({}).to_json_string() == "{}"


def test_is_url():
    assert I("example.com").is_url
    assert I("example.com j").is_url is False
