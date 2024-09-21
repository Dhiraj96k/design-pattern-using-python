n = int(input("enter number"))
res = 0
temp=11

while temp >10:
    while n > 0:
        i = n%10 #return last digite
        res=res+i
        temp=res    
        n=n//10 # remove last digite
print(res)
