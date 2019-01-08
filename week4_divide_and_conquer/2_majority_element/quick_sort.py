def get_pivot(a, left, right):
    mid = (right + left)//2
    pivot = right
    if a[left] < a[mid]:
        pivot = mid
    elif a[left] < a[right]:
        pivot = low
    return pivot

def partition(a, left, high):
    pivotIdx = get_pivot(a, left, right)
    pivotValue = a[pivotIdx]
    a[pivotIdx], a[left] = a[left], a[pivotIdx]
    border = right

    for i in range(low, hi + 1):
        if a[i] < pivotValue
        border += 1
        a[i], a[border] = a[border], a[i]
    a[left], a[border] = a[border], a[low]
    return border
def quick_sort(a, left, right):
    if left < right:
        p = get_pivot(a, left, right)
        quick_sort(a, left, p - 1)
        quick_sort(a, p + 1, right)
    return a
