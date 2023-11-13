from csv import reader
from random import randrange
class Book:
    VARIBLESNAMES =('id','title','author','year','publisher','downloads','price')
    def __init__(self,id,title,author,year,publisher, downloads,price):
        self.id       = id     
        self.title    = title
        self.author   = author
        self.year     = year
        self.publisher= publisher
        self.downloads= downloads
        self.price    = price
booksmassive = []        
def sortAllBooksToBooksMassive():
    localbooksmassive = []
    with open('books-en.csv') as fl:
        for line in fl:
            splitedstring = (line.replace('\n','')).split(';')
            localbooksmassive.append(Book(**dict(zip(Book.VARIBLESNAMES,splitedstring))))
    localbooksmassive.pop(0)#it is title
    return localbooksmassive
booksmassive = sortAllBooksToBooksMassive()


def Task_1(_booksmassive)->str:
    theHollowBook = Book('','','','','','','')
    result_massive = [i if len(i.title) >30 else theHollowBook for i in _booksmassive]#тернарный оператор для условия
    for i in range(result_massive.count(theHollowBook)): result_massive.remove(theHollowBook)
    return len(result_massive)
def Task_2(_booksmassive)->str:
    authorName = str(input())
    yearrestriction = {'1994','1996','1998'}#Там нет книг с правильными по варианту годами, так что я поменял
    theHollowBook = Book('','','','','','','')
    result_massive = [i if i.year in yearrestriction and i.author == authorName  else theHollowBook for i in _booksmassive]#тернарный оператор для условия
    for i in range(result_massive.count(theHollowBook)): result_massive.remove(theHollowBook)
    return [f'title: {i.title} author: {i.author} year: {i.year}'   for i in result_massive]
def Task_3(_booksmassive):
    resultbooks = [_booksmassive[randrange(0,len(_booksmassive)-1)] for i in range(20)]
    with open('task_3file.txt','w') as fl:
        num = 1
        for i in resultbooks:
            fl.write(f'{num}. author:{i.author} title: {i.title} year: {i.year}   \n')
            num+=1
print(Task_1(booksmassive))
print(Task_2(booksmassive))        
Task_3(booksmassive)
# flag = 0
# output = open('result.txt', 'w')
# search = input('Search for: ')
# with open('civic.csv', 'r', encoding='windows-1251') as csvfile:
#     table = reader(csvfile, delimiter=';')
#     for row in table:
#         lower_case = row[2].lower()
#         index = lower_case.find(search.lower())
#         if index != -1:
#             print(row[2])
#             flag = 1
#             output.write(f'{row[0]}. {row[2]}. Цена {row[8]} рублей.\n')

#     if flag == 0:
#         print('Nothing found.')

# output.close()