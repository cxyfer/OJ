#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
#define endl '\n'

void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> A(n + 1);
    for (int i = 1; i <= n; i++) cin >> A[i];

    // 根據複雜度分析，選擇適當的 B 值
    int B = (n > 1) ? (sqrt(static_cast<double>(n) / log2(n)) + 1) : 1;
    vector<i64> s(n + 1);
    for (int i = 1; i <= n; i++) s[i] = s[i - 1] + A[i];

    while (q--) {
        int l, r, x; cin >> l >> r >> x;
        l--;  // 0-based index [l, r)
        int cnt = 0, rem = 0, ln = 1;
        while (l < r) {
            // 剩餘長度不足 ln 或 剩餘總和不足 x
            if (r - l < ln || s[r] - s[l] < x) {
                rem = s[r] - s[l];
                break;
            }

            // 1. 當前長度 ln 足夠
            if (s[l + ln] - s[l] >= x) {
                // ln >= B 時，直接跳躍
                if (ln >= B) {
                    while (l + ln <= r && s[l + ln] - s[l] >= x) {
                        l += ln;
                        cnt += 1;
                    }
                }
                // ln < B 時，二分搜尋找到最大的跳躍次數
                else {
                    int left = 1, right = (r - l) / ln;
                    while (left <= right) {
                        int mid = (left + right) / 2;
                        if (s[l + mid * ln] - s[l + (mid - 1) * ln] >= x)
                            left = mid + 1;
                        else right = mid - 1;
                    }
                    cnt += right;
                    l += right * ln;
                }
                ln += 1;
            }
            // 2. 嘗試 ln + 1
            else if (l + ln + 1 <= r && s[l + ln + 1] - s[l] >= x) {
                ln += 1;
            }
            // 3. 嘗試 ln + 2
            else if (l + ln + 2 <= r && s[l + ln + 2] - s[l] >= x) {
                ln += 2;
            }
            // 4. 二分搜尋找新的長度
            else {
                // 尋找最小的 idx 使得 s[idx] - s[l] >= x 即 s[idx] >= s[l] + x
                i64 target = s[l] + x;
                int idx = lower_bound(s.begin() + l + 1, s.begin() + r + 1, target) - s.begin();
                cnt += 1;
                ln = idx - l;
                l = idx;
            }
        }
        cout << cnt << " " << rem << endl;
    }
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}