from typing import List

def promising(i: int, n: int, col: List[int]) -> bool:
    is_promising = True
    
    for x in range(1, i):
        if is_promising == False: break
        is_promising = (col[x] != col[i] and abs(col[x] - col[i]) != abs(x - i))

    return is_promising

def nqueens(i: int, n: int, col: List[int]) -> None:
    if promising(i, n, col):
        if i == n:
            print("found=", col[1:])
        else:
            for x in range(1, n+1):
                col[i + 1] = x
                nqueens(i + 1, n, col)
