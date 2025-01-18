#include <bits/stdc++.h>
using namespace std;
using LL = long long;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL T;
    cin >> T;

    for (LL tc = 1; tc <= T; ++tc) {
        LL N;
        cin >> N;

        vector<LL> A(N);
        for (LL i = 0; i < N; ++i) {
            cin >> A[i];
        }

        vector<LL> s_odd(1, 0), s_even(1, 0);
        for (LL i = 0; i < N; ++i) {
            if (i % 2 == 0) {
                s_even.push_back(s_even.back() + A[i]);
                s_odd.push_back(s_odd.back());
            } else {
                s_odd.push_back(s_odd.back() + A[i]);
                s_even.push_back(s_even.back());
            }
        }

        bool flag = false;
        unordered_set<LL> diff = {0};
        for (LL i = 1; i <= N; ++i) {
            LL d = s_odd[i] - s_even[i];
            if (diff.find(d) != diff.end()) {
                flag = true;
                break;
            }
            diff.insert(d);
        }

        cout << (flag ? "YES" : "NO") << endl;
    }

    return 0;
}
