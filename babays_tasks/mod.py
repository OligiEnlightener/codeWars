def gcd_func(a: int, b: int) -> int:
        if a >= b:
            if b % a == 0:
                return a
            else:
                return gcd_func(b, a % b)
        else:
            return gcd_func(b, a)

print(gcd_func(5, 5))

assert gcd_func(5, 15) == 5
assert gcd_func(7, 14) == 7
assert gcd_func(6, 9) == 3
assert gcd_func(13, 17) == 1