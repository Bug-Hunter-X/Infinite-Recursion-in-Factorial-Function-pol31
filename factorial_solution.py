def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a non-negative integer"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # Output: 120
print(factorial(-1)) # Output: Error: Input must be a non-negative integer
print(factorial(3.14)) # Output: Error: Input must be a non-negative integer