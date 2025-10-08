# Problem: Count numbers with strictly increasing digits
# A number has strictly increasing digits if each digit is smaller than the digit to its right.
# Example: 123 → digits 1<2<3 ✅, 321 → 3>2>1 ❌, 135 → 1<3<5 ✅
# Task: Write a function increasing_digit_count(nums) that returns how many numbers in the list have strictly increasing digits

nums = [123, 321, 135, 134, 121, 359, 696, 69]

def lol(nums):
    count = 0
    for n in nums:
        digit = n % 10
        n //= 10
        flow = True   #reset flow after every loop, otherwise ill get wrong answer
        while n > 0:
            now = n % 10
            if now < digit :
                flow = True
            elif now >= digit:
                flow = False
                break
            digit = now
            n //= 10
        if flow == True:
            count +=1
    return count

print(lol(nums))
