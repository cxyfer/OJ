#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, a, b;
    cin >> t;
    while (t--) {
        cin >> a >> b;
        if ((a + b) % 3 == 0 and 2 * a >= b and 2 * b >= a) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
        
    }
    return 0;
}