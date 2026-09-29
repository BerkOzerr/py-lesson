from generate_id import generate_id
import pytest
import string


@pytest.mark.parametrize("length", [1, 2, 12, 11])
def test_generate_id_length(length):
    result = generate_id(length)
    assert len(result) == length
    assert all(char in string.ascii_lowercase + string.digits for char in result)


@pytest.mark.parametrize("value", [0, -1, -2])
def test_generate_id_value(value):
    with pytest.raises(ValueError):
        generate_id(value)


@pytest.mark.parametrize("notType", ["a", " ", [], None])
def test_generate_id_type(notType):
    with pytest.raises(TypeError):
        generate_id(notType)
