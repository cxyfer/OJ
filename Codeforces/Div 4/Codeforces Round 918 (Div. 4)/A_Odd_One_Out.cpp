#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int a, b, c;
        cin >> a >> b >> c;
        if (a == b){
            cout << c << endl;
        }
        else if (b == c){
            cout << a << endl;
        }
        else{
            cout << b << endl;
        }
    }
    return 0;
}