def reverse(x):
    res = 0
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True
    while x:
        res *= 10
        res += x % 10
        x -= x % 10
        x //= 10
    return res if not is_negative else -res