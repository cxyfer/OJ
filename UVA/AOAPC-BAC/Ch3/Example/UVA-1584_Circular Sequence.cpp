/*
    String
    tags: string, 紫書-Ch3
*/
#include <bits/stdc++.h>
using namespace std;
const int N = 1000;
#define endl '\n'

int main() {
    int t;
    cin >> t;
    string s, ans, cur;
    while (t--){
        cin >> s;
        ans = s;
        for (int i = 1; i < s.size(); i++){
            cur = s.substr(i) + s.substr(0, i);
            if (cur < ans){
                ans = cur;
            }
        }
        cout << ans << endl;
    }
    return 0;
}