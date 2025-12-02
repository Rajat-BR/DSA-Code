def reverse(x):
    MIN = -2147483648
    MAX = 2147483647

    num = x
    if x < 0:
        num = -1 * x
        lol = str(num)
        rev = int(lol[::-1])
        rev = -rev  

        if rev < MIN or rev > MAX:
            return 0

        return rev

    lol = str(num)
    rev = int(lol[::-1])

    if rev < MIN or rev > MAX:
        return 0

    return rev

print(reverse(-1024))