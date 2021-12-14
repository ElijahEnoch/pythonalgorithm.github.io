#fib(n) = fib(n - 1) + fib(n - 2)

def fib2(n: int) -> int:
    if n < 2:#기저조건base case
        return n
    return fib2(n-2) + fib2(n-1)#재귀조건

if __name__ == "__main__":
    print(fib2(4))
    print(fib2(5))
    print(fib2(10))
    print(fib2(20))
    
