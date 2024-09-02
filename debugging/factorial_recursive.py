#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except IndexError:
        print("Error: No input provided. Please provide an integer as an argument.")
    except ValueError as e:
        print(f"Error: {e}")