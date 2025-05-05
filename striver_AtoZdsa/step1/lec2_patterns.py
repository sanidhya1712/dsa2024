def pattern():
    # Ascending reverse numbers
    for i in range(0,6):
        for j in range(1, 6-i):
            print(j, end="")
        print()
    # Triangle * print
    for i in range(0,5):
        for j in range(0, 5-i):
            print(" ", end="")
        for j in range(0, 1+2* i):
            print("*", end="")
        for j in range(0, 5-i):
            print(" ", end="")
        print()
    # Ascending reverse alphabets
    for i in range(0,6):
        for j in range(0, i):
            print(chr(ord('A')+(5-i+j)), end="")
        print()
pattern()