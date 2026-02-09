"""
C. 墨提斯的排列
https://ac.nowcoder.com/acm/contest/120564/C

貪心 / Gray Code

逐位考慮，令最高位為 d ，則第 d 位一定會在「至少一個」相鄰位置。
為最小化相鄰的異或值，因此應該將第 d 位為 0 的部分和第 d 位為 1 的部分分開成前後兩部分。
且為了確保兩部分之間只有第 d 位不同，因此除了第 d 位之外，後半部分應該是前半部分的鏡像。
之後便是遞迴子問題，而這正是 Gray Code 的一種構造方式。
"""
def solve():
    n = int(input())

    ans = [0]
    for i in range(n):
        ans += [x | (1 << i) for x in reversed(ans)]
    print(*ans)

if __name__ == "__main__":
    solve()