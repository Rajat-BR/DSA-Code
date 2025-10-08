# Problem: Count Harshad Numbers from 1 to N
# A Harshad number (or Niven number) is a number that is divisible by the digit_sum of its digits.
# Example: 18 → digit_sum of digits = 1 + 8 = 9 → 18 % 9 == 0 → Harshad

def harshad(n):
    count = 0
    for i in range(1, n+1):
        num = i
        digit_sum = 0
        last = 0
        while num > 0:
            last = num % 10
            digit_sum = digit_sum + last
            num //= 10
        if i % digit_sum == 0:
            count += 1 
    return count

print(harshad(20))