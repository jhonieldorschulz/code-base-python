def fib_it(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        # print(f"next: {next}")
        # print(f"last: {last}")
        print(next)
        last, next = next, last + next
    return next

print(fib_it(10))