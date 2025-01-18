#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s, t;
    while (cin >> s >> t) {
        int j = 0;
        for (char ch : t) {
            if (ch == s[j]) {
                j++;
                if (j == s.size()) break;
            }
        }
        cout << (j == s.size() ? "Yes" : "No") << endl;
    }
    return 0;
}