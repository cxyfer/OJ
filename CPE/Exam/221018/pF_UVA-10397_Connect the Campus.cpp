#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class Edge {
public:
    int u, v;
    double w;
    Edge(int u, int v, double w): u(u), v(v), w(w) {}
    bool operator<(const Edge &e) const {
        return w < e.w;
    }
};

vector<pair<int, int>> points;
vector<Edge> edges;
vector<int> pa;
int find(int x) {
    return pa[x] == x ? x : pa[x] = find(pa[x]);
}
bool _union(int x, int y) {
    int fx = find(x), fy = find(y);
    if (fx != fy) {
        pa[fx] = fy;
        return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, x, y, u, v;
    while (cin >> n) {
        points.clear();
        for (int i = 0; i < n; i++) {
            cin >> x >> y;
            points.push_back({x, y});
        }
        int cnt = 0;
        pa.resize(n);
        for (int i = 0; i < n; i++) pa[i] = i;
        cin >> m;
        for (int i = 0; i < m; i++) {
            cin >> u >> v;
            if (_union(u - 1, v - 1)) cnt++;
        }
        edges.clear();
        for (int i = 0; i < n; i++) {
            pair<int, int> p = points[i];
            for (int j = i + 1; j < n; j++) {
                pair<int, int> q = points[j];
                x = p.first - q.first;
                y = p.second - q.second;
                double w = sqrt(x * x + y * y);
                edges.push_back({i, j, w});
            }
        }
        sort(edges.begin(), edges.end());
        double ans = 0;
        for (Edge e : edges) {
            if (_union(e.u, e.v)) {
                ans += e.w;
                cnt++;
                if (cnt == n - 1) break;
            }
        }
        cout << fixed << setprecision(2) << ans << endl;
    }
    return 0;
}