# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?


from hw1_task3 import probability

total_billets = 100
win_billets = 2
buying_billets = 2
win_billets_buying = 2

print(f'Вероятность равна : {probability(total_billets, win_billets, buying_billets, win_billets_buying)}')