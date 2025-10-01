import random
count_of_persons = abs(int(input('Введите количество участников олимпиады: ')))
scores = sorted([random.randrange(0, 100, 1) for i in range(count_of_persons)])
student_score = random.choice(scores)
print(f'У Стаса {student_score} балла(ов)')
def check_winners(scores, student_score):
    sort_scores = [i for i in scores[-3:]]
    print(sort_scores)
check_winners(scores, student_score)


