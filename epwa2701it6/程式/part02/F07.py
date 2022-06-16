import scocheck_20 as sc
scores = [80, 95, 70, 40, 65, 55, 75, 50, 90]
print('最高分：', str(sc.highest(scores)))
print('最低分：', str(sc.lowest(scores)))
print('平均分數：', str(sc.average(scores)))
print('及格：', list(sc.get_pass_scores(scores)))
print('不及格：', list(sc.get_fail_scores(scores)))