#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<LL> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    int mx = *max_element(A.begin(), A.end());
    int K = ceil(log2(mx * 1.0 / A[0]));

    int ans = INF;
    for (int k = 0; k <= K; k++) {
        LL a0 = A[0] << k;
        
        auto check = [&](LL mid) {
            LL cnt = 0;
            for (int i = 1; i < n; i++) {
                LL x = A[i];
                while (x > a0) {
                    x >>= 1;
                    cnt++;
                }
            }
            return cnt <= mid;
        };

        int left = 0, right = 200;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        ans = min(ans, k + left);
    }
    cout << ans << endl;
    return 0;
}