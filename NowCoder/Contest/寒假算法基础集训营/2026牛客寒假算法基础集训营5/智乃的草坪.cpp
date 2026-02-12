#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#define endl '\n'

void solve() {
    int n, k;
    double r, c;

    cin >> n >> k >> r >> c;
    vector<pair<double, double>> items(n);
    for (auto &[p, v] : items) {
        cin >> p >> v;
    }

    auto check = [&](double t) -> bool {
        vector<pair<double, double>> intervals;
        for (auto &[p, v] : items) {
            double ri = v * t;
            if (ri < r) continue;
            double d = sqrt(ri * ri - r * r);

            // C++ 可以把全部區間丟去排序，然而 Python 會 TLE，需要去除無效區間
            // intervals.emplace_back(p - d, p + d);

            // 不過還是可以去除不可能包含 [0, c] 的無效區間
            if (p - d <= c && p + d >= 0)
                intervals.emplace_back(p - d, p + d);
        }

        if (intervals.empty()) return false;
        int m = intervals.size();
        ranges::sort(intervals);

        int i = 0, cnt = 0;
        double cur = 0;
        while (cur < c && cnt < k && i < m) {
            double nxt = -1e18;
            while (i < m && intervals[i].first <= cur) {
                nxt = max(nxt, intervals[i].second);
                i++;
            }
            if (nxt <= cur) return false;
            cur = nxt;
            cnt++;
        }
        return cur >= c;
    };

    double left = 0, right = max(c, 2 * r);
    while (right - left > 1e-4) {
        double mid = (left + right) / 2;
        if (check(mid)) right = mid;
        else left = mid;
    }
    cout << fixed << setprecision(10) << right << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}