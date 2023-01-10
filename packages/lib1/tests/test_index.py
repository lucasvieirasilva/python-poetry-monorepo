from pymonorepo_lib1 import index


def test_index():
    assert index.hello() == "Hello lib1"
