/*
    Counter
    Similar to LeetCode 299. Bulls and Cows
    tags: Counter, Simulation, AOAPC-BAC-Ch3, CPE-240424
*/
#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase=1, n, A, B;
    int s[N], g[N], cnt_s0[10], cnt_s[10], cnt_g[10];
    while (cin >> n && n) {
        cout << "Game " << kase++ << ":" << endl;
        for (int i = 0; i < n; i++) cin >> s[i]; // read secret
        memset(cnt_s0, 0, sizeof(cnt_s0));
        for (int i = 0; i < n; i++) cnt_s0[s[i]]++;
        while (1) {
            for (int i = 0; i < n; i++) cin >> g[i]; // read guess
            bool flag = true; // check if all elements are 0
            for (int i = 0; i < n; i++) if (g[i] != 0) flag = false;
            if (flag) break;
            memset(cnt_s, 0, sizeof(cnt_s));
            memset(cnt_g, 0, sizeof(cnt_g));
            A = B = 0;
            for (int i = 0; i < 10; i++) cnt_s[i] = cnt_s0[i]; // set cnt_s to cnt_s0, start from 0
            for (int i = 0; i < n; i++){
                if (s[i] == g[i]) {
                    A++;
                    cnt_s[s[i]]--;
                }
                else {
                    cnt_g[g[i]]++;
                }
            }
            for (int i = 0; i < 10; i++) { // calculate B, start from 0
                B += min(cnt_s[i], cnt_g[i]);
            }
            cout << "    (" << A << "," << B << ")" << endl;
        }
    }
    return 0;
}