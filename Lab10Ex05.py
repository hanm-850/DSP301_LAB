'''Bài 5: Hoàn thành đoạn code để trích xuất những từ có đúng 8 ký tự 
từ chuỗi. Kết quả sau khi chạy sẽ như sau:
['empourpr', 'palmiers'] '''

import re

str='''Au pays parfume que le soleil caresse,
J'ai connu, sous un dais d'arbres tout empourpres
Et de palmiers d'ou pleut sur les yeux la paresse,
Une dame creole aux charmes ignores.'''

#Type your answer here.
# Cách 2: -----------------------------------------
regex= '(\w{8,8})'   # \w thay thế cho cụm chữ hoặc số, {8,8} là giới hạn ký tự tối thiểu, tối đa của chuỗi, phần trong ngoặc sẽ được findall
match=re.findall(regex, str)
print('C2: ',match)

# Cách 1: -----------------------------------------
string = str.replace(',\n',' ').replace('\n',' ').replace('.','').split(' ')
emails = list()
regex = '^[\w]{8,8}'
for i in string:
	l = re.match(regex, i)
	if l: emails.append(i[:8])
print('C1: ',emails)
