# Heart Shape in Python

# Define the size of the heart
size = 15

# Top part of the heart
for a in range(size//2, size, 2):
    for b in range(1, size - a, 2):
        print(" ", end="")
    for c in range(1, a + 1):
        print("♥", end="")
    for b in range(1, size - a + 1):
        print(" ", end="")
    for c in range(1, a + 1):
        print("♥", end="")
    print()

# Bottom part of the heart
for a in range(size, 0, -1):
    for b in range(a, size):
        print(" ", end="")
    for c in range(1, (a * 2)):
        print("♥", end="")
    print()
