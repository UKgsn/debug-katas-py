def add_numbers(a, b):
    # BUG: wrong operator
    return a - b

def is_palindrome(s: str) -> bool:
    # BUG: case-sensitive check
    return s == s[::-1]
