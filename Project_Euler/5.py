# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

# My quick thoughts:
# We just need to check that its divisible from 11 to 20
# We know that units must be cero, and 10ths must be even, because of the 20
# This only happens for 11 at 11*20, 11*40, etc.., enough to space between
# numbers to use brute force
n = 0
while True:
    n += 20
    ans = n * 11
    if n % 12 == 0 and n % 13 == 0 and n % 14 == 0 and n % 15 == 0\
            and n % 16 == 0 and n % 17 == 0 and n % 18 == 0 and n % 19 == 0:
        print(ans)
        break
