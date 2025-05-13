# name: 박정식
# student id: 2023105656
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low, high = 0, n - 1
    location = -1

    while low <= high:
        mid = (low + high) // 2

        if S[mid] == x:
            location = mid
            break
        elif S[mid] > x:
            high = mid-1
        else:
            low  = mid+1

    return location