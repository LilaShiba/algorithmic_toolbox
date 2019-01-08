# Uses python3
import sys

def get_change(m):
    ans = 0
    while m > 0:
        if m >= 10:
            m = m - 10
            ans += 1
        elif m >= 5:
            m = m - 5
            ans += 1
        else:
            m = m - 1
            ans += 1

    return ans

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
