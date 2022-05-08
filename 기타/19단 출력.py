for i in range(1, 20):
    for j in range(1, 20):
        if j % 2 != 0 and j != 19:
            print(i, "*", j, "=", i * j, end=" / ")
        elif j == 19:
            print(i, "*", j, "=", i * j)
        else:
            print(i, "*", j, "=", *j)
