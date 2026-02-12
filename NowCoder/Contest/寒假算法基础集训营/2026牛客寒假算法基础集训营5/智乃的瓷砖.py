"""
B. 智乃的瓷砖
https://ac.nowcoder.com/acm/contest/120565/B
簽到，按題意模擬即可
"""
def solve():
    n, m = map(int, input().split())

    for i in range(n):
        if i & 1 == 0:
            row = ["/\\"] * (m // 2)
            if m & 1:
                row.append("/")
        else:
            row = ["\\/"] * (m // 2)
            if m & 1:
                row.append("\\")
        print(*row, sep="")

if __name__ == "__main__":
    solve()