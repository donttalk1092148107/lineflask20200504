def sum_scores(scores):
    sum = 0
    for n in scores:
        sum += n

    
    return sum

scores = [70, 80, 90, 95, 100]
sum = sum_scores(scores)

print('總分', sum)