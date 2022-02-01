# 1.Дана последовательность целых чисел. Для каждого числа последовательноси
# найти количество его делителей.
import random
def delit(n):
    count=0
    ls=[random.randint(1,100) for i in range(n)]
    for i in ls:
        for j in range(i+1):
            j+=1
            if j<=i and i%j==0:
                count+=1
                #print(j)
        print('У числа',i,'-',count,'делителей')
        count=0
    return ls
delit(10)
