#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    string a, b, s;
    cin >> n >> m;
    map<string, string> mp;
    while (n--) {
        cin >> a >> b;
        mp[a] = b;
    }
    while (m--) {
        cin >> s;
        int k = s.size();
        if (mp.find(s) != mp.end())
            cout << mp[s] << endl;
        else if (k > 1 && s[k-1] == 'y' && s[k-2] != 'a' && s[k-2] != 'e' && s[k-2] != 'i' && s[k-2] != 'o' && s[k-2] != 'u') 
            cout << s.substr(0, k - 1) + "ies" << endl;
        else if (s[k-1] == 'o' || s[k-1] == 's' || s[k-1] == 'x' || (k > 1 && s[k-1] == 'h' && (s[k-2] == 'c' || s[k-2] == 's')))
            cout << s + "es" << endl;
        else
            cout << s + "s" << endl;
    }
    return 0;
}