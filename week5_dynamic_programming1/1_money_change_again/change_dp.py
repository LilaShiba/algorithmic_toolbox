# Uses python3
import sys
# init table
knownResults = [0 for x in range(1001)]
def get_change(m):
   coins = [1,3,4]
   # set min to max
   minCoins = m
   # if change is == to a value in coins
   if m in coins:
      knownResults[m] = 1
      return 1
   # if in memo, return that answer
   elif knownResults[m] > 0:
      return knownResults[m]
   else:
       for i in [c for c in coins if c <= m]:
         # get answers for how to make change
         numCoins = 1 + get_change(m-i)
         # swap if better
         if numCoins < minCoins:
            minCoins = numCoins
            # populate table
            knownResults[m] = minCoins
   return minCoins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
