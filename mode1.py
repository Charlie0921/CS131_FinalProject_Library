import init as init
import mode5 as m5

# Retrieve Book dataframe from 'booklist.txt'
Book = init.read()
# Update Book dataframe & Create Student dataframe through 'librarylog.txt'
Student = []
init.update(Book, Student)

#######################################check fine#########################################################


def checkFine(Student, name):
    studentLst = []
    for item in Student:
        if name == item[0]:
            studentLst.append(item)
    fine = m5.getPendingFines(29, studentLst)[0][1]
    if fine == 0:
        return True
    else:
        return False

######################################################borrow########################################
# calculate number of books after borrowing


def borrow(check, borrowTime, z):
    borrowRange = list(range(borrowTime[z][0], borrowTime[z][1]+1))
    print("borrow", borrowRange)
    i = 0
    while i < len(check):
        if check[i][1] == 0:
            check[i][1] = 0
        elif check[i][0] in borrowRange:
            check[i][1] = check[i][1] - 1
        i += 1
    return check

######################################check number books#####################################################


def findBookRow(Book, name):
    for line in Book:
        if line[0] == name:
            return line


def checkNumberBooks(Bookdata):
    borrowTime = Bookdata[3]
    check = []
    if len(borrowTime) == 0:
        largest = 31
    else:
        # pick the highest number of the end time
        endTime = []
        for index in range(0, len(borrowTime)):
            endTime.append(borrowTime[index][1])
        endTime.sort()
        largest = endTime[len(endTime)-1]
        # pick the lowest number of the start time
        startTime = []
        for index in range(0, len(borrowTime)):
            startTime.append(borrowTime[index][0])
        startTime.sort()
        startTime.reverse()
    numberRange = list(range(1, largest+1))
    print(numberRange)
    # [days,number of books]
    for number in numberRange:
        count = numberRange.count(number)
        check.append([number, count])
    print("check", check)

    changeDate = []
    for item in Bookdata[1]:
        changeDate.append(item)
    print("changeDate", changeDate)

    # change copies of books in 2d list
    j = 0
    while j < len(check):
        i = 0
        while i < len(changeDate):
            if check[j][0] == changeDate[i][0]:
                check[j][1] = changeDate[i][1]
                break
            else:
                check[j][1] = check[j-1][1]
            i += 1
        j += 1
    print(check)

    # calculate number of books after borrowing
    for z in range(0, len(borrowTime)):
        check = borrow(check, borrowTime, z)
    print("number of books after borrowing", check)


#####################################Check available using dates#######################################

# check if the person can borrow base on the number of book(if 0 books can't borrow)
def checkAvailableDates():
    end_date = int(start_date + num_of_days)
    isValid = True
    for j in range(0, len(check)):
        day = []
        numberBook = []
        days = check[j][0]
        numberBooks = check[j][1]
        day.append(days)
        numberBook.append(numberBooks)

        for testDate in range(start_date, end_date):
            for item in day:
                if item == testDate:
                    print("testDate", testDate)
                    print("item", item)
                    index1 = int(day.index(item))
                    if numberBook[index1] == 0:
                        print("numberBook", numberBook[index1])
                        isValid = False
                        break
    if isValid == False:
        print("You can't borrow")
    else:
        print("You can borrow")


# OVERALL##################################################3
# name, book name, 언제 빌려, 언제 반납, 실제 반납일, [날짜, fine]
name = "Greg"
start_date = 10
num_of_days = 2
book_name = "Technical Report Archive and Image Library (TRAIL)"


def checkAvailable(name, start_date, num_of_days, book_name, Book):
    data = Book

    check = []
    checkNumberBooks(name, Student)

    # entering input and outputting result
    """
    bookData = data[i][0]
    originalCopies1 = data[i][1]
    restriction1 = data[i][2]
    borrowTime = data[i][3]
    index = i 
    """

    checkBorrowBook()

    for i in range(0, len(data)):

        if book_name == bookData:
            print(index)
            checkNumberBooks(index)
            checkAvailableDates()


checkAvailable(name, start_date, num_of_days, book_name, Book)
