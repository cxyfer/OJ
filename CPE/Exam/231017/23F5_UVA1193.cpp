#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

bool cmp(const pair<double, double>& a, const pair<double, double>& b) {
    return a.second < b.second;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, d, tc = 1, x, y;
    double dx;
    while (cin >> n >> d && n && d) {
        vector<pair<double, double>> intervals;
        bool flag = false;
        for (int i = 0; i < n; ++i) {
            cin >> x >> y;
            if (y > d) flag = true; // 不可能放置
            dx = sqrt(d * d - y * y);
            intervals.push_back({x - dx, x + dx}); // 可以涵蓋這個島嶼的雷達其所屬的區間
        }
        sort(intervals.begin(), intervals.end(), cmp); // 按照右端點排序
        int ans = 0;
        double last = (double) -INF; // 上一個組的第一個區間的右端點
        for (auto &i : intervals) {
            if (i.first > last) { // 和上一組的所有區間不重疊
                last = i.second;
                ans++;
            }
        }
        cout << "Case " << tc++ << ": " << (flag ? -1 : ans) << endl;
    }
    return 0;
}