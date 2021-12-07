data = [['Introduction to python', [[1, 2], [3, 3], [8, 5]], True, [[1, 7], [2, 5], [1, 10]]], ['Dacheng Laojiukan Quanwen Shujuku (大成老旧刊全文数据库)', [[1, 7]], True, [[1, 7], [2, 5], [1, 10]]], ['India, Raj and Empire', [[1, 4]], True, []], ['Technical Report Archive and Image Library (TRAIL)', [[1, 2]], False, []], ["Women's Studies (Adam Matthew Digital)", [[1, 11], [3, 12]], True, []], ['Medical Letter Databases', [
    [1, 1]], False, []], ['ICC Dispute Resolution Library', [[1, 2]], False, []], ['Eye of the world', [[1, 1]], False, []], ['Index Translationum', [[1, 9]], False, []], ['Taylor & Francis eBooks', [[1, 2]], True, []], ['Meiji Japan: The Edward Sylvester Morse Collection from the Peabody Essex Museum, Salem', [[1, 2]], True, []], ['Introduction to programming', [[1, 9]], False, []]]

name = data[i][0]
originalCopies = data[i][1]
restriction = data[i][2]
borrowTime = data[i][3]

name = input("Student Name")
start_date = input("Starting date")
num_of_date = input("Number of days")


def checkAvailable(name, start_date, num_of_days, Book, Student):

    def checkNumberBooks(x):

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
        smallest = startTime[len(endTime)-1]

        # set range
        x = int(smallest)
        y = int(largest)

        numberRange = list(range(smallest, largest+1))

        # [days,number of books]
        check = []

        for number in numberRange:
            count = numberRange.count(number)
            check.append([number, count])
        print("check", check)

        changeDate = []
        for item in data[0][1]:
            changeDate.append(item)
        print(changeDate)

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

        def borrow(z):
            borrowRange = list(range(borrowTime[z][0], borrowTime[z][1]+1))
            print("brorrow", borrowRange)

            i = 0
            while i < len(check):
                if check[i][1] == 0:
                    check[i][1] = 0
                elif check[i][0] in borrowRange:
                    check[i][1] = check[i][1] - 1
                i += 1

        for x in range(0, len(borrowTime)):
            borrow(x)
        print(check)
