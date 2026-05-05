colours = []

for i in range(5):
    x = input("Enter a colour: ")
    colours.append(x)

print(colours)

y = input("Enter a colour to be inserted after the third: ")
colours.insert(3, y)  

z = input("Enter a colour to swap with the second position: ")
colours[1] = z          

del colours[4]          

print(colours)
