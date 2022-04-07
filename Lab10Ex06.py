'''
Bài số 6:
Hoàn thành đoạn code để trích xuất những số bắt đầu với '212'. Kết quả sau khi chạy sẽ như sau:
['21299']'''

import re
str='''Ancient Script 21299: The Takenouchi documents are the ancient historical records that have been secretly preserved and passed down from generation to generation by the Takenouchi family, the head of family being the chief priest of the Koso Kotai Jingu shrine. 212-111-5932 '''
string = str.split()
#Type your answer here.

regex = '(212+\d+)' #\d tương ứng với digit [0-9], (+) có thể khớp với chuỗi có một hoặc nhiều ký tự được định nghĩa trước nó
data = re.findall(regex, str)
print(data)
