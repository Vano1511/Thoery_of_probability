# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

from hw1_task3 import probability

total_buttons = 10
password_len = 3
pushing_buttons = 3
pass_but_push = 3

print(f'Вероятность равна : {probability(total_buttons,password_len, pushing_buttons, pass_but_push)}')