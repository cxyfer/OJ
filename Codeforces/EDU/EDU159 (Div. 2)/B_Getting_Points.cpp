#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        ll n, P, l, t;
        cin >> n >> P >> l >> t;

        ll cnt_2t = (n + 6) / 14; // 可以讀書+完成兩份作業的天數
        ll cnt_1t = (n + 6) / 7 - 2 * cnt_2t; // 可以讀書+完成一份作業的天數
        ll cnt_l = n - cnt_2t - cnt_1t; // 只能夠靠讀書獲取學分的天數

        ll score = 0;
        ll ans = n;
        while (score < P) {
            if (cnt_2t > 0) {
                ll r = (P - score) / (2 * t + l);
                if ((P - score) % (2 * t + l) != 0) {
                    r++;
                }
                int day = min(r, cnt_2t);
                score += day * (2 * t + l);
                cnt_2t -= day;
                ans -= day;
            } else if (cnt_1t > 0) {
                ll r = (P - score) / (t + l);
                if ((P - score) % (t + l) != 0) {
                    r++;
                }
                ll day = min(r, cnt_1t);
                score += day * (t + l);
                cnt_1t -= day;
                ans -= day;
            } else if (cnt_l > 0) {
                ll r = (P - score) / l;
                if ((P - score) % l != 0) {
                    r++;
                }
                ll day = min(r, cnt_l);
                score += day * l;
                cnt_l -= day;
                ans -= day;
            } else {
                break;
            }
        }
        cout << ans << endl;
    }

    return 0;
}
