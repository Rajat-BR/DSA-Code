#Convert Roman number to numeric value [Leetcode : Easy]
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

dict = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L": 50,
    "C": 100, 
    "D": 500,
    "M" : 1000
}

a = ("MCCLVII")
s = a[::-1] # Reverse the string and traverse in back order
ans = dict[s[0]] #start with the first (last) value

for i in range(1, len(s)):

    if dict.get(s[i]) < dict.get(s[i-1]): #If next element is lesser than the previuos elements then minus 
        ans = ans - dict.get(s[i])
    else:
        ans = ans + dict.get(s[i])


print(ans)