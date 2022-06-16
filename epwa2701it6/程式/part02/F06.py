#filter(判断函数, 迭代對象)

def is_odd(n):
    return n%2==1
 
tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)


scores = [90, 50, 80, 40, 100]
f = lambda x: x if x < 60 else False
fail_scores = filter(f, scores) 

for item in fail_scores:
    print(item)


