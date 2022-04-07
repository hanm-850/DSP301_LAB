'''Bài 3: Hoàn thành đoạn code để lấy được các email có trong chuỗi đó
(chỉ lấy phần ở trước ký tự '@' và ký tự '@').
Kết quả sau khi chạy sẽ như sau:
['franky@', 'sinatra123@']'''

import re

str='The advancements in biomarine studies franky@google.com with \
the investments necessary and Davos sinatra123@yahoo.com Then The \
New Yorker article on wind farms...'
#Type your answer here.
# Cách 2: -----------------------------------------
regex= '[\w]*@'   # \w là lọc chuỗi và số, sau đó kết thúc bằng @
emails=re.findall(regex, str)
print('C2: ',emails)
# Cách 1: -----------------------------------------
string = str.split(' ')
regex = '((@google.com|@yahoo.com)$)'
emails = list()

for i in string:
    match = re.search(regex, i)
    if match: 
        j = re.findall('^[\w].+@', i)    # \w tương đương với [a-zA-Z0-9_]
        emails.append(j[0])
print('C2: ',emails)

input()




