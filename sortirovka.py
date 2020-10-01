# def insertion_sort1(A):
#     for i in range(1, len(A)):
#         for j in range(i-1, -1, -1):
#             if A[j] > A[j+1]:
#                 A[j], A[j+1] = A[j+1], A[j]
#             else:
#                 break
#
# def insertion_sort2(A):
#     for i in range(1, len(A)):
#         j = i-1
#         while A[j] > A[j+1] and j>=0:
#             A[j], A[j+1]=A[j+1],A[j]
#             j-= 1
#
# def insertion_sort3(A):
#     for i in range(1, len(A)):
#         curNum = A[i]
#         k = 0
#         for j in range(i-2, -2, -1):
#             k = j
#             if A[j] > curNum:
#                 A[j+1]=A[j]
#             else:
#                 break
#         A[k+1] = curNum
#
# A = [5,9,1,5,6,8,6,4,12,3]
# print(A)
# insertion_sort1(A)
# print(A)
# insertion_sort2(A)
# print(A)
# insertion_sort3(A)
# print(A)

# def bubble_sort1(A):
#     for i in range(0, len(A)-1):
#         for j in range(0, len(A)-i-1):
#             if A[j] > A[j+1]:
#                 A[j], A[j+1] = A[j+1], A[j]
#
# def bubble_sort2(A):
#     for i in range(0, len(A)-1):
#         done = True
#         for j in range(0, len(A)-i-1):
#             if A[j] > A[j+1]:
#                 A[j],A[j+1]=A[j+1],A[j]
#                 done = False
#         if done:
#             return
# A = [1,5,6,8,7,9,4,5,6,5,9]
# print(A)
# bubble_sort1(A)
# print(A)
# bubble_sort2(A)
# print(A)

# import sys
# def merge_sort(A):
#     merge_sort2(A, 0, len(A)-1)
# def merge_sort2(A, first, last):
#     if first < last:
#         middle = (first+last)//2
#         merge_sort2(A, first, middle)
#         merge_sort2(A, middle+1, last)
#         merge(A, first, middle, last)
#
# def merge(A, first, middle, last):
#     L = A[first:middle+1]# list = [1,2,5,8,6,7] list([::-1])
#     R = A[middle+1:last+1]
#     L.append(sys.maxsize)
#     R.append(sys.maxsize)
#     i = j = 0
#
#     for k in range(first, last+1):
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i+=1
#         else:
#             A[k] = R[j]
#             j+=1
# A = [5,6,8,1,15,16,7,9,3,7]
# print(A)
# merge_sort(A)
# print(A)
#
# def selection_sort(A):
#     for i in range(0,len(A)-1):
#         minIndex = i
#         for j in range(i+1, len(A)):
#             if A[j] < A[minIndex]:
#                 minIndex = j
#         if minIndex !=i:
#             A[i], A[minIndex]=A[minIndex], A[i]
#
# A = [5,4,7,8,9,4,5555,5,1,4,58,99,555]
# print(A)
# selection_sort(A)
# print(A)


