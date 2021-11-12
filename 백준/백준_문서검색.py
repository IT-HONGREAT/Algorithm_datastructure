# 입력
# ababababa
# aba
# 출력
# 2

document = str(input())
search = str(input())

index = 0
count = 0

while len(document) - index >= len(search):

    if document[index:index+len(search)] == search:
        count += 1
        index += len(search)

    else:
        index += 1

print(count)