#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, tc=1, k, n;
    cin >> t;
    while (t--) {
        vector<int> costs(36);
        for (int i=0; i<36; i++) cin >> costs[i];
        cin >> k;
        cout << (tc > 1 ? "\n" : "");
        cout << "Case " << tc++ << ":" << endl;

        for (int i=0; i<k; i++) {
            cin >> n;
            vector<int> min_r;
            int min_s = INT_MAX;
            for (int r=2; r<=36; r++) {
                int nn = n, s = 0;
                while (nn) {
                    s += costs[nn % r];
                    nn /= r;
                }
                if (s < min_s) {
                    min_r.clear();
                    min_r.push_back(r);
                    min_s = s;
                } else if (s == min_s) {
                    min_r.push_back(r);
                }
            }
            cout << "Cheapest base(s) for number " << n << ": ";
            for (int i=0; i<min_r.size(); i++) {
                cout << min_r[i];
                if (i != min_r.size()-1) cout << " ";
            }
            cout << endl;
        }
    }
    return 0;
}