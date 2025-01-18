#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int I, tmp, ans;
    string b;
    while (cin >> I && I) {
        ans = 0;
        tmp = I;
        b = "";
        while (tmp) {
            ans += tmp & 1;
            b += (tmp & 1)? '1': '0';
            tmp >>= 1;
        }
        reverse(b.begin(), b.end());
        cout << "The parity of " << b << " is " << ans << " (mod 2)." << endl;
    }
    return 0;
}