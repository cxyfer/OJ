"""
E. 立希的扫雷构造
https://ac.nowcoder.com/acm/contest/120564/E
AI-Generated Code
"""
import sys

# 增加遞迴深度以防萬一，雖然此解法主要是迭代
sys.setrecursionlimit(2000)

def solve():
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    # 全域緩存：儲存 (n, m) 的計算結果
    # memo_ans[n][m][k] = 最大危險值
    # memo_path[n][m] = 重建路徑所需的轉移表
    # memo_last_state[n][m][k] = 達成最大值時的最後一個 mask 狀態
    memo_ans = {}
    memo_trans = {}
    memo_end_mask = {}

    results = []

    for _ in range(num_test_cases):
        n = int(next(iterator))
        m = int(next(iterator))
        k = int(next(iterator))

        # 為了減少狀態空間（2^(m+1)），確保 m 是較小的一邊
        swapped = False
        if n < m:
            n, m = m, n
            swapped = True

        key = (n, m)
        if key not in memo_ans:
            # 初始化
            length = n * m
            mask_len = m + 1
            mask_size = 1 << mask_len
            total_sz = mask_size * (length + 1)
            
            # 使用一維陣列來存 dp，效率更高
            # dp[s * (length + 1) + j]
            # s: mask, j: 放置的地雷數
            
            # dp 陣列初始化為 -1
            dp = [-1] * total_sz
            dp[0] = 0  # 初始狀態：mask=0, 放置 0 個雷，危險值 0
            
            # 轉移記錄：用來重建路徑
            # mtr[p * total_sz + current_mask * (len+1) + k] = (last_mask_bit << 1) | current_v
            # 這裡我們只存 (drop << 1) | v，其中 drop 是被移出的最舊位元
            # 但更簡單的方式是存上一個狀態的完整 index，不過空間太大。
            # C++ 程式碼中存的是 drop 和 v，足以反推。
            mtr = bytearray(length * total_sz) # 用 bytearray 節省記憶體，因為 v 和 drop 只需要 2 bits
            
            # 迭代每一個位置 p (0 ~ nm-1)
            for p in range(length):
                r, c = divmod(p, m)
                
                new_dp = [-1] * total_sz
                
                # 預先計算鄰居位置的存在性
                has_left = c > 0
                has_top_left = r > 0 and c > 0
                has_top = r > 0
                has_top_right = r > 0 and c < m - 1
                
                # 位元索引 (Bit index in mask S)
                # left_bit = 0 (p-1)
                # tl_bit = m (p-m-1)
                # top_bit = m-1 (p-m)
                # tr_bit = m-2 (p-m+1)
                
                # 遍歷舊狀態 mask (s)
                for s in range(mask_size):
                    # 遍歷已放置的地雷數 j (0 ~ p)
                    start_idx = s * (length + 1)
                    # 優化：只處理有值的 j
                    # 這裡可以進一步優化，如果 dp[start_idx + j] == -1 就跳過
                    # 但 Python 中迭代所有 j 會比每次判斷快一點點，除非稀疏
                    
                    for j in range(p + 1):
                        current_val = dp[start_idx + j]
                        if current_val == -1:
                            continue
                        
                        # 嘗試放空地 (v=0) 或地雷 (v=1)
                        for v in range(2):
                            nj = j + v
                            
                            # 計算新增的危險值
                            add = 0
                            if has_left:
                                add += ((s >> 0) & 1) ^ v
                            if has_top_left:
                                add += ((s >> m) & 1) ^ v
                            if has_top:
                                add += ((s >> (m - 1)) & 1) ^ v
                            if has_top_right:
                                add += ((s >> (m - 2)) & 1) ^ v
                                
                            val = current_val + add
                            
                            # 更新 mask: ((s << 1) & (mask_size - 1)) | v
                            # 為了回溯，我們需要知道最舊的那一位 (s >> m) & 1
                            ns = ((s << 1) & (mask_size - 1)) | v
                            n_idx = ns * (length + 1) + nj
                            
                            if val > new_dp[n_idx]:
                                new_dp[n_idx] = val
                                # 記錄選擇，用於回溯
                                # drop 是被擠出去的那一位 (最舊的位元，對應 p-m-1)
                                drop = (s >> m) & 1
                                # 存入 (drop << 1) | v
                                mtr_idx = p * total_sz + n_idx
                                mtr[mtr_idx] = (drop << 1) | v
                
                dp = new_dp

            # 保存結果到緩存
            ans_k = [-1] * (length + 1)
            end_mask_k = [-1] * (length + 1)
            
            for s in range(mask_size):
                for j in range(length + 1):
                    idx = s * (length + 1) + j
                    if dp[idx] > ans_k[j]:
                        ans_k[j] = dp[idx]
                        end_mask_k[j] = s
            
            memo_ans[key] = ans_k
            memo_trans[key] = mtr
            memo_end_mask[key] = end_mask_k

        # 輸出答案
        max_val = memo_ans[key][k]
        results.append(str(max_val))
        
        # 重建路徑
        # 從最後一個狀態往回推
        grid = [['.' for _ in range(m)] for _ in range(n)]
        
        curr_mask = memo_end_mask[key][k]
        curr_k = k
        length = n * m
        mask_len = m + 1
        mask_size = 1 << mask_len
        total_sz = mask_size * (length + 1)
        mtr = memo_trans[key]
        
        for p in range(length - 1, -1, -1):
            idx = p * total_sz + curr_mask * (length + 1) + curr_k
            info = mtr[idx]
            
            v = info & 1
            drop = (info >> 1) & 1
            
            r, c = divmod(p, m)
            if v == 1:
                grid[r][c] = '*'
            
            # 反推上一個 mask
            # current_mask = ((prev_mask << 1) & mask_lim) | v
            # 所以 prev_mask = (current_mask >> 1) | (drop << m)
            curr_mask = (curr_mask >> 1) | (drop << m)
            curr_k -= v
            
        # 處理旋轉
        if swapped:
            # 如果之前交換了 n, m，現在需要把 grid 轉回來
            new_grid = [['' for _ in range(n)] for _ in range(m)]
            for r in range(n):
                for c in range(m):
                    new_grid[c][r] = grid[r][c]
            grid = new_grid
            n, m = m, n  # 恢復原始尺寸以供輸出
            
        for row in grid:
            results.append("".join(row))

    print("\n".join(results))

if __name__ == "__main__":
    solve()