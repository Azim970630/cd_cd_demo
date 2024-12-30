# tests/unit/test_function.py
import pytest
from app.functions import add, subtract


@pytest.mark.unit
def test_add():
    assert add(1, 2) == 3


@pytest.mark.unit
def test_subtract():
    assert subtract(3, 1) == 2
