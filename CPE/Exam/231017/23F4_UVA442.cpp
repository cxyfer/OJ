#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n, x, y, x1, y1;
    char ch;
    LL ans;

    map<char, pair<int, int>> mp;
    cin >> n;
    while (n--) {
        cin >> ch >> x >> y;
        mp[ch] = {x, y};
    }

    cin.ignore(1024, '\n');
    string line;
    while (getline(cin, line)) {
        ans = 0;
        stack<pair<int, int>> st;
        for (char ch : line) {
            if (mp.count(ch)) {
                st.push(mp[ch]);
            } else if (ch == ')') {
                x = st.top().first;
                y = st.top().second;
                st.pop();
                x1 = st.top().first;
                y1 = st.top().second;
                st.pop();
                if (y1 != x) {
                    ans = -1;
                    break;
                }
                ans += x1 * y1 * y;
                st.push({x1, y});  // new matrix
            }
        }
        cout << (ans != -1 ? to_string(ans) : "error") << endl;
    }
    return 0;
}