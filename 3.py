# # The prime factors of 13195 are 5, 7, 13 and 29.
# # What is the largest prime factor of the number 600851475143 ?


def divisible(num, divisor):
    if num % divisor == 0 and num != divisor:
        return True


def prime(num):
    divisor = 2
    while num > divisor:
        if divisible(num, divisor):
            return False
        divisor += 1
    return True


def max_prime(num):
    i = 2
    new_num = None
    while True:
        if divisible(num, i):
            new_num = num // i
            if prime(new_num):
                return new_num
        i += 1

NUM = 1000
print(max_prime(NUM))


# w = NUM
# for x in range(2, 100000):
#     if w % x == 0:
#         w = w / x
#         print(x)
