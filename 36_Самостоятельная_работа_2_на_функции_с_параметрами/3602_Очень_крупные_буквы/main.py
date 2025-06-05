def huge_letters():
    global page
    page = page.split()
    for i in range(len(page)):
        if i % 2 == 0:
            page[i] = page[i].lower()
    page.sort(reverse=True, key=lambda item: (len(item)))
    page = " ".join(page)
    return