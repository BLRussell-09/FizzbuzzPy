import random
import sys
import os

fizbuzzCount = 0
numberList = list(range(1, 100))
for n in numberList:
  if (n % 15 == 0):
    print("fizz buzz")
    fizbuzzCount = fizbuzzCount + 1
    break
  elif (n % 5 == 0):
    print("buzz")
  elif (n % 3 == 0):
    print("fizz")
  else:
    print(n)

print('\n',fizbuzzCount,)
