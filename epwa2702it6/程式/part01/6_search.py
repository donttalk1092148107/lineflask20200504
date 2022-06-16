import re
#re.search掃描整個字符串並返回第一個成功的匹配
str = "Hello Python Programming"
sobj = re.search(r"programming", str, re.I)
print(sobj.group())


str01 = "Hello Python Programming"
sobj01 = re.search(r"^programming", str01, re.I)
print(sobj01.group())