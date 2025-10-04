# =========================================
#             Strong Number
# =========================================
# A Strong number is a number such that the sum of the factorials of its digits
# is equal to the number itself.
# Example:
#   145 → 1! + 4! + 5! = 145 → True
#   123 → 1! + 2! + 3! = 9 ≠ 123 → False
'''
def fact(x):                     As strong number need factorials of only 0 - 9
    fact = 1.                    This is not optimal as it calculates factorial
    for i in range(1, x+1):      for every number.
        fact *= i
    return fact                  So, best to make a list of facts of 0 - 9
                                 and directly fetch it
'''

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def is_strong(n):
    init = n
    ans = 0
    while n > 0:
        last = n % 10
        ans += factorials[last]
        n //= 10
    return ans == init

print(is_strong(40585))