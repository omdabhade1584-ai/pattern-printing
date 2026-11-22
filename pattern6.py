# Right-Aligned Triangle pattern printing
n=5
for i in range(1,n+1):
    
    for j in range(n-i): # n - i prints leading spaces
        print("  ",end=" ")
    for j in range(i):
        print(" * ",end="") # print stars with range with value of i
    print()   
    
