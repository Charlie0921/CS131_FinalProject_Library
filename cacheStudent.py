# Create cache_student.txt from dataframe
def create(dataframe):
    outputStr = ""
    for line in dataframe:
        linestr = ""
        for i in range(len(line)):
            # Student Name
            if i == 0:
                linestr += line[i]+"#"
            # Book Name
            elif i == 1:
                linestr += line[i]+"#"
            # Borrow Start Date, Borrow End Date, Return Date
            elif i <= 4:
                linestr += str(line[i])+"#"
            # [Latest day that the fine updated, Pending Fine]
            else:
                # Iterate through the list
                for fineTuple in line[i]:
                    linestr += str(fineTuple[0])+','+str(fineTuple[1])+';'
        linestr += '\n'
        outputStr += linestr
    cache_book = open("cache_student.txt", 'w', encoding='utf-8')
    cache_book.write(outputStr)
    cache_book.close()


# Read from cache_student.txt and construct a dataframe
def read():
    # [Student Name, Book Name, Borrow Start Date, Borrow End Date, Return Date, [Latest day that the fine updated, Pending Fine]]
    dataframe = []
    cache_student = open("cache_student.txt", 'r', encoding='utf-8')
    line = cache_student.readline()
    getInfo(line, dataframe)
    while line != "":
        line = cache_student.readline()
        if line != "":
            getInfo(line, dataframe)
    cache_student.close()
    return dataframe


def getInfo(string, dest):
    pcs = []
    line = string.split('#')
    for i in range(len(line)):
        item = line[i].strip()
        # Student Name, Book Name
        if i >= 0 and i <= 1:
            pcs.append(item)
        # Borrow Start, End Date
        elif i == 2 or i == 3:
            pcs.append(int(item))
        # Return Date, Fine Date
        elif i == 4:
            if item == "None":
                pcs.append(None)
            else:
                pcs.append(int(item))
        # [Latest day that the fine updated, Pending Fine]
        elif i == 5:
            # item = 1, 7; 2, 5; 1, 10;
            fineTime = []
            for fineTupleStr in item.split(';'):
                fineTuple = []
                fineTupleList = fineTupleStr.strip().split(',')
                for i in range(len(fineTupleList)):
                    if fineTupleList[i] != "":
                        fineTuple.append(int(fineTupleList[i]))
                if len(fineTuple) != 0:
                    fineTime.append(fineTuple)
            pcs.append(fineTime)
    dest.append(pcs)
    return dest
