import sys

def main():
    import sys
    import threading

    def solve():
        import sys

        MOD = 10**9 + 7

        # 讀取所有輸入
        data = sys.stdin.read().split()
        ptr = 0
        n = int(data[ptr]); ptr +=1
        l = int(data[ptr]); ptr +=1
        k = int(data[ptr]); ptr +=1
        a = []
        for _ in range(n):
            a.append(int(data[ptr]))
            ptr +=1

        # 特殊情況處理: k ==1 時，每個位置都是一個子序列
        if k ==1:
            print(l % MOD)
            return

        # 將每個節中的位置按元素值從小到大排序
        st_range = sorted(range(n), key=lambda x: a[x])

        # 初始化 DP 陣列，大小為 n * k
        # dp[i * n + j] 代表在第 i 個節中第 j 個位置結尾的子序列數量
        dp = [0] * (n *k)

        ans =0

        for i in range(k):
            pt =0   # 指向前一個節中已經處理到的位置
            cur =0  # 當前累積的符合條件的子序列數量

            for j in st_range:
                idx = i *n +j

                if i ==0:
                    # 第一個節中，任何單一元素都是一個子序列
                    dp[idx] =1
                else:
                    # 將前一個節中所有小於等於當前元素的子序列數量累加
                    while pt <n and a[st_range[pt]] <= a[j]:
                        prev_idx = (i -1) *n + st_range[pt]
                        cur += dp[prev_idx]
                        if cur >= MOD:
                            cur -= MOD
                        pt +=1
                    dp[idx] = cur

                # 計算這個子序列在整個長度為 l 的序列中可以被平移多少次
                # 即計算從當前 idx 開始，每隔 n 個元素最多可以平移多少次不超過 l
                times = (l - idx -1) //n +1
                if times >0:
                    # 累加到最終答案中，注意取模
                    ans += (times % MOD) * (dp[idx] % MOD)
                    if ans >= MOD:
                        ans -= MOD

        print(ans % MOD)

    # 使用 threading 來避免 Python 的遞歸深度限制
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()
