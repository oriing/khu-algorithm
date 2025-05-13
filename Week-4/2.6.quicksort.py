from typing import List

def partition(low: int, high: int, S: List[int]) -> int:
    pivotitem = S[low]
    j = low

    for idx in range(low+1, high+1):
        if pivotitem > S[idx]:
            j += 1
            (S[idx], S[j]) = (S[j], S[idx])
    
    (S[j], S[low]) = (S[low], S[j])
    return j

def quicksort(low: int, high: int, S: List[int]) -> None:
    if low < high:
        ptr = partition(low, high, S)
        quicksort(low, ptr-1, S)
        quicksort(ptr+1, high, S)