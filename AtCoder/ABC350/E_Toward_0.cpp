#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

LL N, A, X, Y;
unordered_map<LL, double> dp;

double f(LL x){
    if(x == 0) return 0;
    auto it = dp.find(x);
    if(it != dp.end()) return it->second;
    double res1 = f(x / A);
    double v = 0;
    for(int i = 2; i <= 6; i++) v += f(x / i);
    double res2 = (v + 6 * Y) / 5;
    return dp[x] = min(res1 + X, res2);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> N >> A >> X >> Y;
    cout << fixed << setprecision(15) << f(N) << endl;
    return 0;
}