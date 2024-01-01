import math
n = int(input())
result=0
for i in range(n):
    result += math.factorial(i+1)
print(result)