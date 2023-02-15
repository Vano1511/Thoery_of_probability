# В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов
# поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9.
# Студент сдал первую сессию. Какова вероятность, что он учится:
# a). на факультете A
# б). на факультете B
# в). на факультете C

from hw2.formulas import baies
faculties = ('A', 'B', 'C')
share_of_faculties = [0.25, 0.25, 0.5]
exam_pas_probability = [0.8, 0.7, 0.9]
p_A = sum([share_of_faculties[i] * exam_pas_probability[i] for i in range(len(faculties))])
for i, faculty in enumerate(faculties):
    print(f'вероятность того, что сдавший экзамен учится на факультете {faculty} равна: '
          f'{round(baies(exam_pas_probability[i], p_A, share_of_faculties[i]) * 100, 3)}%')

