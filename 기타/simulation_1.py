def method_name(n, plans):
    x, y = 1, 1

    move = {
        "L": [0, -1],
        "R": [0, 1],
        "U": [-1, 0],
        "D": [1, 0],
    }

    for plan in plans:
        temp_x = x + move[plan][0]
        temp_y = y + move[plan][1]

        if temp_x < 1 or temp_y < 1 or temp_x > n or temp_y > n:
            continue

        x, y = temp_x, temp_y
    print(x, y)


if __name__ == "__main__":
    method_name(5, "RRRUDD")
