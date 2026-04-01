"""AI 生成，待測試與修改。"""

from typing import Iterable, List, Tuple

"""
Combinatorics template
- dynamic extend
- C(n,k), P(n,k), H(n,k) (multiset), multinomial, Catalan
- bigC(n,k): n can be huge, k small/medium (needs precompute up to k)

NOTE:
This template assumes MOD is prime for factorial-based inverses (uses pow(x, MOD-2, MOD)).
If MOD is not prime, inv_mod() (exgcd) can compute inverse when gcd(x, MOD)=1,
but factorial / binom under composite mod generally needs other techniques.
"""


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) s.t. a*x + b*y = g = gcd(a,b)"""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def inv_mod(a: int, mod: int) -> int:
    """mod inverse for general mod when gcd(a,mod)=1"""
    a %= mod
    g, x, _ = egcd(a, mod)
    if g != 1:
        raise ZeroDivisionError("inverse does not exist (gcd != 1)")
    return x % mod


class Comb:
    __slots__ = ("MOD", "n", "fact", "invfact", "inv")

    def __init__(self, n: int = 0, MOD: int = 998244353):
        self.MOD = MOD
        self.n = 0
        self.fact = [1]
        self.invfact = [1]
        self.inv = [0]  # inv[0] dummy
        if n > 0:
            self.init(n)

    def init(self, m: int) -> None:
        """ensure factorial tables up to m (inclusive)"""
        if m <= self.n:
            return
        MOD = self.MOD
        fact = self.fact
        invfact = self.invfact
        inv = self.inv

        old = self.n
        fact.extend([1] * (m - old))
        invfact.extend([1] * (m - old))
        inv.extend([0] * (m - old))

        for i in range(old + 1, m + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact[m] = pow(fact[m], MOD - 2, MOD)  # MOD prime
        for i in range(m, old, -1):
            invfact[i - 1] = invfact[i] * i % MOD
            inv[i] = invfact[i] * fact[i - 1] % MOD  # inv[i] for i>=1

        self.n = m

    # ----- basic getters -----
    def fac(self, m: int) -> int:
        if m > self.n:
            self.init(m)
        return self.fact[m]

    def ifac(self, m: int) -> int:
        if m > self.n:
            self.init(m)
        return self.invfact[m]

    def inv_int(self, x: int) -> int:
        if x <= 0:
            raise ZeroDivisionError("inv_int expects x >= 1")
        if x <= self.n:
            v = self.inv[x]
            if v != 0:
                return v
        return pow(x, self.MOD - 2, self.MOD)  # MOD prime

    # ----- combinatorics -----
    def C(self, n: int, k: int) -> int:
        if k < 0 or k > n:
            return 0
        if n > self.n:
            self.init(n)
        MOD = self.MOD
        return self.fact[n] * self.invfact[k] % MOD * self.invfact[n - k] % MOD

    def P(self, n: int, k: int) -> int:
        if k < 0 or k > n:
            return 0
        if n > self.n:
            self.init(n)
        return self.fact[n] * self.invfact[n - k] % self.MOD

    def H(self, n: int, k: int) -> int:
        """multiset: C(n+k-1, k) for n>=1; define H(0,0)=1 else 0"""
        if k < 0:
            return 0
        if n == 0:
            return 1 if k == 0 else 0
        return self.C(n + k - 1, k)

    def multinomial(self, ks: Iterable[int]) -> int:
        """given k1,k2,... sum to n: n! / prod(ki!)"""
        ks_list = list(ks)
        n = sum(ks_list)
        if n > self.n:
            self.init(n)
        MOD = self.MOD
        res = self.fact[n]
        for k in ks_list:
            if k < 0:
                return 0
            res = res * self.invfact[k] % MOD
        return res

    def catalan(self, n: int) -> int:
        """Cat(n) = C(2n, n)/(n+1)"""
        if n < 0:
            return 0
        if 2 * n > self.n:
            self.init(2 * n)
        MOD = self.MOD
        return self.C(2 * n, n) * pow(n + 1, MOD - 2, MOD) % MOD

    # ----- large n, small k -----
    def falling(self, n: int, k: int) -> int:
        """n*(n-1)*...*(n-k+1) mod MOD; works for huge n"""
        if k < 0:
            return 0
        MOD = self.MOD
        n %= MOD
        res = 1
        for i in range(k):
            res = res * (n - i) % MOD
        return res

    def bigC(self, n: int, k: int) -> int:
        """
        C(n,k) for huge n but k small/medium (needs precompute up to k).
        Complexity O(k). Uses symmetry k=min(k,n-k) only if n fits in int; for huge n still ok.
        """
        if k < 0:
            return 0
        if n < 0:
            return 0
        k = min(k, n - k) if n >= 0 else k
        if k < 0:
            return 0
        if k > self.n:
            self.init(k)
        MOD = self.MOD
        res = 1
        for i in range(1, k + 1):
            res = res * ((n - i + 1) % MOD) % MOD
        return res * self.invfact[k] % MOD


# --- usage example ---
comb = Comb()  # lazy
comb.init(2 * 10**6)  # if you know max needed
ans = comb.C(3, 1)
print(ans)
