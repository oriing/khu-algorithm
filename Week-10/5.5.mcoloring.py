from typing import List

# Global variables
W: List[List[int]] = []     # Adjacency matrix
vcolor: List[int] = []      # Vertex colors
n: int = 0                  # Number of vertices
count: int = 0              # Solution counter

def promising(i: int) -> bool:
    global W, vcolor
    
    for idx in range(i):
        if W[i][idx]:
            if vcolor[i] == vcolor[idx]:
                return False

    return True

def mcoloring(i: int, m: int) -> None:
    global n, vcolor, count
    if promising(i):
        if i == n:
            print(vcolor[1:])
            count += 1
        else:
            for now_color in range(1, m+1):
                vcolor[i+1] = now_color
                mcoloring(i+1, m)
                vcolor[i+1] = 0
