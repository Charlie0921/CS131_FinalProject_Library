# Import Modules
import init as init
import mode1 as m1
import mode2 as m2
import mode3 as m3
import mode4 as m4
import mode5 as m5

welcome_msg = "\n 1) Can a student borrow a book on a particular day for a certain number of days?\n 2) What are the most borrowed/popular books in the library?\n 3) Which books have the highest borrow ratio?\n 4) Sorted lists of most borrowed books / books with highest usage ratio.\n 5) What are the pending fines at the end of the log/at a specific day in the log?\n Press any other key to exit\n\n"

# Retrieve Book dataframe from 'booklist.txt'
Book = init.read()
# Update Book dataframe & Create Student dataframe through 'librarylog.txt'
Student = []
init.update(Book, Student)

while True:
    mode_select = int(input(welcome_msg))
    if mode_select == 1:
        # Borrow Availability
        name = input("Student Name: ")
        start_date = int(input("Starting date: "))
        num_of_date = int(input("Number of days: "))
        book_name = input("Name of the book: ")
        m1.checkAvailable(name, start_date, num_of_date,
                          book_name, Book, Student)
    elif mode_select == 2:
        # Popular books
        print(m2.getPopularBooks(Book))
    elif mode_select == 3:
        # Borrow Ratio
        book_ratio = m3.ratiotest(Book)
        for line in book_ratio:
            print(line[0]+" | Ratio: "+str(line[1])+"%")
    elif mode_select == 4:
        # Sorted List of books (replace 'pass' with corresponding functions)
        book_ratio = m3.ratiotest(Book)
        book_sorted = m4.sortlist(book_ratio)
        for line in book_sorted:
            print(line[0]+" | Ratio: "+str(line[1])+"%")
    elif mode_select == 5:
        # Pending Fines
        uin = input("On which day? Type F for the day at the end of the log: ")
        if uin == "F":
            day = init.getLogDate()
        else:
            day = int(uin)
        finelist = m5.getPendingFines(day, Student)
        if len(finelist) == 0:
            print("There's no pending fine for day", day)
        for tup in finelist:
            print(tup[0]+": "+str(tup[1]))
    else:
        break
