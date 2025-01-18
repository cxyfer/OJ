#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int ans, s, mx;
    string line;
    while (cin >> line) {
        vector<int> A;
        for (char ch : line) {
            if (isdigit(ch)) A.push_back(ch - '0');
            else if (isupper(ch)) A.push_back(ch - 'A' + 10);
            else if (islower(ch)) A.push_back(ch - 'a' + 36);
        }
        s = 0;
        mx = -1;
        for (int x : A){
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