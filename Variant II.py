#Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
#в учебнике “Introduction to Algorithms”  на стр. 71 - 77.

#Задача.
#Перепишите процедуру  MERGE_SORT и отсортируйте последовательность по возрастанию

A = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13]

def merge_sort():
    n1 = len(A) // 2
    n2 = len(A) - n1
    L = [i for i in range(1, n1 + 1)]
    R = [i for i in range(1, n2 + 1)]

    for i in range(n1):
        L[i] = A[i]
    for j in range(n2):
        R[j] = A[n2 + j]
    L[n1 - 1] = 1000
    R[n1 -1] = 1000
    i = 0
    j = 0
    for k in range(0, len(A) - 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1



merge_sort()
print(A)