def getPendingFines(day, Student):
    # Pending Fines
    fineList = []
    # Iterate through all student borrow/return data in the database
    for i in range(len(Student)):
        obj = Student[i]
        # If name already exists
        index = searchName(fineList, obj[0])
        if index > -1:
            # Update fine
            fine = getFineByIndex(day, i, Student)
            fineList[index][1] += fine
        else:
            fine = getFineByIndex(day, i, Student)
            if fine > 0:
                fineList.append([obj[0], fine])
    # Return Fine
    return fineList


def getFineByIndex(day, index, Student):
    data = Student[index][5]
    i = len(data)-1
    if day >= data[i][0]:
        return data[i][1]
    while i > 0:
        upper = data[i]
        lower = data[i-1]
        if day <= upper[0] and day >= lower[0]:
            if upper[0] == lower[0]:
                return upper[1]
            else:
                return lower[1]
        else:
            i -= 1


def searchName(fineList, nameValue):
    index = -1
    for i in range(len(fineList)):
        item = fineList[i]
        # If name already exists
        if item[0] == nameValue:
            index = i
            return index
    return index
