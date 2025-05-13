# name: 박정식
# student id: 2023105656
def fib2(n: int) -> int:
    f = [0] * (n + 1)
    
    if n >= 1:
        f[1] = 1
        
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]

    # 실행시간 경고가 뜨는데,
    # 이는 메모리 할당 시간 혹은 리스트 요소 접근 시간이 원인일 확률이 높음
    # 다음과 같은 유사한 코드는 시간 초과가 발생하지 않음

    # a = 0
    # b = 1
    # for i in range(1, n+1):
    #     (a, b) = (b, a+b)
    # return a

    return f[n]