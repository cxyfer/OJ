#include <bits/stdc++.h>
using namespace std;
const double EPS = 1e-6;
const double INF = 1e12;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, p;
    cin >> n >> p;
    vector<pair<int, int>> devices(n);
    for (auto &[a, b] : devices) {
        cin >> a >> b;
    }

    auto check = [&](double t) {
        double cnt = 0;
        for (auto &[a, b] : devices) {
            if (b - a * t < 0) {
                cnt += (a * t - b);
                if (cnt > t * p) {
                    return false;
                }
            }
        }
        return true;
    };

    double left = 0, right = INF;
    while (right - left > EPS) {
        double mid = (left + right) / 2;
        if (check(mid)) left = mid;
        else right = mid;
    }
    if (right < INF) cout << fixed << setprecision(6) << right << endl;  // 越小越合法，問最大合法值
    else cout << -1 << endl;
    return 0;
}