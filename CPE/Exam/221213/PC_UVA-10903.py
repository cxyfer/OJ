"""
    比對整個字串可能會有問題，可能有 \n 或其他空白字元，所以只比對第一個字元或是在比對前先 strip
"""
import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val)+"\n")
kase = 1
while True:
    line = input().strip() # remove \n
    if line[0] == "0": # 比對整個字串可能會有問題，可能有 \n 或其他空白字元，所以只比對第一個字元或是在比對前先 strip
        break
    n, k = map(int, line.split())
    cnt = [[0, 0] for _ in range(n)] # W/L
    for _ in range(k*n*(n-1)//2):
        p1, m1, p2, m2 = input().split()
        p1, p2 = int(p1)-1, int(p2)-1
        if (m1 == "rock" and m2 == "scissors") or (m1 == "scissors" and m2 == "paper") or (m1 == "paper" and m2 == "rock"):
            cnt[p1][0] += 1
            cnt[p2][1] += 1
        elif (m2 == "rock" and m1 == "scissors") or (m2 == "scissors" and m1 == "paper") or (m2 == "paper" and m1 == "rock"):
            cnt[p2][0] += 1
            cnt[p1][1] += 1
    if kase > 1:
        print()
    kase += 1
    for i in range(n):
        w, l = cnt[i]
        if w + l == 0:
            print("-")
        else:
            print(f"{w/(w+l):.3f}")