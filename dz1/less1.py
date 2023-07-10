a = int(input('Введите длинну первой стороны = '))
b = int(input('Введите длинну второй стороны = '))
c = int(input('Введите длинну тертей стороны = '))

if a <= b + c or b <= a + c or c <= a + b:
    print('Такой треугольник существует')
    if a == b and b == c:
        print('Он равносторонний')
    elif a != b and b != c and a != c:
        print('Он разносторонний')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('Он равнобедренный')
else:
    print('Такого треугольика не сущетсвует')