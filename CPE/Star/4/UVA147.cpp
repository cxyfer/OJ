#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 30005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    int a, b, n;
    int dollars[] = {5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000};
    LL dp[N] = {0};

    dp[0] = 1;
    for (int d : dollars) {
        for (int i = d; i < N; ++i) {
            dp[i] += dp[i - d];
        }
    }

    while (getline(cin, s)) {
        if (s == "0.00") break;
        a = stoi(s.substr(0, s.find('.')));
        b = stoi(s.substr(s.find('.')+1));
        cout << setw(3) << a << "." << setw(2) << setfill('0') << b;
        n = a * 100 + b;
        dp[0] = 1;
        cout << setw(17) << setfill(' ') << dp[n] << endl;
    }
    return 0;
}