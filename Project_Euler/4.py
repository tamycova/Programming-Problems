# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers


ans = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        n = str(i * j)
        if n == n[::-1] and int(n) > ans:
            ans = int(n)
print(ans)

# 0.7, brute force
