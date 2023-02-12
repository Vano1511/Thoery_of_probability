# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?

from hw1.hw1_task3 import probability

colors = ('white', 'no white')
box1 = 10
white1 = 7
box2 = 11
white2 = 9
prob_all = probability(box1, white1, 2, 2) * probability(box2, white2, 2, 2)
print(f'вероятность того, что все мячи белые: {round(prob_all / 100, 3)}% ')
prob_2 = probability(box1,white1, 2, 1) * probability(box2, white2, 2, 1) + \
         probability(box1,white1, 2, 2) * probability(box2, white2, 2, 0) + \
         probability(box1,white1, 2, 0) * probability(box2, white2, 2, 2)
print(f'вероятность того, что ровно два мяча белые: {round(prob_2 / 100, 3)}% ')
prob_0 = probability(box1,white1, 2, 0) * probability(box2, white2, 2, 0) # вероятность того, что ни один не белый
print(f'вероятность того, что хотя бы один мяч белый: {round(100 - (prob_0 / 100), 3)}% ')
