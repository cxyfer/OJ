#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Point {
    double x, y;
};

double dist(Point p1, Point p2) {
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

double solve(vector<Point> &points, int l, int r) {
    if (l == r) return FLT_MAX;

    int mid = (l + r) / 2;
    double mid_x = points[mid].x;

    double d_l = solve(points, l, mid);
    double d_r = solve(points, mid + 1, r);
    double d = min(d_l, d_r);

    // Merge Sort by y
    vector<Point> tmp(r - l + 1);
    int idx = 0, i = l, j = mid + 1;
    while (i <= mid || j <= r) {
        if (i <= mid && (j > r || points[i].y < points[j].y)) {
            tmp[idx++] = points[i++];
        } else {
            tmp[idx++] = points[j++];
        }
    }
    for (int i = l; i <= r; i++) points[i] = tmp[i - l];

    vector<Point> candidates;
    for (int i = l; i <= r; i++) {
        if (abs(points[i].x - mid_x) <= d) {
            candidates.push_back(points[i]);
        }
    }

    for (int i = 0; i < candidates.size(); i++) {
        for (int j = i + 1; j < candidates.size(); j++) {
            if (candidates[j].y - candidates[i].y > d) break;
            d = min(d, dist(candidates[i], candidates[j]));
        }
    }

    return d;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<Point> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }
    sort(points.begin(), points.end(),
            [](Point a, Point b) { return a.x < b.x; });
    double ans = solve(points, 0, n - 1);
    cout << fixed << setprecision(6) << ans << endl;
    return 0;
}