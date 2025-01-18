import sys
import sys
import sys
from collections import defaultdict

# 定義並查集結構，並跟踪每個集合的總面積
class UnionFind:
    def __init__(self, n, areas):
        self.parent = list(range(n))
        self.size = [1]*n
        self.total_area = areas.copy()
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        # 按大小合併
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]
        self.total_area[xr] += self.total_area[yr]

def readints():
    import sys
    return list(map(int, sys.stdin.read().split()))

def main():
    data = readints()
    idx = 0
    while idx < len(data):
        N = data[idx]
        idx +=1
        if N ==0:
            print(0)
            continue
        rectangles = []
        areas = []
        for rect_id in range(N):
            X = data[idx]
            Y = data[idx+1]
            W = data[idx+2]
            H = data[idx+3]
            idx +=4
            x2 = X + W
            y2 = Y + H
            area = W * H
            rectangles.append( (X, Y, x2, y2) )
            areas.append(area)
        uf = UnionFind(N, areas)
        
        # 建立邊界映射
        right_edges = defaultdict(list)   # x -> list of (y_start, y_end, rect_id)
        left_edges = defaultdict(list)
        top_edges = defaultdict(list)     # y -> list of (x_start, x_end, rect_id)
        bottom_edges = defaultdict(list)
        points_to_rects = defaultdict(list)   # (x,y) -> list of rect_id

        for rect_id, (x1, y1, x2, y2) in enumerate(rectangles):
            right_edges[x2].append( (y1, y2, rect_id) )
            left_edges[x1].append( (y1, y2, rect_id) )
            top_edges[y2].append( (x1, x2, rect_id) )
            bottom_edges[y1].append( (x1, x2, rect_id) )
            # 四個角
            points_to_rects[(x1, y1)].append(rect_id)
            points_to_rects[(x2, y1)].append(rect_id)
            points_to_rects[(x1, y2)].append(rect_id)
            points_to_rects[(x2, y2)].append(rect_id)
        
        # 處理垂直邊接觸
        for x in right_edges:
            if x in left_edges:
                list_right = sorted(right_edges[x], key=lambda t: t[0])  # 依 y_start 排序
                list_left = sorted(left_edges[x], key=lambda t: t[0])
                i = j =0
                len_r = len(list_right)
                len_l = len(list_left)
                while i < len_r and j < len_l:
                    r_start, r_end, r_id = list_right[i]
                    l_start, l_end, l_id = list_left[j]
                    # 判斷是否重疊或接觸
                    if r_end < l_start:
                        i +=1
                    elif l_end < r_start:
                        j +=1
                    else:
                        # 重疊或接觸
                        uf.union(r_id, l_id)
                        # 移動指標中結束較小的
                        if r_end < l_end:
                            i +=1
                        else:
                            j +=1
        # 處理水平邊接觸
        for y in top_edges:
            if y in bottom_edges:
                list_top = sorted(top_edges[y], key=lambda t: t[0])  # 依 x_start 排序
                list_bottom = sorted(bottom_edges[y], key=lambda t: t[0])
                i = j =0
                len_t = len(list_top)
                len_b = len(list_bottom)
                while i < len_t and j < len_b:
                    t_start, t_end, t_id = list_top[i]
                    b_start, b_end, b_id = list_bottom[j]
                    # 判斷是否重疊或接觸
                    if t_end < b_start:
                        i +=1
                    elif b_end < t_start:
                        j +=1
                    else:
                        # 重疊或接觸
                        uf.union(t_id, b_id)
                        # 移動指標中結束較小的
                        if t_end < b_end:
                            i +=1
                        else:
                            j +=1
        # 處理角落接觸
        for point, rect_ids in points_to_rects.items():
            if len(rect_ids) >1:
                first = rect_ids[0]
                for other in rect_ids[1:]:
                    uf.union(first, other)
        # 計算最大的面積
        max_area = 0
        for rect_id in range(N):
            if uf.parent[rect_id] == rect_id:
                if uf.total_area[rect_id] > max_area:
                    max_area = uf.total_area[rect_id]
        print(max_area)

if __name__ == "__main__":
    main()
