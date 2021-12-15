import init as init
import mode5 as m5

# Retrieve Book dataframe from 'booklist.txt'
Book = init.read()
# Update Book dataframe & Create Student dataframe through 'librarylog.txt'
Student = []
init.update(Book, Student)

#######################################check fine#########################################################


def checkFine(Student, name, day):
    finelist = m5.getPendingFines(day, Student)
    isIntheList = False
    for fine in finelist:
        if fine[0] == name:
            isIntheList = True
            break
    if isIntheList:
        if fine[1] == 0:
            return False
        else:
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
    largest = init.getLogDate()

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
    return check

#####################################Check available using dates#######################################

# check if the person can borrow base on the number of book(if 0 books can't borrow)


def checkAvailableDates(check, start_date, num_of_days):
    end_date = int(start_date + num_of_days)
    isValid = True
    for j in range(0, len(check)):
        day = []
        numberBook = []
        days = check[j][0]
        numberBooks = check[j][1]
        day.append(days)
        numberBook.append(numberBooks)
        for testDate in range(start_date, end_date+1):
            for item in day:
                if item == testDate:
                    print("testDate", testDate)
                    print("item", item)
                    index1 = int(day.index(item))
                    if numberBook[index1] == 0:
                        print("numberBook", numberBook[index1])
                        isValid = False
                        break
    return isValid

###################################Check student books################


singleStudentLst = []


def singleStudent(Student, student_name):
    for i in range(0, len(Student)):
        if Student[i][0] == student_name:
            singleStudentLst.append(Student[i])

    print("single", singleStudentLst)


# get a largest day
largestBorrowDay = init.getLogDate()

# get a smallest day

borrowDayList = []


def dayList(singleStudentLst):
    borrow = []
    for i in range(0, len(singleStudentLst)):
        whenBorrow = singleStudentLst[i][2]
        whenReturn = singleStudentLst[i][4]
        borrow.append(whenBorrow)
    borrow.sort()
    smallestBorrowDay = borrow[0]

    for i in range(smallestBorrowDay, largestBorrowDay + 1):
        borrowDayList.append([i, 0])

    print(borrowDayList)

# change the numbers of the list


def canBorrow(borrowDayList):
    for i in range(0, len(singleStudentLst)):
        whenBorrow = singleStudentLst[i][2]
        whenReturn = singleStudentLst[i][4]
        studentBorrow = list(range(whenBorrow, whenReturn+1))
        print("studentborrow", studentBorrow)

    # change coies of books
    j = 0
    while i < len(borrowDayList):
        if borrowDayList[i][1] == 0:
            borrowDayList[i][1] = 0
        elif borrowDayList[i][0] in studentBorrow:
            borrowDayList[i][1] = borrowDayList[i][1] + 1
        i += 1

    print("hello ", borrowDayList)


# main


def checkStudentBooks(Student, student_name):
    singleStudent(Student, student_name)
    dayList(singleStudentLst)
    canBorrow(borrowDayList)

#########################################Main######################################


def checkAvailable(student_name, start_date, num_of_days, book_name, Book, Student):
    # 1. Check if the user has a pending fine -> if hasFine is True, user has a pending fine.
    hasFine = checkFine(Student, student_name, start_date)
    print(hasFine)

    # Check if the requested days are available
    data = findBookRow(Book, book_name)
    check = checkNumberBooks(data)
    # 3. if hasBook is True, there is a book for a user to borrow
    hasBook = checkAvailableDates(check, start_date, num_of_days)
    print(hasBook)

    # 2. Check if the user has borrowed over 3 books
    yesBook = checkStudentBooks(Student, student_name)


checkAvailable("Greg", 76, 5, "Intro to python", Book, Student)
