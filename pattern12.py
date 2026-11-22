# Butterfly Pattern printing
n = 5

# Upper half
for i in range(1, n + 1):

    # Left stars
    for j in range(1, i + 1):
        print("*", end=" ")

    # Middle spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")

    # Right stars
    for j in range(1, i + 1):
        print("*", end=" ")

    print()


# Lower half
for i in range(n - 1, 0, -1):

    # Left stars
    for j in range(1, i + 1):
        print("*", end=" ")

    # Middle spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")

    # Right stars
    for j in range(1, i + 1):
        print("*", end=" ")

    print()