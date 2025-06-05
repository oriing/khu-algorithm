from typing import List

def insertionsort(n: int, S: List[int]) -> None:
    for i in range(1, n):
        j = i - 1
        x = S[i]

        while 0 <= j and x < S[j]:
            S[j+1] = S[j]
            j     -= 1

        S[j+1] = x
