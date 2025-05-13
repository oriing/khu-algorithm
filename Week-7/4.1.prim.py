from typing import List, Tuple

def prim(n: int, W: List[List[float]]) -> List[Tuple[int, int, float]]:
    F = []
    nearest  = [-1] * (n + 1)
    distance = [-1] * (n + 1)
    INF = float("inf")
    for i in range(2, n + 1):
        nearest[i]  = 1
        distance[i] = W[1][i]
    for _ in range(n - 1):
        min = INF
        for i in range(2, n+1):
            if distance[i] == -1: continue
            if min > distance[i]:
                min  = distance[i]
                edge = (nearest[i], i, distance[i])

        F.append(edge)
        distance[edge[1]] = -1
        
        for i in range(2, n+1):
            if distance[i] > W[edge[1]][i]:
                nearest[i]  = edge[1]
                distance[i] = W[edge[1]][i]

    return F