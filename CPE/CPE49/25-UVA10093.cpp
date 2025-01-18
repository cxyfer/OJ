#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int ans, s, mx;
    string line;
    while (cin >> line) {
        vector<int> N;
        for (char ch : line) {
            if (isupper(ch)) N.push_back(ch - 'A' + 10);
            else if (islower(ch)) N.push_back(ch - 'a' + 36);
            else if (isdigit(ch)) N.push_back(ch - '0');
        }
        s = 0;
        mx = -1;
        for (int x : N){
            mx = max(mx, x);
            s += x;
        }
        ans = -1;
        for (int i = max(2, mx + 1) ; i <= 62; ++i) {
            if (s % (i - 1) == 0) {
                ans = i;
                break;
            }
        }
        cout << (ans == -1 ? "such number is impossible!" : to_string(ans)) << endl;
    }
    return 0;
}