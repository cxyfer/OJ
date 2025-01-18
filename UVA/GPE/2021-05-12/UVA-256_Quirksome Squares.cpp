#include <bits/stdc++.h>
using namespace std;
const int N = 1e4;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    vector<int> squares;
    vector<vector<int>> ans(9); // 2, 4, 6, 8
    for (int i = 0; i < N; i++) {
        squares.push_back(i * i);
    }
    for (int ln = 2; ln <= 8; ln += 2) {
        for (int x : squares) {
            if (x >= (int) pow(10, ln)) break;
            int a = x / (int) pow(10, ln / 2);
            int b = x % (int) pow(10, ln / 2);
            if ((a + b) * (a + b) == x) ans[ln].push_back(x);
        }
    }
    int n;
    while (cin >> n) {
        for (int x : ans[n]) {
            cout << setw(n) << setfill('0') << x << endl;
        }
    }
    return 0;
}