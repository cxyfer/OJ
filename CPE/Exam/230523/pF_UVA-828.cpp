#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

char rotateLeft(char ch, int N) { // rotate left N times
    return ('A' + (ch - 'A' - N + 26) % 26);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, N, q, kase = 0;
    string L, s, ans;
    cin >> t;
    cin.ignore(); // skip rest of line
    while (t--) { 
        cin.ignore(1024, '\n'); // skip blank line
        if (kase++) cout << endl;
        getline(cin, L);
        cin >> N >> q;
        cin.ignore(); // skip rest of line
        set<char> st(L.begin(), L.end()); // store all characters in L
        while (q--) {
            getline(cin, s); // encrypted string
            int i = 0, m = 0;
            ans = "";
            bool flag = true;
            while (i < s.size()) {
                char ch = s[i];
                // Rule 1
                if (ch == ' ') {
                    ans += ch;
                    i++;
                    continue;
                }
                // Rule 3
                else if (i + 2 < s.size() && ch == L[m] && s[i+2] == L[(m+1) % L.size()]) {
                    char ori = rotateLeft(s[i+1], N); // original character
                    if (!st.count(ori)) { // not satisfy Rule 3
                        // Rule 2
                        ori = rotateLeft(ch, N); // original character
                        if (st.count(ori)) { // also not satisfy Rule 2
                            flag = false;
                            break;
                        }
                        ans += ori;
                        i++;
                        continue;
                    }
                    ans += ori;
                    i += 3;
                    m = (m + 1) % L.size();
                // Rule 2
                } else {
                    char ori = rotateLeft(ch, N); // original character
                    if (st.count(ori)) { // not satisfy Rule 2
                        flag = false;
                        break;
                    }
                    ans += ori;
                    i++;
                }
            }
            cout << (flag ? ans : "error in encryption") << endl;
        }
    }
    return 0;
}