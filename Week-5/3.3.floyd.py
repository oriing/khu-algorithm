from typing import List

def floyd(n: int, W: List[List[int]]) -> List[List[int]]:
    D = W
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j],
                          D[i][k] + D[k][j])

    return D