def getPopularBooks(Book):
    # Most borrowed books = days borrowed in total
    maxTime = -1
    maxBook = ""
    # Iterate through all books in the database
    for i in range(len(Book)):
        obj = Book[i]
        borrowTime = 0
        for timeTuple in obj[3]:
            borrowTime += (timeTuple[1]-timeTuple[0])
        if borrowTime > maxTime:
            maxTime = borrowTime
            maxBook = obj[0]
    return maxBook
