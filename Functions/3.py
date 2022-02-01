# 3.Дана последовательность целых чисел. Для каждого числа последовательности
# проверить. представляют ли его цифры строго воврастастающую последовательность.
import random
def func(n):
    temp=0
    c=0
    d=0
    ls=[random.randint(1,1000) for i in range(n)]
    for i in ls:
        i=str(i)
        for j in i:
            j=int(j)
            d+=1
            if j>temp:
                temp=j
                c+=1
        if c == d:
            print('У числа - ', i, 'цифры идут по возврастанию')
        c=0
        d=0
        temp=0
    return ls

print(func(10))