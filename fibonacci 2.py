from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}#base case

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

if __name__ == "__main__":
    print(fib3(5))
    print(fib3(50))
#memoization : 계산 작업 완료 후 결과 저장 실행된 같은 계산 수행시 재계산하지 않고 저장된 값 사용.
