#MaxPairwiseProductNaive(A[1...n]):
#product←0
# for i from 1 to n:
#     for j from i+1 to n:
#         product←max(product,A[i]·A[j])
# return product


#def max_pairwise_product(numbers):
#    n = len(numbers)
#    for first in range(n):
#        for second in range(first + 1, n):
#            ans = max(ans,numbers[first] * numbers[second])
#    return ans
