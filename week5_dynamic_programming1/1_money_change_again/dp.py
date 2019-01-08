def change(m):
    coin_table = [1,3,4]
    if m == 0:
        return 0
    best = -1
    for coin in coin_table:
        if coin <= m:
            next = change(m-coin)
        if best < 0 or best > next + 1:
            best = next + 1
    return best

print(change(34))
