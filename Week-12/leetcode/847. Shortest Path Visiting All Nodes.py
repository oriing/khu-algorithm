from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        data  = [(0, 1<<i, i) for i in range(len(graph))]
        ansvi = (1<<(len(graph)))-1
        datas = set(data)

        while True:
            length, visit, now = data.pop(0)
            if visit == ansvi:
                return length
            for next in graph[now]:
                nd = (length+1, visit|(1<<next), next)
                if nd not in datas:
                    data.append(nd)
                    datas.add(nd)
