#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        string S;
        cin >> S;

        deque<int> lower, upper;

        for (int idx = 0; idx < S.size(); idx++) {
            char ch = S[idx];
            if (ch == 'b'){
                if (!lower.empty()) {
                    lower.pop_back();
                }
            } else if (ch == 'B') {
                if (!upper.empty()) {
                    upper.pop_back();
                }
            } else if (islower(ch)){
                lower.push_back(idx);
            } else {
                upper.push_back(idx);
            }
        }

        string ans = "";
        while (!lower.empty() || !upper.empty()) {
            if (!lower.empty() && !upper.empty()) {
                if (lower.front() < upper.front()) {
                    ans += S[lower.front()];
                    lower.pop_front();
                } else {
                    ans +=S[upper.front()];
                    upper.pop_front();
                }
            } else if (!lower.empty()) {
                while (!lower.empty()) {
                    ans += S[lower.front()];
                    lower.pop_front();
                }
            } else if (!upper.empty()) {
                while (!upper.empty()) {
                    ans += S[upper.front()];
                    upper.pop_front();
                }
            }
        }
        cout << ans << endl;
    }

    return 0;
}
