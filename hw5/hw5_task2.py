# Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100 шариков средний диаметр
# оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.

from scipy import stats
import numpy as np

alpha = 0.05
n = 100
var = 4
x_0 = 17
x_n = 17.5
limit = stats.norm.ppf(1 - alpha)
zet = (x_n - x_0) / np.sqrt(var / n)
if zet <= limit:
    print(f'The H_0 hypotesis accepted')
else:
    print(f'The H_1 hypotesys accepted')