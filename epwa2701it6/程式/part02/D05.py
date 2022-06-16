thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a=thisdict.items()
print(a)
print(type(a))

for x in thisdict.items():
  print(x)
print(type(x))


for x, y in thisdict.items():
  print(x, y)
print(type(x))