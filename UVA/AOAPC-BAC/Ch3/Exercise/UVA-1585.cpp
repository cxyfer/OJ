#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        string s; cin >> s;
        int ans=0, cur=0;
        for (auto &ch: s){
            if (ch == 'O'){
                cur ++;
                ans += cur;
            }
            else{
                cur = 0;
            }
        }
        cout << ans << endl;
    }
    return 0;
}