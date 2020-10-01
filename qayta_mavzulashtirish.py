#o'zgaruvchilar
# nomi = input("nomini kiriting:")
# nomi_eski = "salom"
# if nomi == "salomaka":
#     nomi = nomi_eski
#     print(nomi)
# else:
#     print(nomi)

# a = float(input("a:"))
# print("Kvadratning perimetri:", round(a*4,3))
# print("Kvadratning yuzasi", round(a**2,3))

# a = float(input("a:"))
# b = float(input("b:"))
# print("4burchak perimetri:", round(a*b,3))
# print("4burchak yuzasi", round(2*(a+b),3))

#shart operatorlari, shart beriladi, shart tanasi bor va natija
# a = float(input("son kiriting:"))
# if a < 0:
#     print(a-2)
# elif a > 0:
#     a+=1
#     print(a)
# else:
#     print(10)

#sikl operatorlari for va while, while shart bilan ishlaydi
# k = int(input("takrorlanuvchi sonni kiriting:"))
# n = int(input("takrorlashlar soni:"))
# for item in range(1, n+1):
#     print(item,":",k)

# a = int(input("a:"))
# b = int(input("b:"))
# for item in range(a, b+1):
#     print(item)
# print("chiqarilgan sonlar miqdori:", b+1-a)

# a = int(input("a:"))
# b = int(input("b:"))
# for item in range(a+1, b):
#     temp = b-item+a
#     print(temp)
# print("chiqarilgan sonlar miqdori:", b-1-a)

#functions funksiya def e'lon qilinishi func nomi(attribute):

# def add_numbers(a,b):
#     return a+b
# def multiple_numbers(a,b):
#     return a*b
# def bulish_numbers(a,b):
#     return a/b
# def ayirish_numbers(a,b):
#     return a-b
# a = float(input("a:"))
# b = float(input("b:"))
# print(add_numbers(a,b))
# print(multiple_numbers(a,b))
# print(bulish_numbers(a,b))
# print(ayirish_numbers(a,b))

#tartiblash algoritmlari

# list = [9,8,7,6,5,4,3,2,1,0]
#
# for j in range(0,10):
#     for i in range(0,9):
#         if list[i] > list[i+1]:
#             temp = list[i]
#             list[i]=list[i+1]
#             list[i+1]=temp
# print(list)
#
# def quick_sort(sequence):
#     lenght = len(sequence)
#     if lenght <=1:
#         return sequence
#     else:
#         pivot = sequence.pop()
#         items_greater = []
#         items_lower = []
#     for item in sequence:
#         if item > pivot:
#             items_greater.append(item)
#         else:
#             items_lower.append(item)
#     return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)
# print(quick_sort([5,6,7,8,11,11,12,51,41,41,55,3,6,84,12,15,15,1,215,123,55,15,66,55]))

