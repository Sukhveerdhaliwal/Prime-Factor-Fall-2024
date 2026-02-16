"""
prime.py -- Write the application code here
"""
import pytest

def test_non_integer_raises_ValueError():
    with pytest.raises(ValueError):
        generate_prime_factors("A String")
    with pytest.raises(ValueError):
        generate_prime_factors(2.3)
    with pytest.raises(ValueError):
        generate_prime_factors([1,1])

def test_1_Returns_Empty_List():
    """Step 2: Assert that the number generates an Empty List[]"""
    assert generate_prime_factors(1) == []

def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError('Input must be an integer')
