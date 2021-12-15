# Construct a dataframe by reading through the booklist
def read():
    # [Book Name, Total Copies, Restriction, Borrow Time]
    dataframe = []
    booklist = open("booklist.txt", 'r', encoding='utf-8')
    line = booklist.readline()
    addInfo(line, dataframe)
    while line != "":
        line = booklist.readline()
        if line != "":
            addInfo(line, dataframe)
    booklist.close()
    return dataframe


# Process each line of the list
def addInfo(string, dest):
    pcs = []
    line = string.split('#')
    for i in range(len(line)):
        item = line[i].strip()
        # Book Name
        if i == 0:
            pcs.append(item)
        # Total Number of Copies
        elif i == 1:
            # [Date, Total copies]
            pcs.append([[1, int(item)]])
        # Book Restriction
        elif i == 2:
            if item == "FALSE":
                pcs.append(False)
            elif item == "TRUE":
                pcs.append(True)
            else:
                ValueError
    # Places for Borrow Time Tuple data
    pcs.append([])
    dest.append(pcs)
    return dest


# Return EOL (End of Log) date from the librarylog.txt
def getLogDate():
    logcalls = open("librarylog.txt", 'r', encoding='utf-8')
    lastDate = -1
    line = logcalls.readline()
    while line != "":
        line = logcalls.readline()
        if len(line.strip().split('#')) == 1 and line != "":
            lastDate = int(line.strip())
    logcalls.close()
    return lastDate


# Update two databases from librarylog.txt records
def update(Book, Student):
    # Data
    student_data = Student
    book_data = Book
    # Read through log file and process
    logcalls = open("librarylog.txt", 'r', encoding='utf-8')
    line = logcalls.readline()
    ReadCommand(line.split('#'), student_data, book_data)
    while line != "":
        line = logcalls.readline()
        if line != "":
            ReadCommand(line.split('#'), student_data, book_data)
    logcalls.close()
    EOL = getLogDate()
    # From student_data, find if somebody did not return the book by the EOL
    for i in range(len(student_data)):
        log = student_data[i]
        if log[4] == None:
            # Make it returned by the end
            returnBooks(EOL, log[0], log[1], student_data, book_data)
    # Update changes to two databases
    Student = student_data
    Book = book_data


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


# Add new line to student_data and modify borrow time portion of book_data
def borrowBooks(day, student_name, book_name, days_borrowed, student_data, book_data):
    # Dataframe Information
    day = int(day)
    days_borrowed = int(days_borrowed)
    # [Student Name, Book Name, Borrow Start, Borrow End, Return Date, [Day, Fine]]
    borrow_info = [student_name, book_name, day,
                   day+days_borrowed, None, [[1, 0]]]
    student_data.append(borrow_info)
    # Find book on book database
    for i in range(len(book_data)):
        if book_data[i][0] == book_name:
            # Add Borrow time to the book data
            book_data[i][3].append([day, day+days_borrowed])
            break


# Modify return date portion of student_data
def returnBooks(day, student_name, book_name, student_data, book_data):
    day = int(day)
    # Find the latest borrow record for given student name and book name
    index = -1
    i = len(student_data)-1
    while i >= 0:
        if student_data[i][0] == student_name and student_data[i][1] == book_name:
            index = i
            break
        i -= 1
    # [Borrow Start Date, Borrow End Date]
    rent_info = [student_data[index][2], student_data[index][3]]
    # Find whether the book is restricted or not
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
        newfine = fine_rate * \
            (int(student_data[index][4]) - int(student_data[index][3]))
        if newfine > 0:
            # Update fine as the return date is given
            student_data[index][5].append([day, newfine])
        else:
            student_data[index][5].append([day, 0])


# Modify [Day, Fine] portion of student_data
def payFines(day, student_name, amount, student_data):
    day = int(day)
    remaining_fine = int(amount)
    for i in range(len(student_data)):
        # Find a data with given student name and pending fine
        if student_data[i][0] == student_name and student_data[i][5][-1][-1] != 0:
            # There is a pending fine
            if remaining_fine >= student_data[i][5][-1][-1]:
                remaining_fine -= student_data[i][5][-1][-1]
                student_data[i][5].append([day, 0])
            else:
                student_data[i][5].append(
                    [day, student_data[i][5][-1][-1] - remaining_fine])
                remaining_fine = 0


# Add book to the book_data
def addBooks(day, book_name, book_data):
    day = int(day)
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
