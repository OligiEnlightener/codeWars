# def solution(n):
#     # TODO convert int to roman string
#     # 2978
#     # 2000 + 900 + 80 + 8
#     # 2 * 1000 + 9 * 100 + 7 * 10 + 8
#     # 2 * M + (D + M) + 7 * X + (V + 3 * I)
#     romans = {
#         1: 'I',  # 1
#         5: 'V',  # 5
#         10: 'X',  # 10
#         50: 'L',  # 50
#         100: 'C',  # 100
#         500: 'D',  # 500
#         1000: 'M', # 1000
#     }
#     result = ""
#
#     thousands = n // 1000 % 10
#     if thousands > 0:
#         result += under_four_thousand(thousands)
#     hundreds = n // 100 % 10
#     if hundreds > 0:
#         result += under_thousand(hundreds)
#     decimals = n // 10 % 10
#     if decimals > 0:
#         result += under_hundred(decimals)
#     ones = n % 10  # 8
#     if ones > 0:
#         result += under_ten(ones)
#
#     return result

def solution_repaired(n):
    romans = {
        1: 'I',  # 1
        5: 'V',  # 5
        10: 'X',  # 10
        50: 'L',  # 50
        100: 'C',  # 100
        500: 'D',  # 500
        1000: 'M',  # 1000
    }
    final_roman_number = ""
    thousands = n // 1000 % 10
    if thousands > 0:
        final_roman_number += thousands * romans.get(1000)
    hundreds = n // 100 % 10
    if hundreds > 0:
        final_roman_number
    decimals = n // 10 % 10
    if decimals > 0:
        final_roman_number
    ones = n % 10  # 8
    if ones > 0:
        final_roman_number += under_ten(ones)

def under_five(number):
    if number > 0:
        if number % 4 == 0:
            return I + V
        else:
            return number * I
    else:
        return ""


def under_ten(number):
    if number < 5:
        return under_five(number)
    else:
        if number % 9 == 0:
            return I + X
        else:
            return V + (number % 5) * I


# def under_fifty(number):
#     if number > 0:
#         if number % 4 == 0:
#             return X + L
#         else:
#             return number * X
#     else:
#         return ""


# def under_hundred(number):
#     if number < 5:
#         return under_fifty(number)
#     elif number % 9 == 0:
#         return X + C
#     else:
#         return L + (number % 5) * X


# def under_five_hundred(number):
#     if number > 0:
#         if number % 4 == 0:
#             return C + D
#         else:
#             return number * C
#     else:
#         return ""


# def under_thousand(number):
#     if number < 5:
#         return under_five_hundred(number)
#     else:
#         if number == 9:
#             return C + M
#         else:
#             return D + (number % 5) * C


# def under_four_thousand(number):
#     return number * M


print("700", solution(700))
print("2978", solution(2978))
print("3", solution(3))
print("91", solution(91))
print("14", solution(14))
print("94", solution(94))
print("3375", solution(3375))
print("3444", solution(3444))
print("555", solution(555))