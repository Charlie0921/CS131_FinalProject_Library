def getFineByIndex(day, index, Student):
    data = Student[index][5]
    i = len(data)-1
    if day >= data[i][0]:
        return data[i][1]
    while i > 0:
        upper = data[i]
        lower = data[i-1]
        print(lower[0], upper[0])
        if day <= upper[0] and day >= lower[0]:
            if upper[0] == lower[0]:
                return upper[1]
            else:
                return lower[1]
        else:
            i -= 1


Student = [['ishan', 'Introduction to python', 25,
           28, 29, [[1, 0], [15, 7], [29, 5], [29, 4], [33, 1]]]]
index = 0

day = int(input("day: "))

print(getFineByIndex(day, index, Student))
