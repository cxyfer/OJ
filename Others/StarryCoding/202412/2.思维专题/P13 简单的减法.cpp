#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, k; cin >> n >> k;
    vector<LL> A(n);
    for (int i = 0; i < n; ++i) cin >> A[i];
    LL s = accumulate(A.begin(), A.end(), 0LL);

    auto check = [&](LL x) {
        LL cnt = 0;
        for (int i = 0; i < n; ++i) cnt += min(A[i], x);
        return cnt >= k * x;
    };

    LL left = 0, right = s / k;
    while (left <= right) {
        LL mid = left + (right - left) / 2;
        if (check(mid)) left = mid + 1;
        else right = mid - 1;
    }
    cout << right << endl;
    return 0;
}