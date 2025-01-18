/*
    Counter
    tags: Counter, Simulation, 紫書-Ch3
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase=1, n, A, B;
    int s[N], g[N], cnt_s[10], cnt_tmp[10], cnt_g[10];
    while (cin >> n && n) {
        cout << "Game " << kase++ << ":" << endl;
        for (int i = 0; i < n; i++) cin >> s[i]; // read secret
        memset(cnt_s, 0, sizeof(cnt_s));
        for (int i = 0; i < n; i++) cnt_s[s[i]]++;
        while (1) {
            for (int i = 0; i < n; i++) cin >> g[i]; // read guess
            if (g[0] == 0) break;
            memset(cnt_tmp, 0, sizeof(cnt_tmp));
            memset(cnt_g, 0, sizeof(cnt_g));
            A = B = 0;
            for (int i = 1; i < 10; i++) cnt_tmp[i] = cnt_s[i];
            for (int i = 0; i < n; i++){
                if (s[i] == g[i]) {
                    A++;
                    cnt_tmp[s[i]]--;
                }
                else {
                    cnt_g[g[i]]++;
                }
            }
            for (int i = 1; i < 10; i++) {
                B += min(cnt_tmp[i], cnt_g[i]);
            }
            cout << "    (" << A << "," << B << ")" << endl;
        }
    }
    return 0;
}