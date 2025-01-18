#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL x;
    string s;
    while (cin >> x) {
        cin.ignore(1024, '\n');
        getline(cin, s);
        stringstream ss(s);
        vector<LL> A;
        LL a;
        while (ss >> a) {
            A.push_back(a);
        }
        LL n = A.size() - 1;
        LL ans = A[0] * n;
        for (int i = 1; i < n; ++i) {
            ans = ans * x + A[i] * (n - i);
        }
        cout << ans << endl;
        
    }
    return 0;
}