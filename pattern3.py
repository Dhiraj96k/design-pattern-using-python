s = int(input("Enter start number: "))
n = int(input("Enter end number: "))
for i in range(s, n):
    if i < 2:
        continue 
     
    for j in range(2, i):  
        if i % j == 0:
            break 
    else:
        print(i, end=" ")  # Prime number found
