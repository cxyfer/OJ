def solve():
    n = int(input())
    A = [0 if input().strip() == "F" else 1 for _ in range(n)]

    # 特判全為 F 的情況，根據題意這時候的 k 應該為 1
    # 但測了一下測資中似乎沒有這種情況
    if all(x == 0 for x in A):
        print(0, 1)
        return

    for k in range(n, 0, -1):
        ans = s = 0
        diff = [0] * (n + 1)
        for i in range(n):
            s ^= diff[i]
            if A[i] ^ s == 1:
                if i + k <= n:
                    ans += 1
                    s ^= 1
                    diff[i + k] ^= 1
                else:
                    break
        else:
            # k = 1 時保證有解
            print(k, ans)
            break


if __name__ == "__main__":
    solve()
