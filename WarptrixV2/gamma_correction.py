import math
import sys

arr = [x for x in range(int(sys.argv[1]))]

r = int(sys.argv[1])-1
b = 50
y = lambda x : r*(math.pow(b,(x/r))-1.0)/(b-1.0)

print(arr)
[print(round(y(x))) for x in arr ]
