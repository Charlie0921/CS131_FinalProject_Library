# Construct a dataframe by reading through the booklist
def read():
    # [Book Name, Total Copies, Restriction, Borrow Time]
    dataframe = []
    booklist = open("booklist.txt", 'r', encoding='utf-8')
    line = booklist.readline()
    addInfo(line, dataframe)
    while line != "":
        line = booklist.readline()
        if line != "":
            addInfo(line, dataframe)
    booklist.close()
    return dataframe


# Process each line of the list
def addInfo(string, dest):
    pcs = []
    line = string.split('#')
    for i in range(len(line)):
        item = line[i].strip()
        # Book Name
        if i == 0:
            pcs.append(item)
        # Total Number of Copies
        elif i == 1:
            # [Date, Total copies]
            pcs.append([[1, int(item)]])
        # Book Restriction
        elif i == 2:
            if item == "FALSE":
                pcs.append(False)
            elif item == "TRUE":
                pcs.append(True)
            else:
                ValueError
    # Places for Borrow Time Tuple data
    pcs.append([])
    dest.append(pcs)
    return dest
