"""
J. 立希坐地铁
https://ac.nowcoder.com/acm/contest/120564/J
AI-Generated Code
"""
import sys
import heapq

# 增加遞歸深度與讀取緩衝區大小（針對大規模數據）
sys.setrecursionlimit(200005)

def solve():
    # 讀取所有輸入數據
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    def read():
        return int(next(iterator))
    
    def read_str():
        return next(iterator)

    try:
        n = read()
        m = read()
        sx, sy = read(), read()
        ex, ey = read(), read()
        
        # 存儲所有關鍵點：起點、終點、換乘站
        # p[0] 是起點, p[1] 是終點, p[2...] 是換乘站
        p = []
        p.append((sx, sy))
        p.append((ex, ey))
        for _ in range(m):
            p.append((read(), read()))
            
    except StopIteration:
        return

    num_points = m + 2
    # 每個點拆成 7 個節點:
    # 0: Hub (站廳)
    # 1: E (東), 2: W (西)
    # 3: S (南), 4: N (北)
    # 5: C (順時針), 6: I (逆時針)
    # 總節點編號: point_idx * 7 + state
    adj = [[] for _ in range(num_points * 7)]

    # 輔助數組用於排序建圖
    # by_row[x] 存儲 (y, original_idx)
    by_row = {} 
    # by_col[y] 存儲 (x, original_idx)
    by_col = {}
    # by_ring[k] 存儲 (pos_on_ring, original_idx)
    by_ring = {}

    # 計算環狀線上的相對位置函數
    def get_ring_pos(x, y, n_full):
        # 計算層數 k (1-based)
        k = min(x, n_full - x + 1, min(y, n_full - y + 1))
        
        # 當前層的邊長
        # 第 1 層邊長 n, 第 2 層邊長 n-2, ...
        # current_n = n_full - 2*(k-1)
        current_n = n_full - 2 * k + 2
        
        # 相對該層左上角 (k, k) 的坐標
        rx = x - k
        ry = y - k
        
        # 展開成一維坐標 (0 到 4*(current_n-1) - 1)
        # 上邊 (x = 0, y 增加)
        if rx == 0:
            return k, ry
        # 右邊 (y = current_n - 1, x 增加)
        elif ry == current_n - 1:
            return k, (current_n - 1) + rx
        # 下邊 (x = current_n - 1, y 減少)
        elif rx == current_n - 1:
            return k, 2 * (current_n - 1) + (current_n - 1 - ry)
        # 左邊 (y = 0, x 減少)
        else:
            return k, 3 * (current_n - 1) + (current_n - 1 - rx)

    # 1. 初始化點與內部邊 (Hub <-> Lines)
    for i in range(num_points):
        px, py = p[i]
        
        # 歸類到行、列、環
        if px not in by_row: by_row[px] = []
        by_row[px].append((py, i))
        
        if py not in by_col: by_col[py] = []
        by_col[py].append((px, i))
        
        k, pos = get_ring_pos(px, py, n)
        if k not in by_ring: by_ring[k] = []
        by_ring[k].append((pos, i))
        
        # Hub (0) 到 各線路 (1~6) 的邊
        # 根據題目邏輯：進入線路算 1 代價，離開線路算 0 代價
        # 這樣 A->Hub->B 的代價是 0(離開A) + 1(進入B) = 1 (換乘費)
        hub = i * 7
        for state in range(1, 7):
            node = hub + state
            adj[hub].append((node, 1)) # Enter line: cost 1
            adj[node].append((hub, 0)) # Exit line: cost 0

    # 2. 構建水平方向的邊 (E: 1, W: 2)
    for r in by_row:
        line = sorted(by_row[r]) # 按 y 排序
        for j in range(len(line) - 1):
            y1, id1 = line[j]
            y2, id2 = line[j+1]
            dist = (y2 - y1) * 2
            
            # id1 -> id2 (E 方向, y 增加)
            # 節點: id1*7+1 -> id2*7+1
            adj[id1 * 7 + 1].append((id2 * 7 + 1, dist))
            
            # id2 -> id1 (W 方向, y 減少)
            # 節點: id2*7+2 -> id1*7+2
            adj[id2 * 7 + 2].append((id1 * 7 + 2, dist))

    # 3. 構建豎直方向的邊 (S: 3, N: 4)
    for c in by_col:
        line = sorted(by_col[c]) # 按 x 排序
        for j in range(len(line) - 1):
            x1, id1 = line[j]
            x2, id2 = line[j+1]
            dist = (x2 - x1) * 2
            
            # id1 -> id2 (S 方向, x 增加)
            adj[id1 * 7 + 3].append((id2 * 7 + 3, dist))
            
            # id2 -> id1 (N 方向, x 減少)
            adj[id2 * 7 + 4].append((id1 * 7 + 4, dist))

    # 4. 構建環狀方向的邊 (C: 5, I: 6)
    for k in by_ring:
        line = sorted(by_ring[k]) # 按環上 pos 排序
        # 計算該層環的總長度
        # current_n = n - 2*(k-1)
        current_n = n - 2 * k + 2
        perimeter = (current_n - 1) * 4
        
        count = len(line)
        for j in range(count):
            pos1, id1 = line[j]
            # 環是閉合的，最後一點連回第一點
            pos2, id2 = line[(j + 1) % count]
            
            # 順時針距離 (pos 增加的方向)
            # 注意處理跨越周長的情況
            dist_cw = (pos2 - pos1 + perimeter) % perimeter * 2
            
            # id1 -> id2 (C 方向, 順時針)
            adj[id1 * 7 + 5].append((id2 * 7 + 5, dist_cw))
            
            # id2 -> id1 (I 方向, 逆時針)
            # 逆時針距離 = 順時針距離 (因為是雙向軌道，物理距離一樣)
            # 從 id2 到 id1 的順時針距離其實就是 id1 到 id2 的逆時針代價
            adj[id2 * 7 + 6].append((id1 * 7 + 6, dist_cw))

    # 5. Dijkstra 演算法
    # 起點是 p[0] 的 Hub (0*7 = 0)
    # 終點是 p[1] 的 Hub (1*7 = 7)
    start_node = 0
    target_node = 7
    
    dist = [-1] * (num_points * 7)
    prev = [-1] * (num_points * 7) # 用於還原路徑
    
    pq = [(0, start_node)]
    dist[start_node] = 0
    
    final_cost = -1
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u] and dist[u] != -1:
            continue
        
        if u == target_node:
            final_cost = d
            break
            
        for v, weight in adj[u]:
            if dist[v] == -1 or dist[v] > d + weight:
                dist[v] = d + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    if final_cost == -1:
        print("Impossible!")
    else:
        # 輸出總時間 (扣除起點多算的一次上車費)
        print(final_cost - 1)
        
        # 還原路徑
        path_nodes = []
        curr = target_node
        while curr != -1:
            path_nodes.append(curr)
            curr = prev[curr]
        path_nodes.reverse()
        
        # 提取經過的站點 (只取 Hub 節點)
        station_path = []
        for node in path_nodes:
            if node % 7 == 0:
                station_idx = node // 7
                station_path.append(p[station_idx])
        
        # 輸出乘坐地鐵數量 (段數)
        print(len(station_path) - 1)
        
        # 輸出起點
        print(f"{station_path[0][0]} {station_path[0][1]}")
        
        # 輸出每一段的詳細信息
        for i in range(len(station_path) - 1):
            u_x, u_y = station_path[i]
            v_x, v_y = station_path[i+1]
            
            direction = ""
            
            # 判斷方向
            if u_x == v_x: # 同行
                if v_y > u_y: direction = "E"
                else: direction = "W"
            elif u_y == v_y: # 同列
                if v_x > u_x: direction = "S"
                else: direction = "N"
            else: # 環線
                # 重新計算 pos 來判斷是順還是逆
                # 這裡需要比較順時針和逆時針哪個距離更短
                # 或者直接看路徑中實際走了哪種邊，但在只存了站點的情況下，重算比較簡單
                k, pos_u = get_ring_pos(u_x, u_y, n)
                _, pos_v = get_ring_pos(v_x, v_y, n)
                current_n = n - 2 * k + 2
                perimeter = (current_n - 1) * 4
                
                dist_cw = (pos_v - pos_u + perimeter) % perimeter
                dist_ccw = (pos_u - pos_v + perimeter) % perimeter
                
                if dist_cw < dist_ccw:
                    direction = "C"
                else:
                    direction = "I"
            
            print(direction)
            print(f"{v_x} {v_y}")

if __name__ == "__main__":
    solve()