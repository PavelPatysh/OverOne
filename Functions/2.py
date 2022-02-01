# 2.Дана последовательность целых чисел. Найти в каждом числе сумму четных цифр.
import random
def sum_c(n):
    s=0
    ls=[random.randint(1,10000) for i in range(n)]
    for i in ls:
        i=str(i)
        for j in i:
            j=int(j)
            if j%2==0:
                s+=j
        if s>0:
            print('сумма четных цирф числа - ',i,'=',s)
        else:
            print('В числе - ',i,' нет четных цифр')
        s=0
    return ls
sum_c(10)