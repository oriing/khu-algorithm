# name: 박정식
# student id: 2023105656
def fib1(n: int) -> int:
    if n <= 1: return n
    
    return fib1(n-1) + fib1(n-2)