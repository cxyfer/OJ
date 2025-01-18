#include <bits/stdc++.h>
using namespace std;
const string one = "one", two = "two";
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        string s; cin >> s;
        if (s.size() == 5) cout << 3 << endl;
        else {
            int diff1 = 0;
            for (int i = 0; i < 3; i++) {
                if (s[i] != one[i]) diff1++;
            }
            cout << (diff1 <= 1 ? 1 : 2) << endl;
        }
    }
    return 0;
}