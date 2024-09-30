# Ask the user for the number of rows they want in the pattern
rows = int(input("Enter the number of rows: "))  

# Loop through each row from 1 to the number of rows entered by the user
for i in range(1, rows + 1):  
# For each row, print numbers starting from 1 up to the current row number
    for j in range(1, i + 1):  
# Print the current number and stay on the same line
        print(j, end=" ")       
  
# Move to the next line after finishing the numbers for the current row
    print()
