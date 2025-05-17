lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

books_dict = {}
for line in lines:
    author, book = line.split(':')
    author = author.strip()
    book = book.strip()
    if author in books_dict:
        books_dict[author].append(book)
    else:
        books_dict[author] = [book]

for author in books_dict:
    books_dict[author].sort()

print(books_dict)