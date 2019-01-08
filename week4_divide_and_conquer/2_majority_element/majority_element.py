# Uses python3
import sys
def merge(a):
    ans = []
    #base
    if len(a) < 2:
        return a
    # divide
    mid = int(len(a) / 2)
    r = merge(a[:mid])
    l = merge(a[mid:])
    # merge
    i = 0
    j = 0
    while i < len(r) and j < len(l):
        if r[i] > l[j]:
            ans.append(l[j])
            j += 1
        else:
            ans.append(r[i])
            i += 1
    ans += r[i:]
    ans += l[j:]
    return ans



def get_majority_element(a, left, right):
    a = merge(a)
    highest = 1
    temp_hi = 1
    for x in range(1, len(a)):
        if a[x] == a[x - 1]:
            temp_hi += 1
        else:
            temp_hi = 1
        if temp_hi > highest:
            highest = temp_hi

    if highest > (right-left)//2:
        return 1
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
