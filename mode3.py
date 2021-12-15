import init as init


def ratiotest(Book):
    book = []
    copies = []
    end_of_the_log = init.getLogDate()
    for i in range(len(Book)):
        t = Book[i]
        book.append(t[0])
        copies.append(t[1])
    # Total availability
    availability = []
    for i in range(len(copies)):
        if len(copies[i]) == 1:
            availability.append((end_of_the_log-1)*copies[i][0][-1])
        else:
            dates = copies[i]
            dateofcopy = []
            for date in dates:
                dateofcopy.append(date[1])
            dates.append([end_of_the_log, dates[-1][1]])
            change = 0
            for j in range(len(dates)-1):
                b = dates[j+1][0]
                a = dates[j][0]
                c = dateofcopy[j]
                change += (b-a)*c
            availability.append(change)
    # total amount of rent
    Rentdaydata = []
    for line in Book:
        Rentdays = line[3]
        Sum = 0
        for i in range(len(Rentdays)):
            RD = Rentdays[i]
            Min = RD[0]
            Max = RD[1]
            Range = Max-Min
            Sum += Range
        Rentdaydata.append(Sum)
    # Calcularing Rate
    rates = []
    for j in range(len(book)):
        rate = float(Rentdaydata[j]/availability[j])*100
        rates.append(rate)
    # Creating 2D List (Book name / Rates)
    bookratio = []
    for k in range(len(book)):
        bookratio.append([book[k], rates[k]])
    return bookratio
