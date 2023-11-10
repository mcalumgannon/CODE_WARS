# recursive functions
def factorial(n):
    if n == 1:          # Base case
        return 1
    else:               # Recursive case
        return n * factorial(n - 1)
print(factorial(5))
# memoization
# exponentiation