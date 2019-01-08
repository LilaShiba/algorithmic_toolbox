# Uses python3
import sys

def optimal_weight(W, w):
    # w = len(items)
    # W = maxweight
    # W + 1 because we need to include all answers from 0 - max
    table = [[None] * (len(w)+1) for _ in range(W +1)]
    # set all first values to 0
    for u in range(W+1):
        table[u][0] = 0

    for i in range(1, len(w) + 1):
        for u in range(W + 1):
            table[u][i] = table[u][i-1]
            if u >= w[i-1]:
                table[u][i] = max(table[u][i], table[u-w[i-1]][i-1]+w[i-1])
    return table[W][len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
