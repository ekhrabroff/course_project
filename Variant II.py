#Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
#в учебнике “Introduction to Algorithms”  на стр. 71 - 77.

#Задача.
#Перепишите процедуру  MERGE_SORT и отсортируйте последовательность по возрастанию

import math
mass = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13]

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [i for i in range(0, n1 +1)]
    R = [i for i in range(0, n2 +1)]
   
    for i in range(n1):
        L[i] = A[p + i - 1]
    for j in range(n2):
        R[j] = A[q + j]
    L[n1] = math.inf
    R[n2] = math.inf
    
    i = 0
    j = 0
    for k in range(p-1, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(m, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(m, p, q)
        merge_sort(m, q + 1, r)
        merge(m, p, q, r)


merge_sort(mass, 1, len(mass))

print(mass)