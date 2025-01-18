#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Point {
    int x, y, z;
};

struct Sphere {
    Point c;
    int r;
};

double dist2(Point a, Point b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) + (a.z - b.z) * (a.z - b.z);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    string name;
    Point P1, P2, D, E;
    while (cin >> name) {
        cin >> P1.x >> P1.y >> P1.z >> P2.x >> P2.y >> P2.z;
        D = {P2.x - P1.x, P2.y - P1.y, P2.z - P1.z};
        cin >> n;
        vector<Sphere> spheres(n);
        for (int i = 0; i < n; i++) {
            cin >> spheres[i].c.x >> spheres[i].c.y >> spheres[i].c.z >> spheres[i].r;
        }
        vector<pair<double, double>> intervals;
        for (auto &s : spheres) {
            E = {P1.x - s.c.x, P1.y - s.c.y, P1.z - s.c.z};
            double a = dist2(P1, P2);
            double b = 2 * (E.x * D.x + E.y * D.y + E.z * D.z);
            double c = dist2(P1, s.c) - s.r * s.r;
            double delta = b * b - 4 * a * c;
            if (delta <= 0) continue;
            double sqrt_delta = sqrt(delta);
            double t1 = (-b - sqrt_delta) / (2 * a);
            double t2 = (-b + sqrt_delta) / (2 * a);
            t1 = max(0.0, t1);
            t2 = min(1.0, t2);
            if (t1 <= t2) {
                intervals.emplace_back(t1, t2);
            }
        }

        // sort(intervals.begin(), intervals.end());
        // vector<pair<double, double>> merged;
        // for (auto &[l, r] : intervals) {
        //     if (merged.empty() || l > merged.back().second) {
        //         merged.emplace_back(l, r);
        //     } else {
        //         merged.back().second = max(merged.back().second, r);
        //     }
        // }

        double ans = 0;
        for (auto p : intervals) {
            ans += p.second - p.first;
        }
        cout << name << endl;
        cout << fixed << setprecision(2) << ans * 100 << endl;
    }
    return 0;
}