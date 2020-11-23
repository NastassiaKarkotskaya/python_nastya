#1
# str = 'samsung forever'
# print (str[5:9])

#2
# я не поняла как создать строку, состоящую из N нулей и K единиц, где N и K – заданные пользователем
# натуральные числа.
# N=input()
# K=input()
# str='{0}{1}'.format(N,K)

# Это часть, если у меня есть готовое число:
import math
# str="11100011"
# print(str)
# a=str.count('0')
# b=str.count('1')
# print (a,b)
# print("В данной строке",a, "нулей и", b ,"единиц")

 #3
# str = 'samsung forever'
# print(str[::2])

#4

# slayd 32, math and random
# import random, math
#
# a = random.random()
# b = math.sqrt(a)
# print(a,b)

#5
# import random, math
# x = random.randint(1,99)
# y = random.randint(1,99)
# c = int(math.sqrt((x*x) + (y*y)))
# print(x,y,c)

#6 slayd 33 (#1)
# import random
# y = random.randrange(100,999,1)
# x = y//10
# a = x//10
# b= x % 10
# c = y % 10
# print(y, a, b, c, a+b+c)


#7 slayd 33 (#2)
import random
list=['26C', '40F']
str = random.choice((list))
a=int(str[0:2])

if str.endswith('F'):
    print((a-32)*5/9)
else:
    print(9/5*a +32)

print(str)


