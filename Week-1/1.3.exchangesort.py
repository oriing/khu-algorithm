from typing import List

def exchangesort(n: int, S: List[int]) -> None:
    # Complete the code here
    # for i in range(0, n-1):
    #     for j in range(0, n-i-1):
    #         if S[j] > S[j+1]:
    #             S[j], S[j+1] = S[j+1], S[j]

    for i in range(0, n):
        for j in range(i+1, n):
            if S[i] > S[j]:
                S[i], S[j] = S[j], S[i]