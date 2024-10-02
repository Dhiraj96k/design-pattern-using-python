value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 5, 4, 1]
num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "V", "IV", "I"]
n = int(input("Enter Number: "))
result = ""

for i in range(len(value)):
    while n >= value[i]:
        result += num[i]  # Add the Roman numeral corresponding to value[i]
        n -= value[i]     # Subtract the value from n

print(result)
