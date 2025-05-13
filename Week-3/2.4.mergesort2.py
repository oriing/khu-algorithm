from typing import List

def merge2(low: int, mid: int, high: int, S: List[int]) -> None:
    U = [0] * (high - low + 1)
    i, j, k = low, mid + 1, 0
    
    while k <= (high - low):
        if (j > high) or (i <= mid and S[i] < S[j]):
            U[k] = S[i]
            i   += 1
        else:
            U[k] = S[j]
            j   += 1
        k += 1
    
    for k in range(high - low + 1):
        S[k+low] = U[k]

def mergesort2(low: int, high: int, S: List[int]) -> None:
    if low < high:
        mid = (low + high) // 2
        mergesort2(low, mid, S)
        mergesort2(mid + 1, high, S)
        merge2(low, mid, high, S)