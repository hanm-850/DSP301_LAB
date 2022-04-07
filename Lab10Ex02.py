'''Bài 2: lấy được các email có trong chuỗi. Kết quả sau khi chạy sẽ như sau:
['franky@google.com', 'sinatra123@yahoo.com']'''

import re
str='The advancements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
#Type your answer here.

#Cách 2: --------------------------------------

regex= '\w*@\w*.\w*'
emails=re.findall(regex, str)
print('C2: ',emails)


# Cách 1:--------------------------------------

string = str.split(' ')
regex = '((@google.com|@yahoo.com)$)'
emails = list()

for i in string:
    match = re.search(regex, i)
    if match: 
        #print('Tim thay email', i ,'nam o trong chuoi')
        emails.append(i)
print('C1 :',emails)

input()
