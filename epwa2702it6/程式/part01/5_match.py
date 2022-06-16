import re
#re.match嘗試從字符串的初始位置匹配一個模式，如果不是起始位置匹配成功的話，match（）就返回none。
m = re.match(r'www\.(.+)\.com', 'www.google.com')
print(m.group(0))
print(m.group(1))

m01 = re.match(r'[a-z]+','tem12po')
print(m01)
if not m01==None:
    print(m01.group())
    print(m01.start())
    print(m01.end())
print(m01.span())


strTest = "Hello Python Programming"
mobj = re.match(r"hell", strTest, re.I)
print(mobj.group())