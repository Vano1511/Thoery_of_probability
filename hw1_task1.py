# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from hw1_task3 import probability

all_cards = 52
clubs_cards = 13
aces_cards = 4
all_out_cards = 4
clubs_out_cards = 4
aces_out_cards = 1

print(f'вероятность а равна {probability(all_cards, clubs_cards, all_out_cards, clubs_out_cards)}')
probability_b = 0
for quantity_of_aces in range(1, 5):
    probability_b += float(probability(all_cards, aces_cards, all_out_cards, quantity_of_aces)[:-1])
print(f'вероятность b равна {probability_b}%')
