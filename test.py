import decimal
import cmath

omega = (1 + cmath.sqrt(5)) / 2

n = int(input("n:"))

def General(k):

    if k == 1:
        return round(omega, 3)
    if k % 2 == 1:
        base = round(General((k - 1) / 2), 3)
        return round(base * base * omega, 3)
    base = round(General(k / 2), 3)
    return round(base * base, 3)

print(General(n))