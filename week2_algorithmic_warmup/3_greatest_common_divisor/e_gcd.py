# Uses python3
import sys

def gcd(a,b):
   while(b):
       a, b = b, a % b

   return a


#if __name__ == "__main__":
#    input = sys.stdin.read()
#    a, b = map(int, input.split())
print(gcd(357, 234))