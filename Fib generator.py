from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0#특수 조건
    if n > 0: yield 1#특수 조건
    last: int = 0#fib(0)
    next: int = 1#fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next#Generator 핵심 반환문.

if __name__ == "__main__":
    for i in fib6(50):
        print(i)
#Generator - yield. 반복문 for 를 통해 반복될떄마다 fib6()의 yield가 실행.
#fib6()의 끝에 도달해서 반횐될 yield 값이 없다면 자동으로 반복이 종료.
