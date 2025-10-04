'''
Not a LEETCODE Problem
Problem:

Given a positive integer n, repeatedly replace n with the absolute difference between the product of its digits and the sum of its digits, until n becomes a single-digit number. Return that single-digit number.

Example:
	•	Input: n = 59
	•	Step 1: sum = 5+9 = 14, product = 5*9 = 45 → abs(45-14) = 31
	•	Step 2: sum = 3+1 = 4, product = 3*1 = 3 → abs(3-4) = 1
	•	Output: 1
'''
def fun(n):
    sum = 0
    product = 1
    if n < 10:
        return n
    while n > 0:
        sum += n % 10 
        product *= n % 10 
        n = n // 10
    ans = abs(product - sum)
    return fun(ans) 

print(fun(59))