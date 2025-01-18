#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T val; // value
    SegNode() : ls(nullptr), rs(nullptr), val(0) {}
};

template<typename T>
class SegmentTree {
public:
    int n;
    vector<SegNode<T>*> roots;

    SegmentTree(int n) {
        this->n = n;
        roots.push_back(new SegNode<T>());
    }

    void insert(T v) {
        roots.push_back(_insert(roots.back(), 1, n, v));
    }

    // 在區間 [left, right] 插入值 v，返回新的根節點
    SegNode<T>* _insert(SegNode<T> *prev, int left, int right, T v) {
        SegNode<T> *node = new SegNode<T>();
        *node = *prev; // 複製舊的節點
        
        if (left == right) {
            node->val++;
            return node;
        }
        
        int mid = left + ((right - left) >> 1);
        if (v <= mid) {
            if (!prev->ls) prev->ls = new SegNode<T>();
            node->ls = _insert(prev->ls, left, mid, v);
        } else {
            if (!prev->rs) prev->rs = new SegNode<T>();
            node->rs = _insert(prev->rs, mid + 1, right, v);
        }
        pushup(node);
        return node;
    }

    // Push up node value
    void pushup(SegNode<T> *node) {
        // Update method (Customized)
        node->val = (node->ls ? node->ls->val : 0) + (node->rs ? node->rs->val : 0);
    }

   // Query the sum of the interval [l, r] in particular version
   T _query(SegNode<T> *node, int left, int right, int l, int r) {
       if (node == nullptr) return 0;
       if (l <= left && right <= r) return node->val;
       int mid = left + ((right - left) >> 1);
       T res = 0;
       if (l <= mid) res += _query(node->ls, left, mid, l, r);
       if (r > mid) res += _query(node->rs, mid + 1, right, l, r);
       return res;
   }

   T query_version(int version, int l, int r) {
       if (l > r) return 0;
       return _query(roots[version], 1, n, l, r);
   }
};

class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        // 轉換成二維座標
        vector<pair<int, int>> points;
        for (int i = 0; i < xCoord.size(); i++) {
            points.emplace_back(xCoord[i], yCoord[i]);
        }

        // 排序 x 座標
        sort(points.begin(), points.end());

        // 離散化 y 座標
        unordered_map<int, int> yMap;
        sort(yCoord.begin(), yCoord.end()); // 排序
        yCoord.erase(unique(yCoord.begin(), yCoord.end()), yCoord.end()); // 去重
        for (int i = 0; i < yCoord.size(); i++) {
            yMap[yCoord[i]] = i + 1;
        }

        // 先依照 y 座標分組
        map<int, vector<int>> mp_y;
        for (const auto& [x, y] : points) {
            mp_y[y].push_back(x);
        }
        
        // 生成潛在的 x 座標對
        map<pair<int, int>, vector<int>> mp_p;
        for (const auto& [y, Xs] : mp_y) {
            // 由於已經對 x 座標排序，所以只需要考慮相鄰的 x 座標對
            for (int i = 0; i < Xs.size(); i++) {
                for (int j = i + 1; j < Xs.size(); j++) {
                    mp_p[{Xs[i], Xs[j]}].push_back(y);
                }
            }
        }

        // 取得所有排序後的 x 座標
        vector<int> xArr;
        for (const auto& [x, _] : points) {
            xArr.push_back(x);
        }

        // Build Segment Tree
        SegmentTree<int> seg(yMap.size());
        for (const auto& [_, y] : points) {
            seg.insert(yMap[y]);
        }
        
        // Find maximum area
        long long ans = -1;
        for (const auto& [x_pair, Ys] : mp_p) {
            auto [x1, x2] = x_pair;
            for (int i = 0; i < Ys.size() - 1; i++) {
                int y1 = Ys[i], y2 = Ys[i + 1];
                int v1 = lower_bound(xArr.begin(), xArr.end(), x1) - xArr.begin();
                int v2 = upper_bound(xArr.begin(), xArr.end(), x2) - xArr.begin();
                int cnt = seg.query_version(v2, yMap[y1], yMap[y2]) - seg.query_version(v1, yMap[y1], yMap[y2]);
                if (cnt == 4) {
                    ans = max(ans, 1LL * (x2 - x1) * (y2 - y1));
                }
            }
        }
        delete seg;
        return ans;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> xCoord, yCoord;
    xCoord = {1,1,3,3};
    yCoord = {1,3,1,3};
    cout << sol.maxRectangleArea(xCoord, yCoord) << endl; // 4
    xCoord = {1,1,3,3,2};
    yCoord = {1,3,1,3,2};
    cout << sol.maxRectangleArea(xCoord, yCoord) << endl; // -1
    xCoord = {1,1,3,3,1,3};
    yCoord = {1,3,1,3,2,2};
    cout << sol.maxRectangleArea(xCoord, yCoord) << endl; // 2
    xCoord = {89,55,89,55,0,34,17,71,98,90,63,49,76,72,4,46,67,94,52,6};
    yCoord = {58,69,69,58,100,36,14,40,13,41,29,23,47,52,95,49,37,77,54,59};
    cout << sol.maxRectangleArea(xCoord, yCoord) << endl; // 374
    return 0;
}

// print(sol.maxRectangleArea([1,1,3,3],[1,3,1,3])) # 4
// print(sol.maxRectangleArea([1,1,3,3,2],[1,3,1,3,2])) # -1
// print(sol.maxRectangleArea([1,1,3,3,1,3],[1,3,1,3,2,2])) # 2
