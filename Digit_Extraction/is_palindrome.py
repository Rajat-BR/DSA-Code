# 121 -> true 
# -121 -> False (Backwards of -121 id 121-)

def is_palindrome(x):
    initial_value = x
    ans = 0
    while int(x) > 0 and int(x) != 0:
        last = x % 10
        ans = ans * 10 + last
        x = x // 10
    if ans == initial_value:
        return True
    else: 
        return False

print(is_palindrome(12121))
        
