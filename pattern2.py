n = int(input("enter number"))
res = 0
temp=11

while n >10 :
    while n > 0:
        i = n%10 #return last digite
        res=res+i   
        n=n//10 # remove last digite
    n=res
    res=0
print(n)
