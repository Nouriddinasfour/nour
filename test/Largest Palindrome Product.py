def is_palindrome(num):
    # Check if a number is a palindrome by comparing with its reverse
    return str(num) == str(num)[::-1]

def largest_3_digit_palindrome_product():
    largest_palindrome = 0
    factors = (0, 0)
    
    # Start from the largest 3-digit number and go down to the smallest
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):  # Check all 3-digit numbers for j
            product = i * j
            if is_palindrome(product):
                if product > largest_palindrome:
                    largest_palindrome = product
                    factors = (i, j)
    
    return largest_palindrome, factors

# Execute the function
largest_palindrome, factors = largest_3_digit_palindrome_product()
print(f"The largest palindrome made from the product of two 3-digit numbers is: {largest_palindrome}")
print(f"This palindrome is the product of numbers: {factors}")

