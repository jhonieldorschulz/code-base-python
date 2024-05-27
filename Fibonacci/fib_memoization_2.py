from typing import Dict
memo: Dict[int, int] = {0:0, 1:1}

def fib_memo(n: int) -> int:
    print(f"n:{n}")
    print(f"memo:{memo}")
    if n not in memo:
        print("not in memo")
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
        print(f"memo[n]: {memo[n]}")
    return memo[n]

print(fib_memo(50))
# print(fib_memo(50))