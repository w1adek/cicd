"""Tests"""

import pytest
import utils


@pytest.mark.parametrize("a,b, expected", [(1, 2, 3), (2, 3, 5), (4, 5, 9)])
def test_add(a, b, expected):
    """Test addition"""
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b, expected", [(1, 2, -1), (2, 3, -1), (4, 5, -1)])
def test_subtract(a, b, expected):
    """Test substraction"""
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b, expected", [(1, 2, 2), (2, 3, 6), (4, 5, 20)])
def test_multiply(a, b, expected):
    """Test multiplying"""
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    """Test dividing"""
    result = utils.divide(a, b)
    assert result == expected
