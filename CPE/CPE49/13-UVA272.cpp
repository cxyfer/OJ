#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    int flag = 0;
    while (getline(cin, s)) {
        for (auto &ch: s){
            if (ch == '"') {
                cout << ((flag == 0)? "``" : "''");
                flag = 1 - flag;
            } else {
                cout << ch;
            }
        }
        cout << endl;
    }

    return 0;
}