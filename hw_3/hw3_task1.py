# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

from hw2.formulas import var
array = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
avg = sum(array) / len(array)
var_0 = var(array)
var_1 = var(array, ddof=1)
std_0 = pow(var_0, 0.5)
std_1 = pow(var_1, 0.5)


print(f'математическое ожидание : {avg} \n'
      f'смещенная дисперсия : {var_0} \n'
      f'смещенное сренеквадратическое отклонение : {std_0} \n'
      f'несмещенная дисперсия : {var_1} \n'
      f'несмещенное сренеквадратическое отклонение : {std_1}')