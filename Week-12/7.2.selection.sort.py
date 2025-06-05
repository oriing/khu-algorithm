from typing import List

def selectionsort(n: int, S: List[int]) -> None:
    for idx in range(0, n-1):
        small = idx

        for ptr in range(idx+1, n):
            if S[small] > S[ptr]:
                small = ptr

        S[small], S[idx] = S[idx], S[small]