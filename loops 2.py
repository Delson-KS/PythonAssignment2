a=int(input())
b=int(input())
result=1
for i in range(b-a+1):
    result *= (a+i)
print(result)