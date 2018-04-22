"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

print("Computing smallest multiple common to n: 1-20...")
start = time.time()

def smallest_common_multiple():
    scp = 0
    divisors = range(11, 21)
    multiple = 2520
    iter = 0
    for i in range(1, 20):
        iter += i
    while(scp == 0):
        for i in divisors:
            remainder = False
            if multiple%i != 0:
                remainder = True
                break
        if remainder == False:
            scp = multiple
        multiple += iter
    return scp

print(smallest_common_multiple())
#232792560

end = time.time()
print("Computed in "+str(end-start)+" seconds.")
