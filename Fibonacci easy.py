def fib5(n: int) -> int:
    if n == 0: return n
    last: int = 0#fib(0)
    next: int = 1#fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    print(fib5(5))
    print(fib5(50))
