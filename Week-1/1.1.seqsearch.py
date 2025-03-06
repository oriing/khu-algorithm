from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    location = 0

    for val in range(0, n+1):
        if val == n:
            location = -1
        elif S[val] == x:
            location = val
            break

    return location