from sage.all import *

def rabin_test(f, R, x):
    q = R.base_ring().order()
    n = f.degree()
    prime_divisors = [p for p,e in factor(n)]

    for p in prime_divisors:
        ni = n // p
        h = x**(q**ni) % f
        g = f.gcd(h)
        if g.degree() > 0:
            return False
        
    g = x**(q**n) % f - x
    if g == 0:
        return True
    else:
        return False

F = GF(5) # Field
ring = PolynomialRing(F, 'x') # Polynomial Ring over F
x = ring.gen()
f = x**2 + 1
print(rabin_test(f, ring, x))
