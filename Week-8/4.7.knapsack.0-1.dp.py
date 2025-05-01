from typing import Dict, Tuple

def knapsack(n: int, W: int, DP: Dict[Tuple[int, int], int]) -> int:
    global w, p
    if n == 0 or W <= 0:
        DP[(n, W)] = 0
    else:
        for i in range(n+1): DP[(i, 0)] = 0
        for i in range(W+1): DP[(0, i)] = 0
        for idx in range(1, n+1):
            for weight in range(0, W+1):
                if w[idx] <= weight:
                    DP[(idx, weight)] = max(
                        DP[(idx-1, weight)],
                        DP[(idx-1, weight-w[idx])] + p[idx]
                    )
                else:
                    DP[(idx, weight)] = DP[(idx-1, weight)]

    return DP[(n, W)]