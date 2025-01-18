N, M = map(int, input().split())
# S = input()
# 存全部字串再修改會TLE，直接用一個Array存每個字元是否為?
s = [ch == "?" for ch in input()]
MOD = 998244353
 
output = []
ans = 1
for j in range(1, N-1):
    if (s[j]):
        ans = ans * j % MOD
# print(ans if not s[0] else 0)
output.append(ans if not s[0] else 0)
 
 
for _ in range(M):
    i, ch = input().split()
    i = int(i) - 1
    flag = ch == "?"
 
    # 這個字元發生從 <>到? 或從 ?到<> 的改變
    if i > 0 and s[i] != flag: 

        if (flag): # ans *= i
            ans = ans * i % MOD
        else: # ans /= i
            # ans = (ans / i) % MOD
            """
                對於 m = (a / b) % MOD 的問題，因為除法不能用同餘定理，我們需要將除法轉換成乘法
                (a / b) % MOD = (a * inv(b, MOD)) % MOD = (a % MOD * inv(b, MOD) % MOD) % MOD
                而 inv(b, MOD) = b ^ (MOD - 2) % MOD ， 證明如下：
                b * inv(b, MOD) = 1 % MOD
                b * inv(b, MOD) = b ^ (MOD - 1) % MOD (費馬小定理)
                inv(b, MOD) = b ^ (MOD - 2) % MOD ，得證
            """
            ans = ( ans * pow(i, MOD-2, MOD) ) % MOD
    s[i] = flag
 
    # print(ans if not s[0] else 0)
    output.append(ans if not s[0] else 0)
print('\n'.join(map(str, output)))