#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'
#define all(x) x.begin(), x.end()

class Rect {
public:
    int x1, y1, x2, y2;
};

class Edge {
public:
    int st, ed, rect_id, delta;
    Edge(int st, int ed, int rect_id, int delta) : st(st), ed(ed), rect_id(rect_id), delta(delta) {}
    bool operator<(const Edge &other) const {
        return st < other.st;
    }
};

class UnionFind {
public:
    vector<int> pa;
    vector<LL> areas;

    UnionFind(int n, const vector<LL>& areas) : pa(n), areas(areas) {
        iota(all(pa), 0);
    }

    int find(int x) {
        return pa[x] == x ? x : pa[x] = find(pa[x]);
    }

    bool merge(int x, int y){
        int fx = find(x), fy = find(y);
        if(fx == fy) return false;
        if(areas[fx] < areas[fy]) swap(fx, fy);
        pa[fy] = fx;
        areas[fx] += areas[fy];
        return true;
    }
};

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x, y, w, h;
    while(cin >> n && n){
        vector<Rect> rects(n);
        vector<LL> areas(n);
        for(int i = 0; i < n; i++){
            cin >> x >> y >> w >> h;
            rects[i].x1 = x;
            rects[i].y1 = y;
            rects[i].x2 = x + w;
            rects[i].y2 = y + h;
            areas[i] = (LL) w * h;
        }
        
        // 初始化 Disjoint Set
        UnionFind uf(n, areas);

        // 離散化
        set<int> xSet, ySet;
        for(auto &rect : rects){
            xSet.insert(rect.x1);
            xSet.insert(rect.x2);
            ySet.insert(rect.y1);
            ySet.insert(rect.y2);
        }
        map<int, int> xMap, yMap;
        int idx = 1;
        for (auto x : xSet) xMap[x] = idx++;
        idx = 1;
        for (auto y : ySet) yMap[y] = idx++;

        // 掃描線
        unordered_map<int, vector<Edge>> xLines, yLines;
        for (int i = 0; i < n; i++){
            Rect &rect = rects[i];
            xLines[xMap[rect.x1]].push_back(Edge(yMap[rect.y1], yMap[rect.y2], i, 1));
            xLines[xMap[rect.x2]].push_back(Edge(yMap[rect.y1], yMap[rect.y2], i, -1));
            yLines[yMap[rect.y1]].push_back(Edge(xMap[rect.x1], xMap[rect.x2], i, 1));
            yLines[yMap[rect.y2]].push_back(Edge(xMap[rect.x1], xMap[rect.x2], i, -1));
        }

        // 掃 x 軸上相鄰的線段
        for (auto it = xLines.begin(); it != xLines.end(); ++it) {
            int x = it->first;
            vector<Edge>& edges = it->second;
            sort(all(edges));
            // 這裡 C++ 二重迴圈枚舉所有 Edge 也可以過，但區間合併可以做到 O(n log n)
            Edge &e1 = edges[0];
            for (int j = 1; j < edges.size(); j++) {
                Edge &e2 = edges[j];
                if (e1.st <= e2.st && e2.st <= e1.ed) {
                    uf.merge(e1.rect_id, e2.rect_id);
                    e1.ed = max(e1.ed, e2.ed);
                }
                else {
                    e1 = e2;
                }
            }
        }
        // 掃 y 軸上相鄰的線段
        for (auto it = yLines.begin(); it != yLines.end(); ++it) {
            int y = it->first;
            vector<Edge>& edges = it->second;
            sort(all(edges));
            Edge &e1 = edges[0];
            for (int j = 1; j < edges.size(); j++) {
                Edge &e2 = edges[j];
                if (e1.st <= e2.st && e2.st <= e1.ed) {
                    uf.merge(e1.rect_id, e2.rect_id);
                    e1.ed = max(e1.ed, e2.ed);
                }
                else {
                    e1 = e2;
                }
            }
        }
        cout << *max_element(all(uf.areas)) << endl;
    }
}