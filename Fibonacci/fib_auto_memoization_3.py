from functools import lru_cache


@lru_cache(maxsize=None)
def fib_auto_memo(n: int) -> int:
    if n < 2:
        return n
    print(f"fib_auto_memo({n - 2}) + fib_auto_memo({n - 1})")
    fib =  fib_auto_memo(n - 2) + fib_auto_memo(n - 1)
    print(f"fib:{fib}")
    return fib


print(fib_auto_memo(50))