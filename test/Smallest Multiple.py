from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def smallest_multiple(n):
    lcm_value = 1
    for i in range(1, n+1):
        lcm_value = lcm(lcm_value, i)
    return lcm_value

# Find the smallest multiple of all numbers from 1 to 20
smallest_num = smallest_multiple(20)
print(smallest_num)
