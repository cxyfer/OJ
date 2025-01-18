#include <bits/stdc++.h>
using namespace std;
using LL = long long;
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int T;
    cin >> T;

    for(int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;

        vector<pair<int, int>> P(N);
        for(int i = 0; i < N; i++) {
            cin >> P[i].first >> P[i].second;
        }

        sort(P.begin(), P.end());

        int ans = 0;
        for(int i = 0; i < N-1; i++) {
            int cur = P[i].second;
            for(int j = i+1; j < N; j++) {
                if(cur >= P[j].second) {
                    ans++;
                }
            }
        }

        cout << ans << endl;
    }

    return 0;
}
