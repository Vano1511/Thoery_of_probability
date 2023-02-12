# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from formulas import bernuli

n = 144
k = 70
p = 0.5

print(f'вероятность того, что из {n} подбрасываний орел выпадет ровно {k} раз равна : {round(bernuli(n, k, p)*100, 2)}%')