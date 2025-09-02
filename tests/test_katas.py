import pytest
from src import katas

def test_add_numbers():
    assert katas.add_numbers(2, 2) == 4

def test_is_palindrome():
    assert katas.is_palindrome("Racecar") is True
    assert katas.is_palindrome("hello") is False
