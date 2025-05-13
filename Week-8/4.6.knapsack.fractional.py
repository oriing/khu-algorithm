from heapq import heappush, heappop
from typing import List, Tuple

class Item:
    def __init__(self, id: int, weight: float, profit: float) -> None:
        self.id: int = id
        self.weight: float = weight
        self.profit: float = profit
        self.profit_per_weight: float = profit / weight
        
def knapsack(n: int, W: float, w: List[float], p: List[float]) -> float:
    heap: List[Tuple[float, Item]] = []
    for i in range(n):
        item: Item = Item(i + 1, w[i], p[i])  # type: ignore
        heappush(heap, (-item.profit_per_weight, item))
    maxprofit:    float = 0.0
    total_weight: float = 0.0

    for _ in range(n):
        if W <= total_weight: break
        data: Item = heappop(heap)[1]
        if total_weight + data.weight <= W:
            maxprofit    += data.profit
            total_weight += data.weight
        else:
            maxprofit   += data.profit_per_weight * (W - total_weight)
            total_weight = W

    return maxprofit