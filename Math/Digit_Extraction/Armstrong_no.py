# =========================================
#            Armstrong Number
# =========================================
# An Armstrong number is a number that is equal to the sum of its own digits
# each raised to the power of the number of digits.
# Example:
#   153 → 1^3 + 5^3 + 3^3 = 153 → True
#   123 → 1^3 + 2^3 + 3^3 = 36 ≠ 123 → False

def is_armstrong(n):
    count = 0
    ans = 0
    init = n
    no = n
    while n > 0: #Calculate the number of digits
        n //= 10
        count += 1

    while init > 0:
        last = init % 10
        ans += last ** count
        init //= 10

    return ans == no

print(is_armstrong(153))


