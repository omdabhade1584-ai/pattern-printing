# Star Pyramid pattern printing
n = 5

for i in range(1, n + 1):
   
    for j in range(n - i):  #this loop Print spaces 
        print(" ", end="")

    
    for j in range(2 * i - 1): # this loop Print stars
        print("*", end="")

    print()