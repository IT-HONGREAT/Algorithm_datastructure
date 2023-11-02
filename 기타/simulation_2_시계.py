n = int(input())

count = 0
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if ("3" in str(hour)) or ("3" in str(minute)) or ("3" in str(second)):
                # print(f"{hour}:{minute}:{second}")
                count += 1
print("count : ", count)
