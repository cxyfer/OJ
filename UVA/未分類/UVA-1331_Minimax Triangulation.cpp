#include <bits/stdc++.h>
using namespace std;
const int N = 55;
#define endl '\n'

int t, n;
struct Point {
    double x, y;
} points[N];

double dist(Point p1, Point p2) {
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

double area(Point p1, Point p2, Point p3) {
    double d1 = dist(p1, p2), d2 = dist(p1, p3), d3 = dist(p2, p3);
    double s = (d1 + d2 + d3) / 2;
    return sqrt(s * (s - d1) * (s - d2) * (s - d3)); // 海龍公式
}

// 計算 a, b, c 形成的三角形是否為凸多邊形的一部份
// 檢查有沒有其他點在這個三角形內部
bool check(int a, int b, int c) {
    double A = area(points[a], points[b], points[c]);
    for (int i = 0; i < n; i++) {
        if (i == a || i == b || i == c) continue;
        double tmp = area(points[a], points[b], points[i]) + area(points[a], points[c], points[i]) + area(points[b], points[c], points[i]);
        if (abs(tmp - A) < 1e-6) {
            return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> points[i].x >> points[i].y;
        }
        vector<vector<double>> f(n, vector<double>(n, DBL_MAX));
        for (int i = 0; i < n - 1; i++) {
            f[i][i + 1] = 0;
        }
        for (int ln = 3; ln <= n; ln++) {
            for (int i = 0; i <= n - ln; i++) {
                int j = i + ln - 1;
                for (int k = i + 1; k < j; k++) {
                    if (!check(i, k, j)) continue;
                    f[i][j] = min(f[i][j], max({f[i][k], f[k][j], area(points[i], points[k], points[j])}));
                }
            }
        }
        cout << fixed << setprecision(1) << f[0][n - 1] << endl;
    }
    return 0;
}