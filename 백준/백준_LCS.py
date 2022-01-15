# ACAYKP
# CAPCAK


str_1 = input()
str_2 = input()

check = [[0] * (len(str_2) + 1) for _ in range(len(str_1) + 1)]

for i in range(1, len(str_1) + 1):
    for j in range(1, len(str_2) + 1):
        if str_1[i - 1] == str_2[j - 1]:
            check[i][j] = check[i - 1][j - 1] + 1
        else:
            check[i][j] = max(check[i][j - 1], check[i - 1][j])

print(check[len(str_1)][len(str_2)])
