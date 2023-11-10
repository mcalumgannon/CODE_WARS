def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == -1:
        return 1

    a, b = 0, 1
    sign = -1 if n < 0 and n % 2 == 0 else 1
    n = abs(n)

    transformation_matrix = [[1, 1], [1, 0]]
    
    def multiply_matrix(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def power_matrix(M, n):
        if n == 1:
            return M
        if n % 2 == 0:
            half_pow = power_matrix(M, n // 2)
            return multiply_matrix(half_pow, half_pow)
        else:
            half_pow = power_matrix(M, (n - 1) // 2)
            return multiply_matrix(M, multiply_matrix(half_pow, half_pow))

    powered_matrix = power_matrix(transformation_matrix, n - 1)

    result = sign * powered_matrix[0][0]
    return result

# Example usage:
result = fib(-20000)
print(result)  # Output: A very large negative Fibonacci number.



