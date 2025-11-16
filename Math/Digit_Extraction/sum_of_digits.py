'''
Not a LEETCODE Problem
Write a function that takes an integer n and returns the sum of its digits until only one digit remains.

For example:
	•	n = 38 → 3 + 8 = 11 → 1 + 1 = 2 → output = 2
	•	n = 942 → 9 + 4 + 2 = 15 → 1 + 5 = 6 → output = 6
	•	n = 5 → already one digit → output = 5

'''

def fun(n):
    sum = 0
    if n < 10:
        return n
    while int(n)>0 and int(n)!= 0:
        sum = n % 10 + sum 
        n = n // 10
    return fun(sum) 

print(fun(69))