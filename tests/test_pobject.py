from pobject import P
from pobject import I


def test_to_json_string():
    assert I({}).to_json_string() == "{}"
