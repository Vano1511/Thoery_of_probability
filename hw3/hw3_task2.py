# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?


box1 = 8
white1 = 5
box2 = 12
white2 = 5
out1 = 2
out2 = 4
out_white = 3

from hw1.hw1_task3 import probability

prob3 = probability(box1, white1, 2, 1) * probability(box2, white2, 4, 2) + \
        probability(box1, white1, 2, 2) * probability(box2, white2, 4, 1) + \
        probability(box1, white1, 2, 0) * probability(box2, white2, 4, 3)

print(f'Вероятность того, что из вытянутых мячей ровно 3 белые равна {round(prob3 / 100, 3)}%')
