# 5. Дано натуральное число N. Уменьшить число в 2 раза (деление нацело) и
# проверить, изменилось ли после уменьшения количество разрядов в числе.
import random
def func():
    n=random.randint(1,10000)
    print(n)
    m=n//2
    print(m)
    if len(str(n))==(len(str(m))):
        print('Количество разрядов в числе не изменилось')
    else:
        print('Количество разрядов в числе изменилось')
func()