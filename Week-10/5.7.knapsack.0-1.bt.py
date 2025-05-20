from typing import List

# Global variable type declarations
n: int
W: float
w: List[float]
p: List[float]
maxprofit: float
bestset: List[bool]
include: List[bool]

def promising(i: int, weight: float, profit: float) -> bool:
    global n, W, w, p, maxprofit
    
    if weight >= W: return False
    
    temp_weight = weight
    temp_profit = profit

    idx = i + 1

    while idx <= n and temp_weight + w[idx] <= W:
        temp_weight += w[idx]
        temp_profit += p[idx]
        idx         += 1

    if idx <= n:
        temp_profit += (W - temp_weight) * p[idx] / w[idx]

    return temp_profit > maxprofit

def knapsack(i: int, weight: float, profit: float) -> None:
    global n, W, w, p, bestset, include, maxprofit
    if weight <= W and profit > maxprofit:
        maxprofit  = profit
        bestset    = include.copy()
    if promising(i, weight, profit):
        include[i+1] = True
        knapsack(i+1, weight + w[i+1], profit + p[i+1])
        include[i+1] = False
        knapsack(i+1, weight,        profit)
