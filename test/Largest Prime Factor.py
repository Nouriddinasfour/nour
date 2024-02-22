def largest_prime_factor(n):
    # Initialize the largest factor to the smallest prime number
    largest_factor = 2
    
    # Divide n by 2 until it's odd
    while n % 2 == 0:
        n = n // 2
    
    # Now that n is odd, we can check for factors from 3 onwards
    factor = 3
    while n != 1 and factor * factor <= n:
        if n % factor == 0:
            n = n // factor
            largest_factor = factor
        else:
            factor += 2  # Increment the factor by 2, since we know it's odd
    
    # If there's any number left, that is a prime factor
    if n > 1:
        largest_factor = n
    
    return largest_factor

# The number provided in the exercise
number = 600851475143

# Find and print the largest prime factor
largest_factor = largest_prime_factor(number)
print(f"The largest prime factor of the number {number} is: {largest_factor}")
