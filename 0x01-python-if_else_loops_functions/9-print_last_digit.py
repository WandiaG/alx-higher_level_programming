#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(number):
    """Print and return the last digit of a number."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)