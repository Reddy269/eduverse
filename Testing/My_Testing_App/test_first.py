from unittest.mock import Mock

def test_is_prime_for_prime_number_return_true():
    from .primes import is_prime

    n = 5

    result = is_prime(n)

    assert result == True

def test_is_prime_for_edge_case_1_return_false():
    from .primes import is_prime

    n = 2
    result = is_prime(n)
    assert result == False