import re
#re.compile用於編譯正則表達式，生成一個正則表達式（Pattern）對象，供match（）和search（）這兩個函數使用。
pat = re.compile('[a-z]+')

m = pat.findall('tem12po')
print(m) 