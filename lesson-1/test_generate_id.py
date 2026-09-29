from generate_id import generate_id
import pytest



def test_generate_id_not():
    with pytest.raises(TypeError):
        generate_id("a")
    with pytest.raises(TypeError):
        generate_id(1.5)
    with pytest.raises(TypeError):
        generate_id(None)
    with pytest.raises(ValueError):
        generate_id(0)
    with pytest.raises(ValueError):
        generate_id(-2)
    with pytest.raises(TypeError):
        generate_id([])

def test_generate_id_length():
    assert len(generate_id(6)) == 6
    assert len(generate_id(7)) == 7
    assert len(generate_id(12)) == 12
    assert len(generate_id(1)) == 1