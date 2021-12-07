# CS131_FinalProject_Library

# Compound Computer Science 131 Final Project

## Final Project Description

Booklist.txt includes a line for each book in the library in the following form:

<book name>#<number of copies>#<restricted>

Where <book name> indicates the name of the book, <number of copies indicates> how many copies the library has and <restricted> is a TRUE/FALSE value indicating if the book has borrowing restrictions.

For example if booklist.txt contains

Introduction to python#3#TRUE

Eye of the world#1#FALSE

it means

The library has 3 copies of Introduction to python and it has borrowing restrictions. It also has one copy of Eye of the world and there are no borrowing restrictions for that book. Borrowing restrictions for a book means the book can be borrowed for at most 7 days. Books with no borrowing restrictions can be borrowed for upto 28 days.

Next we are given a log of the library's working in the form of librarylog.txt . Each line of text of the log is of one of the following types:

1. Borrow notation

B#<day>#<Student Name>#<Book name>#<days borrowed for>

2. Return notation

R#<day>#<Student Name>#<Book name>

3. Book addition

A#<day>#<Book name>

4. Fine pay notation

P#<day>#<student name>#<amount>

For example a librarylog.txt which has

B#1#adam#harry potter#6

R#10#adam#harry potter

A#11#Introduction to programming

P#15#adam#5

indicates adam borrowed harry potter on day 1 for 6 days. Adam then returned harry potter on day 10 (he was thus 3 days late). On day 11 a copy of introduction to programming was added to the library. Finally on day 15 adam paid 5 dollors towards the owed library fine dues.

The final line of librarylog.txt will include a single number which indicates the current day.

The rules of the library are :

Restricted books can be borrowed for at most 7 days. Non restricted books can be borrowed for 28 days.

Books returned late are fined 5 a day for each day late for restricted books, 1 per day late for non restricted books.

Any library user can have at most 3 books borrowed at a time.

A library user can only borrow if they have no pending fines.

New books to the library can be added as per the log, these are in addition to the original list of books in booklist. (The added book can already exist in which case its an additional copy or can be a new book)

A book can only be borrowed if there is an unborrowed copy in the library.

You program should process booklist and librarylog

And be able to answer the following questions.

1. Can a student borrow a book on a particular day for a certain number of days (this depends on how many copies remain in the library, if the person has any pending fines or too many borrowed books and consider book restriction conditions)

2. What are the most borrowed/popular books in the library (How many days were they borrowed vs not borrowed) .

3. Which books have the highest borrow ratio. You have to consider how many copies are there for this also . For example if a book has 10 copies from day 1 and 1 copy was always borrowed but another book has only 2 copies and 1 copy was borrowed half the number of days. The 2nd book has more borrow ratio. Basically for how much of the books were available vs how much they got borrowed.

4. Be able to produce sorted lists of most borrowed books/ books with highest usage ratio.

5. What are the pending fines at the end of the log/at a specific day in the log.

I will put up a test submission page with more details / clarify any doubts about the questions. However, please consider the above and try and get started on your final project. This is meant to take 3 weeks so the expectation is you start work on it as soon as break ends as it is due end of finals week.

## Project Sample IO

You have a list of two books and a third book gets added using the library log.

(Book addition clarification: Books added due to library log if new are assumed not to be restricted. If they are a book which already exists its restricted type is the restricted type of the original book. The new book added does not exist so it is not restricted)

Given this library log. The answers to questions of the various types are as follows.

### 1) Can a student borrow a book on a particular day for a certain number of days (this depends on how many copies remain in the library, if the person has any pending fines or too many borrowed books and consider book restriction conditions)

Examples:

Can lauren borrow harry potter on day 2? No as the only copy is borrowed.

Can lauren borrow harry potter on day 11? Yes

Can Adam borrow harry potter on day 12? No, he has a pending fine due to a late return

### 2) What are the most borrowed/popular books in the library (How many days were they borrowed vs not borrowed) .

For given example

The days each book was borrowed are:

harry potter 9 days by adam

Eye of the world 3 days by Lauren

Introduction to programming 3 days and then 4 days by Ishan

So the books sorted by most popular (total borrowed days are):

harry potter 9

Introduction to programming 7

Eye of the world 3

### 3) Which books have the highest borrow/ratio ratio. You have to consider how many copies are there for this also . For example if a book has 10 copies from day 1 and 1 copy was always borrowed but another book has only 2 copies and 1 copy was borrowed half the number of days. The 2nd book has more borrow ratio. Basically for how much of the books were available vs how much they got borrowed.

For the given files

Note while harry potter was borrowed 9 days it was available for 29 days. Thus its usage ratio is ~31.034% (Books in booklist are added day 1, end date is number indicated at end of list so day 30)

Eye of the world was borrowed for 3 days but it was only available for 15 days . It was added later via the library log. So its usage ratio is 20%

Introduction to programming was borrowed 7 days

Introduction to programming however had 3 copies available from day 1. Thus it was borrowed. 7 days out of a total of 87 days available across all copies. Thus its usage ratio is ~8.0459%

### 4) Be able to produce sorted lists of most borrowed books/ books with highest usage ratio.

This is covered in sections 2/3. This part just involves sorting the book lists according to most borrowed or usage ratios.

### 5) What are the pending fines at the end of the log/at a specific day in the log.

At the end of librarylog (day 30)

adam had a fine of 3 dollars as he returned a non-restricted book 3 days late on day 10 instead of 7 (which is when he should have returned it given he borrowed it on day 1 for 6 days). He then paid 2 dollars off his fine. So he still has a dollar left.

ishan had a fine of 5 since he returned 1 day late on a restricted book.

If asked the same question on day 12 Adam was the only one with a 3 dollar fine.

## Project FAQ

### When we add a book how do we know if it is restricted or not?

For added books if is a book which already exists in the booklist its restricted class is the same as the information given in the booklist. This basically means youre adding an additional copy. If it does not exist in the booklist its is NOT restricted (FALSE status)

### If someone wants to borrow a restricted book for over 7 days are they allowed to? If not, what does the program output?

No. The librarylog will not contain such instances unless it is a case of someone asking for less but then returning it late. In which case a fine is assessed. These questions will be of the form on day x can so and so borrow this book? Your program should process the log till that day and indicate yes or no if its possible or not.

### Is the fine counted from the day when the customer was suppose to return the book or after the max number of days a book can be borrowed for (customer borrowed the book for 7 days but the returned ?

From the indicated return date when the person borrowed the book.

Adam was 8 days late paying fine, so does he still have $3 + (number of days he takes to pay off the fine) ?
No there is no late penalty for fine payment. You just cant borrow books during that time

### How do we handle input/output? Can we assume that we will not be writing to the txt files (no new information is given)?

I will put up a sample solution page for this with a test booklist and librarylog. It will be in the form of a quiz. You will be given a booklist and librarylog and have to fill out quiz questions of the forms indicated.
Can so and so borrow this on day y?
On day x who is the user with the largest fine and what is the fine?
At the end of the log which book was borrowed 2nd most and how many days was it borrowed?
At the end of the log which book had 4th highest usage and what is the usage?
You fill in the answers on that canvas quiz (fill in the blanks of the canvas quiz with what your program generates) and also submit the py files of the program you wrote. Your answers determine your intial quiz score . This is done so you know quicky if you have solved the final project correctly. Following this we will go over your solution and confirm you actually has correct code which solves the problem. So just copying the answers from someone else will not work as we will verify the code works while grading. In general your scores can usually only go down from the quiz score you will be given. The only exceptions being if we notice some very simple and easily fixable error in your program while verifying. Eg you add 1 to days borrowed everywhere by mistake or some other very simple fix, or you always add extra spaces while typing out the quiz answers etc.

### Can a copy of a book that the library already has be added to the list? Do we need to check every time that a book is added to see if the library already has a copy?

Yes

### Can we assume that the log will have people only taking out 3 or less books at a time?

Should they assume that all of the actions on the library log are correct (i.e. they dont have to check if the library log entries are capable of being performed)
Yes, You can in general assume the library log is valid.

### Is the library log sorted by ascending date? like could first entry be day 8, and third entry be day 5?

Yes, the log is sorted in ascending order by date

### Can someone check out multiples copies of one book and if so, how would they differentiate between the copies for fines. I assume they cannot check out multiple copies of one book but can you confirm this?

A person is not allowed to borrow multiple copies of one book simultaneously. In fact while it is possible for a book to be returned and reborrowed that same day (by the original borrower or another person) we will avoid this in our given log just to avoid confusion. You do not need to handle this case. Basically we will avoid same say entries from the same person/book. So no day 10 someone returns and pays fine for the late return. So say 20 someone returns and borrows also etc. This is done to simply the programming. However, technically the logs within a single day are sorted according to time if you need/want to use that information.

### Can a user rack up multipe files from multiple books. What is the user starts paying fines before returning books late?

Yes it is possible to have a fine due to multiple books. However, the fines are assed when the books are returned/ on the librarylog end date. We only care about the total fine pending, not individual book fines. Also there will be no instances of a student paying a fine before a fine is assessed by the library (upon return of book or end of library log or if asked to check for user fines). Essentially you do not need to worry about students having a credit with the library or essentially racking up a fee prior to the late return and then paying midway through. The fee is only assed on return/end of librarylog (if book is not returned by end of log/ or if you are asked to asses for fines on a specific date)
