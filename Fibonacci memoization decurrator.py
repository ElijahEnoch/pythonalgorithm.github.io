from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n<2:
        return n
    return fib4(n - 2) + fib4(n - 1)

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))
#계산된 반환값을 메모리에 저장
#이후 다시 동일한 인자와 fib4가 실행되면 캐시된 값을 검색해서 반환.
#@lru_cache(maxsize=None) - 데커레이터에서 가장 최근의 호출을 캐시할수 있는 크기.
##noe 캐시에 제한이 없다는 걸 의미.
