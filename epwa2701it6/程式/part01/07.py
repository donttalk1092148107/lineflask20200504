score=60

if 90 <= score <= 100:
    score_level = 'A'
elif 80 <= score <= 89:
    score_level = 'B'
elif 70 <= score <= 79:
    score_level = 'C'
elif 60 <= score <= 69:
    score_level = 'D'
else:
    score_level = 'E'
print(score_level)