length = int(input("введите число: "))
height = int(input('введите второе число: '))

for i in range(height):
    for j in range(length):
        if i == 0 or i == height - 1 or j == 0 or j == length - 1:
            print("A", end="")
            continue

        print("B", end="")
    print()