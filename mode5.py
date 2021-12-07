def getPendingFines(day, Student):
    # Pending Fines
    fineList = []
    # Iterate through all student borrow/return data in the database
    for i in range(len(Student)):
        obj = Student[i]
        # If Name already exists
        index = searchName(fineList, obj[0])
        if index > -1:
            # Update fine
            fine = obj[5]
            fineList[index][1] += fine
        else:
            fine = obj[5]
            fineList.append([obj[0], fine])
    # Return Fine
    return fineList


def searchName(fineList, nameValue):
    index = -1
    for i in range(len(fineList)):
        item = fineList[i]
        # If name already exists
        if item[0] == nameValue:
            index = i
            return index
    return index


# [Latest day that the fine updated, Pending Fine]
