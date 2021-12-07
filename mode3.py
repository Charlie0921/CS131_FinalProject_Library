'''
2. 분모 - cache_book.txt 데이터 사용
a) 데이터에서 line을 추출
b) Total Copies의 리스트들만 추출
c) 제일 마지막 리스트의 마지막 element를 분모로 사용
'''


def ratiotest(book_ratio):
    Book = input("Book you want: ")

    # library 3
    book = []
    copies = []

    # book = [책제목...]
    # copies = [책 소유량]

    for i in range(len(booklist)):
        t = list(booklist[i])
        book.append(t[0])
        copies.append(t[1])

    # booklist에서 가져온 것들
    # changed amount of book
    # 분모 v1
    '''
    분모 -> 책을 빌릴 수 있는 기회 총 횟수
    기간을 30일이라 했을 때: 
    Total Copies = [1,3][4,4][8,5]

    p=[4,16]
    min = p[0]
    max = p[1]
    range = max-min+1
    print(range)
    '''
    x = "end point"
    Booknote = list(cache_book)
    Trent = list(cache_book[1])
    date = []
    for i in range(len(Trent)):
        Tr = list(Trent[i])
        max_d = Tr[1]
        min_d = Tr[0]
        tday = Tr[1]-Tr[0]
        date.append(tday)

    # total amount of rent
    # 분자 v2
    Rentdaydata = []
    Rentdays = list(cache_book[3])
    for i in range(len(Rentdays)):
        for j in range(len(RD)):
            sum = 0
            RD = list(Rentdays[j])
            min = RD[0]
            max = RD[1]
            range = max-min+1
            sum += range
        Rentdaydata.append(sum)
    # Calcularing Rate
    rate = []
    for j in range(len(copies)):
        r = copies[j]-data[j]/copies[j]
        r.append(rate)
    # Creating 2D List (Book name / Rates)
    bookratio = []
    for k in range(len(book)):
        x = []
        x.append(book[k])
        x.append(rate[k])
        bookratio.append(x)
    # [
    #    [book name / ratio]
    #    .
    #    .
    #    .
    # ]
