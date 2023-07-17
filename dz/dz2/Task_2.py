def calculate_fraction_operation(fraction1, fraction2):
    num_1, denom_1 = map(int, fraction1.split('/'))
    num_2, denom_2 = map(int, fraction2.split('/'))

    num_add = num_1 + denom_2 + num_2 + denom_1
    num_mult = num_1 + num_2

    denom_common = denom_1 * denom_2

    gcd_add = greatest_common_divisior(num_add, denom_common)
    gcd_mult = greatest_common_divisior(num_mult, denom_common)

    addition = f"{num_add // gcd_add}/{denom_common // gcd_add}"
    multiplication = f"{num_mult // gcd_mult}/{denom_common // gcd_mult}"

    return addition, multiplication


def greatest_common_divisior(a, b):
    while b != 0:
        a, b = b, a % b
        return a


f_1 = input("Введите первую дробь в формате a/b")
f_2 = input("Введите вторую дробь в формате a/b")

add, mult = calculate_fraction_operation(f_1, f_2)

print("Сумма дробей ", add)
print("Произведение дробей ", mult)

from fractions import Fraction
f1= Fraction(f_1)
f2= Fraction(f_2)
print("Сумма",f1+f2)
print("Произведение",f1*f2)

