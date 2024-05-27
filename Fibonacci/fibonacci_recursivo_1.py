def fibonacciRecursivo(n: int) -> int:
    print(f"fibonacciRecursivo({n})")
    print(f"fibonacciRecursivo({n-1}) + fibonacciRecursivo({n-2})")
    if n < 2:
        print("n<2")
        print(f"n:{n}")
        return n
    fibo = fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2)
    print(f"fibo:{fibo}")
    return fibo

print(fibonacciRecursivo(50))