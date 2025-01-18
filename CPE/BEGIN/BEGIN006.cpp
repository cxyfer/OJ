#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL sum, x;
    string s;
    while (getline(cin, s)) {
        sum = 0;
        stringstream ss(s);
        while (ss >> x) {
            sum += x;
        }
        cout << "Sum=" << sum << endl;
    }
    return 0;
}