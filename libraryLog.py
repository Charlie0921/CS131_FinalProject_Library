# Import Modules
import cacheStudent as cacheStudent
import cacheBook as cacheBook


def getLogDate():
    logcalls = open("librarylog.txt", 'r', encoding='utf-8')
    lastDate = -1
    line = logcalls.readline()
    lastDate = int(line.split('#')[1].strip())
    while line != "":
        line = logcalls.readline()
        if line != "":
            lastDate = int(line.split('#')[1].strip())
    logcalls.close()
    return lastDate


def update(booklist):
    # Data
    student_data = []
    book_data = booklist
    # Read through log file and process
    logcalls = open("librarylog.txt", 'r', encoding='utf-8')
    line = logcalls.readline()
    ReadCommand(line.split('#'), student_data, book_data)
    while line != "":
        line = logcalls.readline()
        if line != "":
            ReadCommand(line.split('#'), student_data, book_data)
    logcalls.close()
    # Backup data into cache_book.txt and cache_student.txt
    cacheBook.create(book_data)
    cacheStudent.create(student_data)


def ReadCommand(code, student_data, book_data):
    command = []
    for i in range(len(code)):
        command.append(code[i].strip())

    # Call proper commands
    identifier_code = command[0]

    # [Borrow Notation]
    if identifier_code == "B":
        # B  # <day>#<Student Name>#<Book name>#<days borrowed for>
        day = command[1]
        student_name = command[2]
        book_name = command[3]
        days_borrowed = command[4]
        borrowBooks(day, student_name, book_name,
                    days_borrowed, student_data, book_data)

    # [Return Notation]
    elif identifier_code == "R":
        # R  # <day>#<Student Name>#<Book name>
        day = command[1]
        student_name = command[2]
        book_name = command[3]
        returnBooks(day, student_name, book_name, student_data, book_data)

    # [Book Addition]
    elif identifier_code == "A":
        # A  # <day>#<Book name>
        day = command[1]
        book_name = command[2]
        addBooks(day, book_name, book_data)

    # [Fine Pay Notation]
    elif identifier_code == "P":
        # P  # <day>#<student name>#<amount>
        day = command[1]
        student_name = command[2]
        amount = command[3]
        payFines(day, student_name, amount, student_data)
    else:
        # Identifier code does not exist => End of the log
        NameError


# Add new line to student_data and modify borrow time portion of book_data
def borrowBooks(day, student_name, book_name, days_borrowed, student_data, book_data):
    # Dataframe Information
    # [Student Name, Book Name, Borrow Start, Borrow End, Return Date, [Days, Pending Fines]]
    borrow_info = [student_name, book_name, day,
                   day+days_borrowed, None, []]
    student_data.append(borrow_info)
    # Find book on book database
    for i in range(len(book_data)):
        if book_data[i][0] == book_name:
            # Add Borrow time to the book data
            book_data[i][3].append([day, day+days_borrowed])
            break
    print("BORROW BOOKS [200]")


# Modify return date portion of student_data
def returnBooks(day, student_name, book_name, student_data, book_data):
    # Update books dataframe to address the remaining books
    index = -1
    for i in range(len(student_data)):
        if student_data[i][0] == student_name and student_data[i][1] == book_name:
            index = i
            break
    # Find whether the book is restricted or not
    rent_info = [student_data[index][2], student_data[index][3]]
    fine_rate = 0
    for i in range(len(book_data)):
        if book_data[i][0] == book_name:
            # Check the restriction
            if book_data[i][2]:
                fine_rate = 5
            else:
                fine_rate = 1
            # Update borrow time by new return date
            borrow_time_index = book_data[i][3].index(rent_info)
            rent_info = [student_data[index][2], day]
            book_data[i][3][borrow_time_index] = rent_info

    # If there is an existing borrow record in student_data
    if index > -1:
        student_data[index][4] = day  # Update return date
        # Update fine as the return date is given
        student_data[index][5] = [day, fine_rate *
                                  (int(student_data[index][4]) - int(student_data[index][3]))]
    print("RETURN BOOKS [200]")


# Modify fine & finedate portion of student_data
def payFines(day, student_name, amount, student_data):
    remaining_fine = int(amount)
    for i in range(len(student_data)):
        if student_data[i][0] == student_name and student_data[i][5] != 0:
            # There is a pending fine
            if remaining_fine >= student_data[i][5]:
                remaining_fine -= student_data[i][5]
                student_data[i][5] = 0
            else:
                student_data[i][5] -= remaining_fine
                remaining_fine = 0
            # Update the latest day the fine is paid
            student_data[i][6] = day
    print("PAY FINE [200]")


# Add book to the book_data
def addBooks(day, book_name, book_data):
    index = -1
    for i in range(len(book_data)):
        if book_data[i][0] == book_name:
            index = i
            break
    # If the book already exists
    if index > -1:
        book_data[index][1].append([day, book_data[index][1][-1][1]+1])
    # If the book does not exist
    else:
        book_data.append([book_name, [day, 1], False, []])
    print("ADD BOOKS [200]")
