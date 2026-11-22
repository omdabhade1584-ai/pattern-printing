# Hollow Square Pattern printing
n = 5

for i in range(n):
    for j in range(n):

        if i == 0 or i == n-1 or j == 0 or j == n-1: # checking the position of boundry to print stars for that position
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()