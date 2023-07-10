num = int(input('Введите число для проверки в диапазоне от 0 до 100000 = '))
MIN_LIMIT = 0
MAX_LIMIT = 100000
i = 2
j = 0

if num == 0 or num == 1:
    print('Это исключение')
elif MIN_LIMIT < num < MAX_LIMIT:
    while i*i <= num and j != 1:
        if num % i == 0:
            j = 1
            i += 1
        else:
            i += 1
    if j == 1:
        print('Введенное число является составное')
    else:
        print('Введенное число является простым ')

else:
    print(' Введите число в диапозоне от 0 до 100000')