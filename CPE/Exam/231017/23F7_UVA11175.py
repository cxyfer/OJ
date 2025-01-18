""" 
    tags: AOAPC-BAC-Ch8
    Python 都會 TLE
    
    對圖E中的點對 (i, j)
    若存在一個點 k1，使得 i 和 j 都能到達 k1，
    但是又同時存在一個點 k2，使得 i 和 j 只有其中一個能到達 k2，
    則 (i, j) 是一個不可逆的點對。
     
    https://blog.csdn.net/Inuyasha__/article/details/103384599
    https://home.gamer.com.tw/creationDetail.php?sn=3800895
    Line Graph:
    https://web.ntnu.edu.tw/~algo/Graph2.html
"""
import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val)+"\n")

T = int(input())

for kase in range(1, T+1):
    m = int(input())
    k = int(input())

    g = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(k):
        u, v = map(int, input().split())
        g[u][v] = 1
    
    flag = False
    for i in range(m):
        for j in range(m):
            ck1 = ck2 = False
            for k in range(m):
                if g[i][k] and g[j][k]: # i 和 j 都能到達 k
                    ck1 = True
                if g[i][k] != g[j][k]: # i 和 j 只有其中一個能到達 k
                    ck2 = True
            if ck1 and ck2:
                flag = True
                break
        if flag:
            break
    print("Case #%d: %s" % (kase, "No" if flag else "Yes"))