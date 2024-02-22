# Initialize the sum to 0
sum_multiples = 0

# Iterate through numbers from 1 to 999
for i in range(1, 1000):
    # Check if the number is a multiple of 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        sum_multiples += i

# Output the result
print("the sum is :",sum_multiples)