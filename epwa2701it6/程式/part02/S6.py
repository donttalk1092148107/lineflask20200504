setA = {1, 6, 8, 10, 20}
setB = {1, 3, 8, 10}

#聯集
print('聯集',setA.union(setB))
print('聯集',setA | setB)

#交集
print('交集',setA.intersection(setB))
print('交集',setA & setB)

#差集
print('差集',setA.difference(setB))
print('差集',setA - setB)

#對稱差集
print('對稱差集',setA.symmetric_difference(setB))
print('對稱差集',setA ^ setB)