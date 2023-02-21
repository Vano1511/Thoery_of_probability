# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

from scipy.stats import norm

math_exp = 174
mu = 8
distr = norm(math_exp, mu)
higher_182 = round((1 - distr.cdf(182)) * 100, 4)
higher_190 = round((1 - distr.cdf(190)) * 100, 4)
between_166_190 = round((distr.cdf(190) - distr.cdf(166)) * 100, 4)
between_166_182 = round((distr.cdf(182) - distr.cdf(166)) * 100, 4)
between_158_190 = round((distr.cdf(190) - distr.cdf(158)) * 100, 4)
lower_150_higher_190 = round((distr.cdf(150) + 1 - distr.cdf(190)) * 100, 4)
lower_150_higher_198 = round((distr.cdf(150) + 1 - distr.cdf(198)) * 100, 4)   
lower_166 = round(distr.cdf(166) * 100, 4)
print(f"а). больше 182 см : {higher_182} %\nб). больше 190 см : {higher_190} %\nв). от 166 см до 190 см : {between_166_190} %"
      f"\nг). от 166 см до 182 см : {between_166_182} %\nд). от 158 см до 190 см : {between_158_190} %\n"
      f"е). не выше 150 см или не ниже 190 см : {lower_150_higher_190} %\n"
      f"ё). не выше 150 см или не ниже 198 см : {lower_150_higher_198} %\nж). ниже 166 см. : {lower_166} %")
