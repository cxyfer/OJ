#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL x, y;
    int ans, carry;
    while (cin >> x >> y && (x || y)) {
        ans = 0;
        carry = 0;
        while (x || y) {
            if (x % 10 + y % 10 + carry > 9) {
                ans++;
                carry = 1;
            } else {
                carry = 0;
            }
            x /= 10;
            y /= 10;
        }
        cout << (ans ? to_string(ans) : "No") << " carry operation" << (ans > 1 ? "s." : ".") << endl;
    }
    return 0;
}