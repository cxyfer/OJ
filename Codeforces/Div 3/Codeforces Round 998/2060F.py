import sys
input_data = sys.stdin.read().strip().split()
t = int(input_data[0])

MOD = 998244353
MAX_K = 10**5  # k 的最大值

########################################################
# (1) 最小質因數 (smallest prime factor) 篩法 (spf_sieve)
#
#   用來為每個 1..MAX_K 預先計算出其最小質因數 spf[x]，
#   之後可在 O(log x) 時間內做質因數分解。
########################################################

def spf_sieve(n):
    """ 建立長度為 n+1 的 spf (最小質因數) 陣列 """
    spf = [0] * (n+1)
    spf[1] = 1
    for i in range(2, n+1):
        if spf[i] == 0:
            # i 為質數 (prime)
            spf[i] = i
            # 對 i 的倍數做篩，填入最小質因數
            for j in range(i*i, n+1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf

# 建立 SPF 表
spf = spf_sieve(MAX_K)

########################################################
# (2) 質因數分解 (factorize)
#
#   利用 spf[x]，可以在 O(log x) 內分解 x。
#   回傳結果為一個 dict: prime -> exponent
########################################################

def factorize(x):
    """ 回傳 x 的質因數分解，形式為 {p1: a1, p2: a2, ...} """
    factors = {}
    while x > 1:
        p = spf[x]
        factors[p] = factors.get(p, 0) + 1
        x //= p
    return factors

########################################################
# (3) 多項式相關的預處理: 
#     (a) 小階層 (factorial) 及其逆元
#     (b) 建立 binomial 相關多項式
#
#   在展開 G_m(x) = ∏ binom(α_i + m - 1, m - 1) 時，
#   單項 binom(a+m-1, m-1) 可視為 (∏_{j=0}^{a-1}(m+j)) / a!
#   這會是一個 "m 的 a 次多項式"。其係數需要用到 a! 及反元素。
########################################################

# 為了安全，這邊我們只需要到 factorial 最高大約 20 即足以覆蓋 α_i <= 16
MAX_FACT = 20  
fact = [1]*(MAX_FACT+1)
invfact = [1]*(MAX_FACT+1)

# 建立 factorial 與逆元 factorial
for i in range(1, MAX_FACT+1):
    fact[i] = (fact[i-1]*i) % MOD

# 費馬小定理求逆元: inv(a) = a^(MOD-2) mod MOD (MOD 為質數)
def modinv(a, m=MOD):
    return pow(a, m-2, m)

invfact[MAX_FACT] = modinv(fact[MAX_FACT], MOD)
for i in reversed(range(MAX_FACT)):
    invfact[i] = (invfact[i+1]*(i+1)) % MOD

def poly_binom(a):
    """
    回傳多項式 poly[], 使得 poly(m) = binom(a+m-1, m-1)，
    也就是 ( (m)*(m+1)*...*(m+a-1 ) ) / a! 的展開。
    回傳形式: poly[0], poly[1], ..., poly[a] (長度 a+1)
    """
    # 若 a=0，binom(m-1,m-1)=1，對應於常數多項式 1
    if a == 0:
        return [1]
    
    # P(m) = (m)(m+1)...(m+a-1) = ∏_{j=0 to a-1} (m + j)
    # 先把這個做成展開的多項式:
    #   (m+0)*(m+1)*...*(m+a-1)
    #   這是 a 次多項式。
    # 然後最後除以 a! (對應到乘上 invfact[a])
    res = [1]  # 開始是一個常數多項式
    for j in range(a):
        # 將 res 與 (m + j) 做多項式乘法
        new_poly = [0]*(len(res)+1)
        for p in range(len(res)):
            # (res[p] * m^p) * (m + j) = res[p]*m^(p+1) + j*res[p]*m^p
            new_poly[p]   = (new_poly[p] + res[p]*j) % MOD
            new_poly[p+1] = (new_poly[p+1] + res[p]) % MOD
        res = new_poly
    
    # 乘上 invfact[a]
    inv_a_fact = invfact[a]
    for i in range(len(res)):
        res[i] = (res[i]*inv_a_fact) % MOD
    return res

def poly_mul(poly1, poly2):
    """
    多項式相乘 (polynomial multiplication):
      回傳 poly1(x)*poly2(x) 的係數陣列
    """
    deg1 = len(poly1)
    deg2 = len(poly2)
    res = [0]*(deg1+deg2-1)
    for i in range(deg1):
        for j in range(deg2):
            res[i+j] = (res[i+j] + poly1[i]*poly2[j]) % MOD
    return res

########################################################
# (4) 計算 ∑_{m=1 to n} m^p mod M 的函式:
#
#   為了針對 p<=16 做快速求和，可使用 "多項式插值 (Lagrange interpolation)"
#   或 "Faulhaber's formula + Bernoulli numbers" 等方法。
#
#   以下示範一種「事先對 f(n)=n^p 做前 p+2 個點，
#   然後對 g(n)=∑_{m=0..n} m^p 用 Lagrange 多項式的方式建表」來完成。
#
#   注意若要確保計算效率，我們要在一開始就對所有 p=0..16 建好插值所需內容，
#   之後對每個 test case, 只要 O(p) = O(16) 即可取得 sum_{m=0..n} m^p。
########################################################

MAX_P = 16  # 我們最多只需要到 p=16
# 建立一個 cache，用來存放 sum_{m=0..n} m^p 的 Lagrange 多項式參數
# 我們將會在 0..p+1 的範圍內 (共 p+2 個整數點) 做取樣。
# 之後用 eval_sum_of_powers(n,p) 來快速算出 sum_{m=0..n} m^p
lagrange_info = [None]*(MAX_P+1)

def precompute_sum_of_powers():
    """
    建立針對每個 p=0..MAX_P 的 Lagrange interpolation 資料。
    g_p(n) = sum_{m=0..n} m^p
    我們取點 n=0,1,2,...,p+1
    => g_p(0), g_p(1), ..., g_p(p+1)
    然後用這些點做多項式插值 (degree p+1)。
    """
    for p in range(MAX_P+1):
        # 收集插值所需點 (x_i, y_i):
        # x_i = i,  y_i = ∑_{m=0..i} m^p
        #      = 0^p + 1^p + ... + i^p
        pts_x = []
        pts_y = []
        ssum = 0
        for i in range(p+2):
            pts_x.append(i)
            ssum = (ssum + pow(i, p, MOD)) % MOD
            pts_y.append(ssum)
        
        # 接下來建 Lagrange 多項式所需的「逆元乘積」
        # L(x) = sum_{i=0..p+1} y_i * l_i(x)
        # l_i(x) = Π_{j!=i} ( x - x_j ) / ( x_i - x_j )
        # 為了快速評估，我們預先把 (x - x_j) / (x_i - x_j) 的分母準備好。
        # 這裡我們只需記錄 "每個 i 的分母的乘積" 與 "pts_x"、"pts_y"。
        
        # 分母: denom[i] = ∏_{j!=i} (x_i - x_j)
        # 之後評估時, l_i(N) = product_{j!=i}(N - x_j)*inv(denom[i])
        # => 會在 O(p) 內完成。
        denom = [1]*(p+2)
        for i in range(p+2):
            d = 1
            xi = pts_x[i]
            for j in range(p+2):
                if j != i:
                    xj = pts_x[j]
                    d = (d * (xi - xj)) % MOD
            denom[i] = modinv(d, MOD)
        
        lagrange_info[p] = (pts_x, pts_y, denom)

def eval_sum_of_powers(n, p):
    """ 回傳 sum_{m=0..n} m^p mod MOD。使用 Lagrange interpolation。 """
    if n <= p+1:
        # 直接算
        ssum = 0
        for m in range(n+1):
            ssum = (ssum + pow(m, p, MOD)) % MOD
        return ssum
    
    pts_x, pts_y, denom = lagrange_info[p]
    # 需要計算 L(n) = ∑ y_i * l_i(n)
    # l_i(n) = ∏_{j!=i} (n - x_j) * inv( (x_i - x_j) )
    # 但我們已經把分母準備在 denom[i] 裡。
    # => l_i(n) = denom[i] * ∏_{j!=i} (n - x_j)
    #   我們把 ∏_{j=0..p+1} (n - x_j) 先算好, 再除以 (n - x_i)。
    
    # prod = ∏_{j=0..p+1} (n - x_j)
    #      = ∏_{j=0..p+1} (n - j)
    # 但是 j 只到 p+1 => 這可以直接算
    # 之後 l_i(n) = prod/(n - x_i) * denom[i] (mod)
    
    # 先算 prod = (n - 0)*(n - 1)*...*(n - (p+1))
    prod = 1
    for j in range(p+2):
        prod = (prod * (n - pts_x[j])) % MOD
    
    total = 0
    for i in range(p+2):
        xi = pts_x[i]
        yi = pts_y[i]
        # term = yi * denom[i] * (prod * inv(n - xi)) mod
        #      = yi * denom[i] * prod * inv(n-xi)
        
        num = prod
        # (n - xi) 可能為 0 mod => 不過這情況不會發生，因為 n>p+1>= xi。
        inv_ = modinv(n - xi, MOD)
        term = (yi * denom[i]) % MOD
        term = (term * num) % MOD
        term = (term * inv_) % MOD
        
        total = (total + term) % MOD
    
    return total

# 建立插值表
precompute_sum_of_powers()

def sum_m_p(n, p):
    """ 回傳 ∑_{m=1..n} m^p mod MOD """
    # 我們上面定義的是從 m=0..n，所以要減去 m=0^p=0^p
    # 不過 0^p = 0 (當 p>0), 若 p=0, 0^0 依情況定義為1，但 sum_{m=1..n} m^0 = n
    if p == 0:
        # ∑_{m=1..n} 1 = n
        return n % MOD
    return eval_sum_of_powers(n, p)

########################################################
# (5) 封裝函式: compute_arrays_count(x, n)
#
#   回傳 ∑_{m=1..n} G_m(x) (mod MOD)，其中 G_m(x) = 乘積 binom(α_i + m - 1, m - 1)。
#   步驟:
#     - factorize x 得到各質因數次方 α_i
#     - 把每個 poly_binom(α_i) 做多項式相乘 => 得到 P_x(m)
#     - 計算 sum_{m=1..n} P_x(m)
#        => 若 P_x(m) = ∑ c_p m^p, 則 sum_{m=1..n} P_x(m) = ∑ c_p * (∑ m^p)
#     - 取 mod
########################################################

def compute_arrays_count(x, n):
    """
    回傳 x 的答案: 對所有 1 <= m <= n 的陣列長度 m，乘積為 x 的陣列數量之和 (mod)
    """
    if x == 1:
        # 只有全部為 1 的陣列才乘積=1
        # 長度可以是 1..n，共 n 種
        return n % MOD
    
    # 質因數分解
    fdict = factorize(x)  # {p1: a1, p2: a2, ...}
    # 建立多項式 P_x(m) = ∏_{i} binom(a_i + m - 1, m - 1)
    # => poly = poly_binom(a1) * poly_binom(a2) * ...
    poly = [1]  # 常數 1，多項式
    for prime, a in fdict.items():
        # 用多項式乘法合併
        binom_poly = poly_binom(a)
        poly = poly_mul(poly, binom_poly)
    
    # 現在 poly[i] = c_i，對應 m^i
    # => G_m(x) = poly[0] + poly[1]*m + ... + poly[A]*m^A
    # => sum_{m=1..n} G_m(x) = sum_{i=0..A} [poly[i] * sum_{m=1..n} m^i]
    ans = 0
    for i, c in enumerate(poly):
        if c != 0:
            ans = (ans + c*sum_m_p(n, i)) % MOD
    return ans

########################################################
# (6) 處理輸入 (input) 與輸出 (output)
########################################################

idx = 1
out = []
for _testcase in range(t):
    k_ = int(input_data[idx]); idx+=1
    n_ = int(input_data[idx]); idx+=1
    
    # 對 x=1..k_，計算答案並輸出
    # 由於題目要在同一行輸出 k 個空白分隔的答案
    result_line = []
    for x_ in range(1, k_+1):
        result_line.append(str(compute_arrays_count(x_, n_)))
    
    out.append(" ".join(result_line))

print("\n".join(out))
