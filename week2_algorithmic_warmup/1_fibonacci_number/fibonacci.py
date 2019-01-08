# Uses python3
def calc_fib(n):
    memo = {}
    if n in memo: return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)

    memo[n] = f
    return f

n = int(input())
print(calc_fib(n))
