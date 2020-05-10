
print('введите  2 числа')
while True:
        print('введите первый номер')
        a = int(input())
        if(a > -1):
            print('Первый номер принят')
            break
        else:
            print('введите положительное число')


print('введите  2 числа')
while True:
        print("введите второй номер")
        b = int(input())
        if(b > -1):
            print("второй номер принят")
            break
        else:
            print('введите положительное число')
try:
    result = a+b
    print('сумма: %d '%result)

    result = a-b
    print('вычитание: %d '%result)

    result = a*b
    print('умножение: %d '%result)

    result = a/b
    print('деление: %d '%result)

except ZeroDivisionError:
    print('на ноль делить нельзя')

except Exception:
    print('что то случилось')


