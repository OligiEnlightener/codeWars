def gcd_func(a: int, b: int) -> int | None:
    if a >= b:
        if a % b == 0:
            return b
        else:
            return gcd_func(b, a % b)
    else:
        return gcd_func(b, a)


print(gcd_func(6, 6))

assert gcd_func(15, 5) == 5
assert gcd_func(9, 6) == 3
assert gcd_func(17, 13) == 1