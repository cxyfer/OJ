"""
G. 智乃的箭头魔术
https://ac.nowcoder.com/acm/contest/120565/G

簽到
將圖視為一個 [-1, 1] x [-1, 1] 的座標系，維護箭頭的位置 (x, y)，按照題意模擬即可。
"""
def solve():
    s = "0112233445142015320125410214530214510214102302142025101203201451451522302514203214510021454101002532"
    
    ans = []
    x, y = 1, 1
    for op in map(int, s):
        if op == 0:
            x = -x
        elif op == 1:
            x, y = y, x
        elif op == 2:
            y = -y
        elif op == 3:
            x, y = -y, -x
        elif op == 4:
            x, y = y, -x
        else:
            x, y = -y, x

        if x == 1 and y == 1:
            ans.append(0)
        elif x == 1 and y == -1:
            ans.append(1)
        elif x == -1 and y == -1:
            ans.append(2)
        else:
            ans.append(3)

    print(*ans, sep='')

if __name__ == "__main__":
    solve()