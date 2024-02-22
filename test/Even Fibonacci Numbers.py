def sum_even_fibonacci(limit):
    # Starting values for Fibonacci sequence
    a, b = 1, 2
    total_sum = 0

    # Continue until the next Fibonacci number exceeds the limit
    while a <= limit:
        # If the number is even, add it to the sum
        if a % 2 == 0:
            total_sum += a
        # Generate the next number in the sequence
        a, b = b, a + b

    return total_sum

# The limit provided is four million
limit = 4000000

# Calculate and print the result
result = sum_even_fibonacci(limit)
print(f"The sum of the even-valued terms in the Fibonacci sequence (not exceeding {limit}): {result}")
