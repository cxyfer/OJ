#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s, ans;
    unordered_set<string> st;
    while (cin >> s) {
        if (s == "0") break;
        if (st.find(s) == st.end()) {
            st.insert(s);
            ans += s;
        }
    }
    cout << ans << endl;
    return 0;
}