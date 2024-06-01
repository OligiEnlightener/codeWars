

def solve_fibonacci_sequence(number: int) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return solve_fibonacci_sequence(number-1) + solve_fibonacci_sequence(number-2)


print(solve_fibonacci_sequence(7))


assert solve_fibonacci_sequence(0) == 0
assert solve_fibonacci_sequence(1) == 1
assert solve_fibonacci_sequence(2) == 1
assert solve_fibonacci_sequence(3) == 2
assert solve_fibonacci_sequence(4) == 3
assert solve_fibonacci_sequence(5) == 5
assert solve_fibonacci_sequence(6) == 8
assert solve_fibonacci_sequence(34) == 5702887
# assert solve_fibonacci_sequence(299) == 137347080577163115432025771710279131845700275212767467264610201
