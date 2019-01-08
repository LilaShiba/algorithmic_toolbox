# Uses python3

def edit_distance(a, b):
    # basic elements
    a_len = len(a)
    b_len = len(b)
    # basic tests
    if not a: return len(b)
    if not b: return len(a)
    if a == b: return 0
    # create matrix
    t = [[float("inf")] * (b_len +1) for _ in range(a_len + 1)]
    # set up grid
    for i in range(a_len+1):
        t[i][0] = i
    for j in range(b_len+1):
        t[0][j] = j
    # algorithm for min cost

    # cycle through matrix
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            # if elements are the same cost is 0
            diff = 0 if a[i-1] == b[j-1] else 1
            # otherwise, add 1 and calculate the min cost for a move
            t[i][j] = min(t[i-1][j]+1, t[i][j-1]+1, t[i-1][j-1]+diff)
    # return the last element of the matrix for min cost
    return (t[a_len][b_len])
    
# run main function
if __name__ == "__main__":
   print(edit_distance(input(), input()))
