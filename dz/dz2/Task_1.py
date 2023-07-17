
def hex_number(number):
    hexnumber = ""

    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    while number > 0:
        remainder = str(number % 16)
        hexnumber = remainder + hexnumber
        number = number // 16

    if is_negative:
        hexnumber = "-" + hexnumber

    return hexnumber


num = int(input('Введите целое число: '))
result = hex_number(num)
print(result)
print(hex(num))
