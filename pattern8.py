def print_cuboid(length, breadth, height):
    for i in range(height): 
        if i == 0 or i == height - 1: 
            print('* ' * breadth)  
        else:
            print('* ' + '  ' * (breadth - 2) + '*')  

# Example usage:
length = 5 
breadth = 10  
height = 4  

print_cuboid(length, breadth, height)
