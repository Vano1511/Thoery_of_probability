# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial as f

all_details = 15
coloured_details = 9
quantity_out = 3
coloured_out = 3

def probability(all_in, all_factored, all_out, factor_out):
    """Функция высчитывает вероятность того, что из общего количества(all_in), где имеется несколько определенных
    с одним параметром(all_factored) выбирается несколько(all_out), из которых должно быть с параметром(factor_out)"""
    non_factored = all_in - all_factored
    numerator = (f(all_factored) / (f(factor_out) * f(all_factored - factor_out))) * \
                (f(non_factored) / (f(all_out - factor_out) * f(non_factored - all_out + factor_out)))
    denominator = f(all_in) / (f(all_out) * f(all_in - all_out))
    return round((numerator / denominator) * 100, 3)


if __name__ == '__main__':
    print(f'{probability(all_details, coloured_details, quantity_out, coloured_out)}%')
