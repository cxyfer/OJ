#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int H, U, D, F;
    while (cin >> H >> U >> D >> F && (H || U || D || F)) {
        double cur = 0, up = U, f = U * F / 100.0; // current height, increase height, fatigue factor
        int ans = 0; // day
        bool flag = false;
        while (cur >= 0 && !flag) {
            ans += 1;
            cur += up;
            up = max(0.0, up - f); // 上升高度衰減，但不會衰減到負值
            if (cur > H) flag = true; // 爬出井口
            cur -= D; // 掉落高度
        }
        cout << (flag ? "success" : "failure") << " on day " << ans << endl;
    }
    return 0;
}