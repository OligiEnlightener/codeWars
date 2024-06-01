def solve_power(number: int, degree: int) -> int:
    if degree == 0:
        return 1
    else:
        return number * solve_power(number, degree - 1)

assert solve_power(3, 4) == 81
assert solve_power(2, 24) == 16777216