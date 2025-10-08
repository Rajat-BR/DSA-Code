#Convert a number to Roman Number [Leetcode : Medium]

mappings = [
    {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'},       
    {1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'},      
    {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'},      
    {1:'M', 2:'MM', 3:'MMM'}                                                         
]

def roman(x : int) -> str:
    index = 0 # 0 = units, 1 = tens , 2 = hundreds, 3 = thousands
    ans = ""
    while x > 0:
        num = x % 10
        if num != 0:
            ans = mappings[index][num] + ans 
        x //= 10
        index += 1
    return ans

print(roman(1259))

