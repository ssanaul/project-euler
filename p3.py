"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(num):
    if num%2 == 0:
        return False
    i = 3
    upper_bound = int(num/3)
    while i < upper_bound:
        if num%i == 0:
            return False
        i += 2
        upper_bound = int(num/i)
    return True
    
def lpf(num):
    if num%2 == 0 and is_prime(num/2):
        return "LPF("+str(num)+"): "+str(num/2)
    i = 3
    upper_bound = int(num/3)
    while i < upper_bound:
        if num%i == 0:
            if is_prime(num/i):
                return "LPF("+str(num)+"): "+str(num/i)
            if is_prime(i):
                lpf = i
        i += 2
        upper_bound = int(num/i)
    return "LPF("+str(num)+"): "+str(lpf)

print(lpf(600851475143))
#6857
