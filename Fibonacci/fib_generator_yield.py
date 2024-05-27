from typing import Generator

def fib_yield(n: int) -> int:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


for i in fib_yield(5):
    print(i)