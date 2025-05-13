from typing import List, Tuple

def dijkstra(n: int, W: List[List[float]]) -> List[Tuple[int, int, float]]:
    F      = []
    INF    = float("inf")
    touch  = [-1] * (n + 1)
    length = [-1] * (n + 1)
    for i in range(2, n + 1):
        touch[i]  = 1
        length[i] = W[1][i]
    for _ in range(n - 1):
        min = INF
        for i in range(2, n+1):
            if length[i] == -1: continue
            if min > length[i]:
                min  = length[i]
                edge = (touch[i], i, W[touch[i]][i])
        
        F.append(edge)

        for i in range(2, n+1):
            if length[i] == -1: continue
            next_len = W[edge[1]][i] + length[edge[1]]
            if next_len < length[i]:
                length[i] = next_len
                touch[i]  = edge[1]

        length[edge[1]] = -1

    return F