from typing import List

class Heap:
    def __init__(self, n: int, S: List[int]) -> None:
        self.data = S
        self.n    = n               # started at 1

def shiftdown(H: Heap, i: int) -> None:
    if   H.n <  2 * i: return
    elif H.n == 2 * i: lptr  = 2 * i
    else:
        if H.data[i*2] < H.data[i*2+1]: lptr = i * 2 + 1
        else:                           lptr = i * 2
    
    if H.data[i] < H.data[lptr]:
        H.data[i], H.data[lptr] = H.data[lptr], H.data[i]
        shiftdown(H, lptr)
        

def root(H: Heap) -> int:
    if H.n <  1: raise IndexError()

    rval      = H.data[1]
    H.data[1] = H.data[H.n]
    H.n      -= 1

    shiftdown(H, 1)
    return rval

def removekeys(n: int, H: Heap, S: List[int]) -> None:
    for i in range(n, 0, -1):
        S[i] = root(H)

def makeheap(n: int, H: Heap) -> None:
    for i in range(n//2, 0, -1):
        shiftdown(H, i)

def heapsort(n: int, H: Heap, S: List[int]) -> None:
    makeheap(n, H)
    removekeys(n, H, S)
