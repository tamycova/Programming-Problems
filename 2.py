# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will
# be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

ant_num = 0
post_num = 1
nums = []
while True:
    next_num = ant_num + post_num
    ant_num = post_num
    post_num = next_num
    if post_num >= 4 * 10**6:
        break
    if post_num % 2 == 0:
        nums.append(next_num)
print(sum(nums))
