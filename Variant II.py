#Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
#в учебнике “Introduction to Algorithms”  на стр. 71 - 77.

#Задача.
#Перепишите процедуру  MERGE_SORT и отсортируйте последовательность по возрастанию

A = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13]

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [i for i in range(1, n1 + 1)]
    R = [i for i in range(1, n2 + 1)]


    for i in range(n1):
        L[i] = A[p + i - 1]
    for j in range(n2):
        R[j] = A[q + j]
    L[n1 -1] = 2000
    R[n2 -1] = 2000

    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
        return A

print(len(A))
B = merge_sort(A, 0, len(A) - 1)


print(B)