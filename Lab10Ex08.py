'''Bài 8: Mở file Ex8.py và hoàn thành đoạn code để trích xuất các thẻ html
 có nhiều hơn 4 chữ cái. Các thẻ html mở có thể được tìm thấy bên trong các
  ký tự <> và các thẻ html đóng có thể được tìm thấy ở cùng một định dạng 
  sau ký tự </>, ví dụ <param> </param>. Kết quả sau khi chạy sẽ như sau:
['video', 'center', 'button']'''

import re

str="""<div class="tut-list tut-list-new tut-row "> 
<div class="tut-list-primary"> <div class="tut-vote"> 
<video>intro</video> 
<span class="count">50</span> <span class="tut-upvotes-text hidden">Upvotes</span> </a> </div>  
<center>k="11" rel="nofollow"></center>
<span class="tutorial-title-txt">Automate the Boring Stuff with Python</span> 
<span class="tut-title-link">  <span class="js-tutorial" data-id="3529" 
title="Automate the Boring Stuff with Python" target="_blank">(udemy.com)</span>  
</span>  </a></div> <div class="action-footer">
<form class="save-tutorial-form" method="post" <button></button> </form>"""

# Cách 2: -----------------------------------------
regex= '<([a-z]+)>'   # phần trong ngoặc sẽ được findall
match=re.findall(regex, str)
print('C2: tag html gồm ',list(set(match)))

# Cách 1: -----------------------------------------
string = str.split()

# tạo danh sách thẻ 'open html'
open_html = set(); close_html = set(); 
regex1 = "<[a-z]+>"	# tìm ký tự mở html
for i in string:
	data = re.findall(regex1, i)
	if len(data) != 0: open_html.add(data[0].replace('<','').replace('>',''))
	else: continue
	
# tạo danh sách thẻ 'close html'
regex2 = "/[a-z]+>"	# tìm ký tự đóng html
for j in string:
	data = re.findall(regex2, j)
	if len(data) != 0: close_html.add(data[0].replace('/','').replace('>',''))
	else: continue

# Tìm các thẻ html được đóng và mở trong đoạn code đề bài
tag_html = list(open_html & close_html)

#print('open html', open_html)
#print('close html', close_html)
print('C1: tag html gồm ', tag_html)

input()
