# Inverted Star Pyramid pattern printing
n = 5

for i in range(n, 0, -1):

   
    for j in range(n - i):  # Print spaces
        print("  ", end=" ")

   
    for j in range(2 * i - 1):  # Print stars
        print(" * ", end="")

    print()