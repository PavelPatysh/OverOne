# Дан диапазон целых чисел от n1 до n2.
# Найти факториал каждого третьего простого числа в заданном диапазоне.

import random
import math
def func(n):
    c=0
    print('Введите диапазон чисел:\n')
    n1=int(input())
    n2=int(input())
    ls=[random.randint(n1,n2) for i in range(n)]
    for i in ls:
        c+=1
        if c%3==0:
            k = 0
            for j in range(2, i // 2 + 1):
                if (i % j == 0):
                    k = k + 1
            if (k <= 0):
                print('Факториал числа - ',i,'=',math.factorial(i))
    return ls
print(func(20))