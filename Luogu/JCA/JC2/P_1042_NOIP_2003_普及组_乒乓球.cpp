#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    char ch;
    string s, line;
    while (cin >> ch) {
        if (ch == 'E') {
            break;
        }
        s += ch;
    }
    for (int target : {11, 21}) {
        int x = 0, y = 0;
        for (char ch : s) {
            if (ch == 'W') x++;
            else y++;
            if (max(x, y) >= target && abs(x - y) >= 2) {
                cout << x << ":" << y << endl;
                x = y = 0;
            }
        }
        cout << x << ":" << y << endl;
        cout << endl;
    }
    return 0;
}