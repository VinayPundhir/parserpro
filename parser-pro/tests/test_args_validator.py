from core.methods.args_validator.is_dict_string import is_dict_string
import pytest


def test_is_valid_dict_string():
    arg = '{"name":"parser","version":"0.1"}'
    assert is_dict_string(arg) == True


def test_is_invalid_dict_string():
    args = [
        '{"name":"parser","version""0.1"}',
        '{"name":"parser" "version":"0.1"}',
        '{"name":"parser","version":"0.1"',
    ]
    for arg in args:
        with pytest.raises(ValueError) as excinfo:
            is_dict_string(arg)
        assert "Error parsing arg" in str(excinfo.value)
