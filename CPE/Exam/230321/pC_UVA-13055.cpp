#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    string s;
    stack<string> st;
    while (t--) {
        cin >> s;
        if (s == "Sleep") { // Sleep {name}
            cin >> s;
            st.push(s);
        } else if (s == "Kick") { // Kick
            if (!st.empty()) {
                st.pop();
            }
        } else { // Test
            if (!st.empty()) {
                cout << st.top() << endl;
            } else {
                cout << "Not in a dream" << endl;
            }
        }
    }
    return 0;
}