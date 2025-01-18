"""
    集合枚舉 + 位運算(Bit Manipulation)
    看到 1 ≤ N ≤ 20，就知道這題是要用集合枚舉 + 位運算
    
    每筆測資的時間複雜度是 O(2^n) ，使用 Python 很有可能會 TLE 
    CPE 上能通過，但 UVA 上應該會 TLE 

    https://leetcode.cn/circle/discuss/CaOJ45/
"""
import sys
buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)
def print(val):
    sys.stdout.write(str(val) + '\n')

while True:
    # n, m = map(int, input().split())
    n, m = map(int, [cin(), cin()])
    if n == 0 and m == 0:
        break
    saya = [0] * n # saya[i] << j means i believe j
    sayb = [0] * n # sayb[i] << j means i unbelieve j
    for _ in range(m):
        # x, y = map(int, input().split())
        x, y = map(int, [cin(), cin()])
        if y > 0: # believe
            saya[x-1] |= 1 << (y-1)
        else: # unbelieve
            sayb[x-1] |= 1 << (-y-1)
    ans = 0
    for x in range(1 << n):
        if bin(x).count('1') <= ans: # pruning
            continue
        flag = True
        for i in range(n):
            if (x & (1 << i)): # j 在答案的集合中
                if (x & saya[i]) != saya[i] or (x & sayb[i]) != 0:
                    flag = False
                    break
        if flag:
            ans = max(ans, bin(x).count('1'))
    print(ans)