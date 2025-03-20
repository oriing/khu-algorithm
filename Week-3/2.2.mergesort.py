from typing import List

def merge(h: int, m: int, U: List[int], V: List[int], S: List[int]) -> None:
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0
    
    for i in range(h+m):
        if k >= m or (j < h and U[j] < V[k]):
            S[i] = U[j]
            j   += 1
        else:
            S[i] = V[k]
            k   += 1

def mergesort(n: int, S: List[int]) -> None:
    h = n // 2
    m = n - h
    if n > 1:
        U = S[:h]
        V = S[h:]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)

