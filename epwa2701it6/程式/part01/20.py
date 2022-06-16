score = int(input("輸入學生成績："))

while score < 0 or score > 100:
    score = int(input("成績錯誤，請重新輸入："))