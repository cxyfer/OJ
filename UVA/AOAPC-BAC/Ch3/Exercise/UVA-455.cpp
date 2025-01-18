#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t; cin.ignore(1024, '\n');
    string s;
    while (t--) {
        cin.ignore(1024, '\n');
        getline(cin, s); // read a line
        int n = s.size();
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) { // i is a factor of n
                bool flag = true;
                for (int j = 0; j < n; j++) {
                    if (s[j] != s[j % i]) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    cout << i << endl;
                    break;
                }
            }
        }
        if (t) cout << endl;
    }
    return 0;
}