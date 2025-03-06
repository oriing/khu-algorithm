from typing import List

def arrsum(n: int, S: List[int]) -> int:
    # Complete the code here
    sm = 0
    for i in range(0, n):
        sm += S[i]
    return sm