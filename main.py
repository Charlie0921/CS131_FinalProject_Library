# Import Modules
import bookList as bookList
import cacheStudent as cacheStudent
import cacheBook as cacheBook
import libraryLog as libLog
import mode1 as m1
import mode2 as m2
import mode5 as m5

welcome_msg = " 1) Can a student borrow a book on a particular day for a certain number of days?\n 2) What are the most borrowed/popular books in the library?\n 3) Which books have the highest borrow ratio?\n 4) Sorted lists of most borrowed books / books with highest usage ratio.\n 5) What are the pending fines at the end of the log/at a specific day in the log?\n Press any other key to exit\n"

# Read book list from 'booklist.txt'
booklist = bookList.read()
# Update booklist by using 'librarylog.txt'
libLog.update(booklist)
# Get cache_book and cache_student database
Book = cacheBook.read()
Student = cacheStudent.read()
print(Book)
print(Student)

while True:
    mode_select = int(input(welcome_msg))
    if mode_select == 1:
        name = input("Student Name")
        start_date = input("Starting date")
        num_of_date = input("Number of days")
        m1.checkAvailable(name, start_date, num_of_date, Book, Student)
        # Borrow Availability (replace 'pass' with corresponding functions)
        pass
    elif mode_select == 2:
        # Popular books
        print(m2.getPopularBooks(Book))
    elif mode_select == 3:
        # Borrow Ratio (replace 'pass' with corresponding functions)
        pass
    elif mode_select == 4:
        # Sorted List of books (replace 'pass' with corresponding functions)
        pass
    elif mode_select == 5:
        # Pending Fines
        uin = input("On which day? Type F for the day at the end of the log: ")
        if uin == "F":
            day = libLog.getLogDate()
        else:
            day = int(uin)
        print(day)
        m5.getPendingFines(day, Book, Student)
    else:
        break
