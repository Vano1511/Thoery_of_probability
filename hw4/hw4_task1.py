# Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.

import formulas_normal_distribution as fnd

start = 200
finish = 800
math_exp = fnd.math_expectation(start, finish)
var = fnd.var(start, finish)
print(f"матожидание равно : {math_exp}, \nдисперсия равна : {var}")