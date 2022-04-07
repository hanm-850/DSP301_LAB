'''Bài 1: Mở file Ex1.py và hoàn thành đoạn code để lấy các dòng 
được bắt đầu bằng ký tự ">", kết quả sau khi chạy sẽ như sau: 
['>Venues', '>Marketing', '>medalists', '>Controversies', '>Paralympics', 
'>snowboarding', '>Netherlands', '>Norway', '>References', '>edit', 
'>Norway', '>Germany', '>Canada', '>Netherlands', '>Japan', '>Italy', 
'>Belarus', '>China', '>Slovakia', '>Slovenia', '>Belgium', '>Spain', 
'>Kazakhstan', '>1964', '>1968', '>1972', '>1992', '>1996', '>2000']'''

import re
str="""
>Venues
>Marketing
>medalists
>Controversies
>Paralympics
>snowboarding
>[1]
>Netherlands
>[2]
>Norway
>[10]
>[11]
>References
>edit
>[12]
>Norway
>Germany
>Canada
>Netherlands
>Japan
>Italy
>Belarus
>China
>Slovakia
<$#%#$%
<#$#$$
<**&&^^
>Slovenia
>Belgium
>Spain
>Kazakhstan
>[15]
>1964
>1968
>1972
>1992
>1996
>2000"""
#Type your answer here.
# Cách 2: -----------------------------------------
regex= '(>[\w]+)'   # > là lọc chuỗi có dấu lớn hơn, dấu + là buộc phải có ký tự chữ số sau >, phần trong ngoặc tròn sẽ được findall
match=re.findall(regex, str)
print('C2: ',match)


# Cách 1: -----------------------------------------
str1 = str.split('\n')

patern = '(?!.*[<[])' #lọc các chuỗi không bao gồm ký tự < và ký tự [ 
str2 = list()
for i in str1:
    data = re.match(patern, i)
    if data and i !='': str2.append(i)
print('C1: ',str2)

input()
