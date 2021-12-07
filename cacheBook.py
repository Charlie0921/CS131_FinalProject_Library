# Read from cache_book.txt and construct a dataframe
def read():
    # [Book Name, Total Copies, Restriction, Borrow Time]
    dataframe = []
    cache_book = open("cache_book.txt", 'r', encoding='utf-8')
    line = cache_book.readline()
    getInfo(line, dataframe)
    while line != "":
        line = cache_book.readline()
        if line != "":
            getInfo(line, dataframe)
    cache_book.close()
    return dataframe


def getInfo(string, dest):
    pcs = []
    line = string.split('#')
    for i in range(len(line)):
        item = line[i].strip()
        # Book Name
        if i == 0:
            pcs.append(item)
        # Total Number of Copies
        elif i == 1:
            # item = 1, 3; 4, 4; 12, 5;
            copyTime = []
            for copyTupleStr in item.split(';'):
                copyTuple = []
                copyTupleList = copyTupleStr.strip().split(',')
                for i in range(len(copyTupleList)):
                    if copyTupleList[i] != "":
                        copyTuple.append(int(copyTupleList[i]))
                if len(copyTuple) != 0:
                    copyTime.append(copyTuple)
            pcs.append(copyTime)
        # Book Restriction
        elif i == 2:
            if item == "False":
                pcs.append(False)
            elif item == "True":
                pcs.append(True)
            else:
                ValueError
        # Borrow Time
        else:
            # item = 1, 7; 2, 5; 1, 10;
            borrowTime = []
            for timeTupleStr in item.split(';'):
                timeTuple = []
                timeTupleList = timeTupleStr.strip().split(',')
                for i in range(len(timeTupleList)):
                    if timeTupleList[i] != "":
                        timeTuple.append(int(timeTupleList[i]))
                if len(timeTuple) != 0:
                    borrowTime.append(timeTuple)
            pcs.append(borrowTime)
    dest.append(pcs)
    return dest


# Construct another file from the dataframe
def create(dataframe):
    outputStr = ""
    for line in dataframe:
        linestr = ""
        for i in range(len(line)):
            # Book Name
            if i == 0:
                linestr += line[i]+"#"
            # Total Copies
            if i == 1:
                # Iterate through the list
                for copyTuple in line[i]:
                    linestr += str(copyTuple[0])+','+str(copyTuple[1])+';'
                linestr += "#"
            # Restriction:
            if i == 2:
                linestr += str(line[i])+"#"
            # Borrow Time
            if i == 3:
                # Iterate through the list
                for timeTuple in line[i]:
                    linestr += str(timeTuple[0])+','+str(timeTuple[1])+';'
        linestr += '\n'
        outputStr += linestr
    cache_book = open("cache_book.txt", 'w', encoding='utf-8')
    cache_book.write(outputStr)
    cache_book.close()
