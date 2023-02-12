from math import factorial as f

def bernuli(n, k, p):
    c = f(n) / (f(k) * f(n - k))
    return c * pow(p, k) * pow(1 - p, n - k)

def puasson(n, k, p):
    lam_da = n * p
    return (pow(lam_da, k) * pow(2.72, (-1 * lam_da))) / f(k)



