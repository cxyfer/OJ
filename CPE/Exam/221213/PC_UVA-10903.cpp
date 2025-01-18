#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 105;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase=1, n, k, p1, p2, w, l;
    int cnt[N][2]; // W / L
    string m1, m2;
    while (cin >> n >> k && n){
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < k * n * (n - 1) / 2; i++){
            cin >> p1 >> m1 >> p2 >> m2;
            p1--, p2--;
            if (m1 == "rock" && m2 == "scissors" || m1 == "scissors" && m2 == "paper" || m1 == "paper" && m2 == "rock"){
                cnt[p1][0]++;
                cnt[p2][1]++;
            }else if (m2 == "rock" && m1 == "scissors" || m2 == "scissors" && m1 == "paper" || m2 == "paper" && m1 == "rock"){
                cnt[p2][0]++;
                cnt[p1][1]++;
            }
        }
        if (kase++ > 1) cout << endl;
        for (int i = 0; i < n; i++){
            w = cnt[i][0], l = cnt[i][1];
            if (w + l == 0){
                cout << "-" << endl;
            }else{
                cout << fixed << setprecision(3) << (double) w / (w + l) << endl;
            }
        }
    }
    return 0;
}