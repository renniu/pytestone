import pytest
import yaml


def inc(x):
    return x + 1
def div(a, b):
    return a/b

@pytest.mark.low
def test_answer():
    assert inc(3) == 4

@pytest.mark.parametrize("a,b",yaml.safe_load(open("/Users/renniu/PycharmProjects/pythonProject2/web/test/data.yaml")))
@pytest.mark.high
def test_div(a,b):
    assert div(a,b) == 3
