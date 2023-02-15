from math import factorial as f

def bernuli(n, k, p):
    c = f(n) / (f(k) * f(n - k))
    return c * pow(p, k) * pow(1 - p, n - k)

def puasson(n, k, p):
    lam_da = n * p
    return (pow(lam_da, k) * pow(2.72, (-1 * lam_da))) / f(k)


def baies(p_AB, p_A, p_B):
    return p_AB * p_B / p_A

def var(array, ddof = 0):
    avg = sum(array) / len(array)
    return sum(pow(el - avg, 2) for el in array) / (len(array) - ddof)

# print(round(bernuli(50, 0, 0.004) * 100, 2))
