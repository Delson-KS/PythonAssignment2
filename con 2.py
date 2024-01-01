a=int(input())
b=int(input())
c=int(input())
mylist=[a,b,c]
positive =0
negative=0
zero = 0
for i in range(len(mylist)):
    if mylist[i]>0:
        positive+=1
    elif mylist[i]<0:
        negative+=1
    elif mylist[i]==0:
        zero+=1
print("Positive",positive,"Negative",negative,"Zero",zero)