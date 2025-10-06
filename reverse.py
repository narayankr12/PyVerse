def reverse(x):
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_x = int(str(x_abs)[::-1])
    if reversed_x > 2**31 - 1:
        return 0
    return sign * reversed_x
