# funksiya o'zi nima? Funksiya hayotiy misolda
# def func_name(attr):#funksiya e'loni
#     func_body = attr**2#funksiya tanasi
#     return func_body#qaytariladigan natija
#
# a = int(input("a:"))#attribut e'loni
# print(func_name(a))#natijani chop etish

# def triangle(a,b,c):
#     s = a*b*c
#     p = 2*(a+b+c)
#     print("Yuza",s, "perimetr:",p)
#
# a = float(input('a katetni kiriting:'))
# b = float(input('b katetni kiriting:'))
# c = float(input('c gipotenuzani kiriting:'))
#
# triangle(a,b,c)
# import math
# def gipotenuza(a,b):
#     c = math.sqrt(a*a+b*b)
#     return c


# a = float(input('a katetni kiriting:'))
# b = float(input('b katetni kiriting:'))
# print(gipotenuza(a,b))
# print(a+b+gipotenuza(a,b))

# ikkilik sanoq sistemasi
# 0 dan 9 gacha sonlar 10 lik sanoq sistemasi
# 2 lik sanoq sistemasi 0 va 1 dan tashkil topadi

# def converToBinary(attr):
#     if attr>1:
#         converToBinary(attr//2)
#     print(attr%2, end='')
#
# decimal = int(input("10 lik son kiriting:"))
# converToBinary(decimal)

#faktorial sonlarni topish funksiyai
#recursive funksiyalarimiz - o'ziga o'ziga murojaat qiluvchi funksiyalar
# def recursive_factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num*recursive_factorial(num-1)
#
# number = int(input("Faktorial sonni kiriting:"))
# #faktorial son n!=1*2*3...*n
# if number < 0:
#     print("Uzr faktorial manfiy son qabul qilmaydi!")
# elif number == 0:
#     print("Faktorial sonimiz 1 ga teng!")
# else:
#     print("Faktorial:", number,"! = ", recursive_factorial(number))
