#include <bits/stdc++.h>
using namespace std;
const double INF = 1e18;
#define endl '\n'

struct Point {
    int x, y;
};

double dist(const Point &a, const Point &b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

int n;
vector<Point> points;
vector<vector<double>> memo;

double dfs(int i, int j) {
    if (i == n - 1) return dist(points[i], points[j]);
    double &res = memo[i][j];
    if (res != INF) return res;
    res = dfs(i + 1, j) + dist(points[i], points[i + 1]);
    if (j != i + 1) {
        res = min(res, dfs(i + 1, i) + dist(points[j], points[i + 1]));
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    while (cin >> n) {
        points.resize(n);
        for (int i = 0; i < n; ++i) {
            cin >> points[i].x >> points[i].y;
        }
        memo.assign(n, vector<double>(n, INF));
        cout << fixed << setprecision(2) << dfs(0, 0) << endl;
    }
    return 0;
}