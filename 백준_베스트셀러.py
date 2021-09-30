# 5
# top
# top
# top
# top
# kimtop


n = int(input())

books = {}

for _ in range(n):
    book = str(input())

    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

best = max(books.values())

answer = []
for book, count in books.items():
    if count == best:
        answer.append(book)


# print(books.items())
print(sorted(answer)[0])
