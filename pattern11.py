#  Hollow Right-Angled Triangle pattern printing
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):

        if j == 1 or j == i or i == n: # checking position of boundry for printing *
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()