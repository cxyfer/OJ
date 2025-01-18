/*
令 f(n) 為 n 個節點的二叉樹的個數，
則 f(n) = f(0)f(n - 1) + f(1)f(n - 2) + ... + f(n - 1)f(0) = Catalan Number

令 g(n) 為 n 個節點的二叉樹的葉子節點總個數。
則 g(n) = n * f(n - 1)

則答案為 
g(n) / f(n) 
= [C(2n-2, n-1) / n * n] / [C(2n, n) / (n + 1)]
= [C(2n-2, n-1) * (n + 1)] / C(2n, n)
= [n * n] / [(2n - 1) * (2n)] * (n + 1)
= n * (n + 1) / (2n - 1) * (2)
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    cout << fixed << setprecision(9) << (double)n * (n + 1) / (2.0 * n - 1.0) / 2.0 << endl;
    return 0;
}