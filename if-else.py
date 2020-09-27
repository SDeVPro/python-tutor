# print('Salom!')#ekranga natijani chiqarish uchun
# #data types int, float, string, list[], dictionary = {key:value}
# string = input()
# numberic = int(input('Butun son kiriting:'))
# floatic = float(input())
# print('STR:', string, 'INTEGER:', numberic, 'Float:', floatic)
# # bitta qator kommentariyasi
"""
Katta komentariya
"""
'''
Katta kommentariya
'''

# print('Nimadir text')#print ekranga chop qilish komandasi
# #o'zgaruvchi e'lon qilish
# nomi = "hello world!"
# print(nomi)
"""
Uzodan uzo nimanidir tushunchasini berish uchun
katta matnda berib borish
"""
'''
Kotta kommentariya qoldirish uchun
'''
#bitta qatorli kommentariya ctrl + / kommentariyaga

# Num_Ber = 15
# print(Num_Ber)
# number = 101
# number2 = 25
# print(number+number2)#qo'shish
# print(number-number2)#ayirish
# print(number*number2)#ko'paytirish
# print(number/number2)#bo'lis
# print(number**number2)#sonni darajasi
# print(number//number2)#math.pow(son, daraja) sonni butun qismini olib berish
# print(number%number2)#sonlarni qoldiq qismini olib berish

# print('Nimadir text')#print ekranga chop qilish komandasi
# #o'zgaruvchi e'lon qilish
# nomi = "hello world!"
# # print(nomi)
# """
# Uzodan uzo nimanidir tushunchasini berish uchun
# katta matnda berib borish
# """
# '''
# Kotta kommentariya qoldirish uchun
# '''
# #bitta qatorli kommentariya ctrl + / kommentariyaga
# # Num_Ber = 15
# # print(Num_Ber)
# number = 101
# number2 = 25
# print(number+number2)#qo'shish
# print(number-number2)#ayirish
# print(number*number2)#ko'paytirish
# print(number/number2)#bo'lis
# print(number**number2)#sonni darajasi
# print(number//number2)#sonni butun qismini olib berish
# print(number%number2)#sonlarni qoldiq qismini olib berish

#1-vazifa kvadrat perimetrini topish
#
# kvadrat_tomoni = float(input('Kvadrat tomonini kiriting:'))
# print('Kvadrat Perimetri:', kvadrat_tomoni*4)
# print('Kvadrat Yuzasi:', kvadrat_tomoni**2)

#to'rtburchakni yuzasi va perimetrini topish masalasi
# print('a:')
# a = int(input())
# print('b:')
# b = int(input())
# print("4burchak yuzasi: ", a*b, "4burchak perimetri: ", 2*(a+b))

#aylana uzunligini topish
# pi = 3.14
# print('diametrni kiriting:')
# d = float(input())
# print('Aylana uzunligi:', d*pi)

# print('Kub tomonini kiriting:')
# kub_tomoni = int(input())#ekrandan ma'lumot kiritish uchun/butun sonlar uchun int,
# #float haqiqiy sonlar uchun, float(input()), int(input())
# print('Kub Hajmi:', kub_tomoni**3)
# print('Kub tula sirti :', 6*(kub_tomoni**2))

#parallepipedning hajmi va to'la sirtini aniqlash
# print('a:')
# a = int(input())
# print('b:')
# b = int(input())
# print('c:')
# c = int(input())
# print('Hajmi: ', a*b*c, "To'la sirti:", 2*((a*b)+(b*c)+(a*c)))

#doira uzunligi va yuzasi aniqlansin
# pi = 3.14
# print('Radiusni kiriting:')
# radius = float(input())
# print("Uzunligi:", 2*pi*radius, "Yuzasi :", pi*(radius**2))

# a = float(input('A:'))
# b = float(input('B:'))
# print((a+b)/2)
# import math#math kutubxonasini chaqirish
# a = 15
# b = 15
# print(math.sqrt(a*b))#sqrt ildizni olish uchun
#2 ta son yig'indisi, ko'paytmasi, va har biri kvadratini aniqlash
# a = float(input('a:'))
# b = float(input('b:'))
# print("Yig'indi:", a+b, "Ko'paytmasi:", a*b, "Ayirmasi:", a-b, a**2,b**2)

# print(abs(a-b))#abs sonning absolut + musbat holatda olib berish

# x1 = 188
# x2 = 18
# # print(abs(x2-x1))#
# import math
# a = float(input('a:'))
# b = float(input('b:'))
# print("gipotenuzasi:", math.sqrt(a**2+b**2), "Perimetri:", a+b+math.sqrt(a**2+b**2))
import math
# pi = 3.14
# r1 = float(input('r1:'))
# r2 = float(input('r2:'))
# if r1 > r2:
#     print('1-yuza:', pi*(r1**2))
#     print('2-yuza:',pi*(r2**2))
#     print('3-yuza:', pi*(r1-r2))
# else:
#     print('R1 < R2')

# import math
# x1 = 15
# x2 = 10
# y1 = 15
# y2 = 18
# print(math.sqrt((x2-x1)**2+(y2-y1)**2))

#if else elif

# print('Son kiriting:')
# son = float(input())
# if son < 0:
#     print(son)
# else:
#     son += 1
#     print(son)
# # #
# print('Son kiriting:')
# son = float(input())
# if son < 0:
#     print(son-2)
# else:
#     son += 1
#     print(son)

# print('Son kiriting:')
# son = float(input())
# if son < 0:
#     print(son-2)
# elif son == 0:
#     son = 10
#     print(son)
# else:
#     son += 1
#     print(son)

# list = [1,-2,-3]
# count = 0
# for i in list:
#     if i < 0:
#         count += 1
#         print(count)


# list = [1,-2,-3,5,6]
# count = 0
# countplus = 0
# for i in list:
#     if i < 0:
#         count += 1
#         print('manfiy sonlar',count)
#     else:
#         countplus += 1
#         print('+',countplus)

# for i in range(1,11):
#     for k in range(2,11):
#         print(i,'*',k,'=',i*k,'\t')
# a = int(input())
# b = int(input())
# a = a +b
# b = b-a
# a = b +a
# print(abs(a), abs(b))

#List massiv tushunchasiga yaqin, massiv - bu bir xil turga tegishli
#bo'lgan elementlar ketma-ketligi, pythonda bir xil turga tegishli
#shart emas
# list = [1, 2.3,'s',"Olma", True]
# print(list)
"""
1 2 3 
4 5 6
7 8 9
"""
# print("Karra jadvali:")
# for i in range(1,11):
#     for k in range(2,11):
#         print(f'{i}*{k}={i*k}','\t',end="")
#     print('')

#Shart operatori bo'yicha tushuncha
"""
if (shart) va shart beriladi if dan keyin
if 3<2: #shart e'loni
    print('shart qoniqarsiz')#shart tanasi
else:#aksincha bo'lsa, 1-shart qondirilmasa
    print('shart qoniqarli')#aks holat tanasi
"""

# a = "salom"
# if a != "salom":
#     print(True)
# else:
#     print(False)

# a = int(input('Yoshingizni kiriting:'))
# if a >= 30 and a <= 100:
#     print('Sizni buyuk kelajak kutmoqda')
# elif a >= 19 and a<=30:
#     print('Siz yosh ekansiz!')
# elif a <= 18 and a >= 1:
#     print('Passport olganingizdan keyin keling!')
# else:
#     print('Sizni yoshingizda odam yashamaydi')


# for i in 'Hello World':
#     if i =='':
#         break
#         print(i, end="")
#     else:
#         print('\n No Space')
# print('')

#Kvadrat tenglama
# import math
# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# D = b*b - 4*a*c
# if D>=0:
#     x1 = (-b-math.sqrt(D))/(2*a)
#     x2 = (-b + math.sqrt(D)) / (2 * a)
#     print('Ha', round(x1,2), round(x2,2))
# else:
#     print('Ildiz yuq')

#random holatda 3xonali son kiritiladi, shundan eng maximumini topish, eng kattasini

# from random import random
# num = round(random()*1000,1)
# print(num)
# strNum = str(num)
# maxDigit = -1
# for i in range(len(strNum)):
#     if strNum[i] =='.':
#         continue
#     elif maxDigit < int(strNum[i]):
#         maxDigit = int(strNum[i])
# print(maxDigit)

#Polindrom son yoki so'zni topish, Polindrom - 1001, arra ya'ni o'rtasidan bo'lganda 2 la tomon bir xil bo'lish holati

# print("So'z yoki son kiriting:")
# s = input()
# l = len(s)
# for i in range(l//2):
#     if s[i] != s[-1-i]:
#         print('Bu polindrom emas!')
#         quit()
# print("Bu polindrom")


#berilgan matndagi istalgan so'zni yangisiga almashtirish
# satr = input('Matnni kiriting:')
# print(satr)
# substrOld = input("Eski so'z:")
# substrNew = input("Yangi so'z:")
# lenStrOld = len(substrOld)
#
# while satr.find(substrOld)>0:
#     i = satr.find(substrOld)
#     satr = satr[:i]+substrNew+satr[i+lenStrOld:]
# print(satr)

# berilgan matnimiz orasida eng uzun so'zni aniqlash
#
# str = input('matn kiriting:')
# print(str)
# listWords = str.split()
# idLongestWord = 0
# for  i in range(1, len(listWords)):
#     if len((listWords[idLongestWord]))<len(listWords[i]):
#         idLongestWord = i
#         print(listWords[idLongestWord])

#random holatda massiv beriladi: massiv bir tuga yoki bir neha
# bir necha turdagi o'zgaruvchilar ketma-ketlikda joylashishi

# import random
# a = []
# for i in range(10):
#     a.append(int(random.random()*100))
# print(a)
# juft_son = 0
# toq_son = 0
# for i in a:
#     if i%2==0:
#         juft_son +=1
#     else:
#         toq_son +=1
# print("Juft sonlarimiz soni:", juft_son)
# print("Toq sonlarimiz soni:", toq_son)

#massiv beriladi random holatda, shu yerdan manfiy va musbat sonlarni ajratib berishimiz kerak

# import random
# a = []
# for i in range(15):
#     a.append(int(random.random()*20)-10)
# print(a)
# manfiy = []
# musbat = []
# for i in a:
#     if i < 0:
#         manfiy.append(i)
#     elif i > 0:
#         musbat.append(i)
#     else:
#         print(i)
# print("Manfiy sonlar:", manfiy)
# print("Musbat sonlar:", musbat)

# massiv beriladi, agar manfiy son joylashgan bo'lsa,
# -1 ga o'zgartirilsin, musbat son bo'lsa 1 ga a
#almashtirilsin, 0 ga teng 0 deb chiqarilsin
# massiv = [10,-2,3,8,0,0,5,-8,-33,55,-15.25,-1,5]
# almashgan_massiv = []
# for i in massiv:
#     if i >0:
#         almashgan_massiv.append(1)
#     elif i < 0:
#         almashgan_massiv.append(-1)
#     else:
#         almashgan_massiv.append(0)
# print(massiv)
# print("Almashtirilgan massiv:", almashgan_massiv)

# matritsa beriladi, uning asosiy va ikkilamchi dioganali
# elementlari yig'indisi topilsin
#
# from random import random
# n = 4
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(int(random()*20))
#     matrix.append(row)
# for row in matrix:
#     print(row)
# asosiydioganal = 0
# ikkilamchidioganal = 0
# for i in range(n):
#     asosiydioganal += matrix[i][i]
#     ikkilamchidioganal +=matrix[i][n-i-1]
# print("Asosiy dioganal summasi:", asosiydioganal)
# print("Ikkilamchi dioganal summasi", ikkilamchidioganal)

# k va n sonlari berilgan k sonini n martta
#chop etuvchi dastur tuzilsin

# n = int(input("Takrorlashlar sonini kiriting:"))
# k = int(input("Takrorlanuvchi son:"))
# for i in range(1,n+1):
#     print(k)

# for qadam in range(11):# for har doim 0 indexdan boshlab ishlaydi
#     print(qadam)

# a = int(input("a:"))
# b = int(input("b:"))
# for i in range(a,b+1):
#     print(i)
# print("Chiqarilgan sonlar miqdori:", b+1-a)

# a = int(input("a:"))
# b = int(input("b:"))
# for i in range(a,b+1):
#     j = b-i+a
#     print(j)
# print("Chiqarilgan sonlar miqdori:", b-1-a)


# 1 kg konfet narxi haqiqiy sonda kiritilsin
# 1 dan 12 kg gacha bo'lgan konfet narxi chiqailsin

# narx = float(input('1 kg konfet narxi:'))
# for i in range(1,13):
#     print(i,"kg konfet narxi:", i*narx)

# 0.1, 0.2 ... 1 kg konfet narxini chiqarsin
# narx = float(input('1 kg konfet narxi:'))
# for i in range(1,11):
#     print(i/10,"kg konfet narxi:", i*narx/10)

# 1.2, 1.4, 1.6, 1.8, 2 kg konfet narxlarini chiqarsin
# narx = float(input('1 kg konfet narxi:'))
# for i in range(6,11):
#     print(i/5,"kg konfet narxi:", i*narx/5)

# a va b orasidagi sonlar yig'indisini chiqarish

# a = int(input('a:'))
# b = int(input('b:'))
# summa = 0
# for i in range(a,b+1):
#     if i>=a:
#         summa=summa+i
# print("a va b oralig'idagi sonlar yig'indisi:",summa)

# a va b oraliqdagi sonlar ko'paytmasini topish
# a = int(input('a:'))
# b = int(input('b:'))
# kupaytma = 1
# for i in range(a,b+1):
#     if i>=a:
#         kupaytma=kupaytma*i
# print("a va b oralig'idagi sonlar ko'paytmasi:",kupaytma)

#a va b oraliqdagi sonlar kvadrati chiqarilsin
#
# a = int(input('a:'))
# b = int(input('b:'))
# kvadrat = 0
# for i in range(a,b+1):
#     if i>=a:
#         kvadrat=kvadrat+i*i
# print("a va b oralig'idagi sonlar kvadrati:",kvadrat)

# s = 1+1/2+1/3+1/4+...1/n gacha ishlaydigan dastur tuzilsin
# n = int(input('Chegarani kiriting:'))
# summa = 0
# for i in range(1,n):
#     summa = summa +1/i
# print("1/1 dan 1/n gacha bo'lgan sonlar yig'indisi", round(summa,1))

#for masalasi 11
# import math
# n = int(input("N ni kiriting:"))
# m = 0
# for i in range(0,n+1):
#     m = m + math.pow((n+i),2)
#     print(math.pow((n+i),2))
# print("(n+i)*(n+i) siklning summasi!:",m)

#for masalasi 12
# n = int(input("Ko'paytirishlar sonini kiriting:"))
# m=1
# for i in range(11, 10+n):
#     m=m*i/10
#     print(m)
# print("1.1*1.2*....*n :", (11+n)/10, " = ", round(m,2))

# for sikl 13
# n = int(input("Ko'paytirishlar sonini kiriting:"))
# m=0
# k = 0
# for i in range(1,n+1):
#     m = ((i+10)-(i+11))/10
#
#     k = k+(m * (-1))
#     print(k)
# print("S = 1,1-1,2 + ....:", -1-n/5," = ", round(m,2))

#for sikl 14
# n = int(input("Kvadratga ko'tarilishi kerak bo'lgan sonni kiriting:"))
# s = 0
# for i in range(1,n):
#     s=s+(2*i-1)
#     print(s)
# print("n*n=1+3+5....(2*n-n):", s)

#for sikl 15

# n = int(input("Daraja bering:"))
# a = int(input("Sonni bering:"))
# print(a,"ning",n,"darajasi:", a**n)

#for sikl 16
# import math
# n = int(input("Daraja bering:"))
# a = int(input("Sonni bering:"))
# for i in range(1,n+1):
#     j=math.pow(a,i)
#     print(j)
# print(a,"ning :",n,"darajasi", j)

#for 17
# import math
# n = int(input("Daraja bering:"))
# a = int(input("Sonni bering:"))
# s = 0
# for i in range(1,n+1):
#     j=math.pow(a,i)
#     print(j)
#     s = s+j
# print(a,"ning :",n,"darajalari yig'indisi", s)

#for 18
# import math
# a=float(input("sonni kiriting: "))
# n=int(input("darajani kiriting: "))
# s=0
# r=1
#
# for i in range(1, n+1):
#     s+=r*(math.pow(a,i))
#     r*=-1
#     print(s)
# print(a," ning ",n," darajasi yegindilari: ", s)

#for 19 faktorial
# import math
# n = int(input("Faktorial chegarasi:"))
# for i in range(1,n+1):
#     m=math.factorial(n)
# print(n,"ning faktoriali:",m)

#for 20
# import math
# n = int(input("Faktorial chegarasi:"))
# b = 0
# for i in range(1,n+1):
#     m=math.factorial(i)
#     print(i,"!=",m)
#     b=b+m
# print(n,"gacha bo'lgan faktoriallar yig'indisi:",b)

# import functions
#
# a = int(input("a:"))
# b = int(input("b:"))
# print(functions.gipotenuza(a,b))
