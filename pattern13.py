n=int(input("Enter number="))
k=len(str(n))
i=1
sum=0
num=n
while i<=k:
    x=n%10
    sum+=x**k
    n=n//10
    i+=1
print(sum)
if(sum==num):
    print(f"{num}  is armstrong number")
else:
    print(f"{num}  is not armstrong number")