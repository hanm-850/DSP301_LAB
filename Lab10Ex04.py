'''Bài 4: MHoàn thành đoạn code tương tự như bài 3, nhưng lần này 
không lấy ký tự '@' nữa. Kết quả sau khi chạy sẽ như sau:
['franky', 'sinatra123']'''

import re

str='The advancements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
#Type your answer here.
# Cách 2: -----------------------------------------
regex= '([\w]*)@'   # \w là lọc chuỗi và số, sau đó kết thúc bằng @, phần trong ngoặc tròn sẽ được findall
emails=re.findall(regex, str)
print('C2: ',emails)

# Cách 1: -----------------------------------------
string = str.split(' ')
regex = '((@google.com|@yahoo.com)$)'
emails = list()

for i in string:
    match = re.search(regex, i)
    if match: 
        j = re.findall('^[\w].+@', i) # \w tương đương với [a-zA-Z0-9]
        k = j[0][:len(j[0])-1]
        emails.append(k)
print('C1: ',emails)
input()
