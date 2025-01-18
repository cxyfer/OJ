/*
    tags: string, palindrome, 紫書-Ch3, CPE-140325
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, idx;
    bool flag1, flag2;
    string s, mp = "A   3  HIL JM O   2TUVWXY51SE Z  8 ";
    while (getline(cin, s)) {
        n = s.size();
        flag1 = (s == string(s.rbegin(), s.rend()));
        flag2 = true;
        for (int i = 0; i < n/2+1; ++i) {
            if (isupper(s[i])) idx = s[i] - 'A';
            else if (isdigit(s[i])) idx = s[i] - '0' + 25;
            else idx = -1;
            if (idx == -1 || s[n-1-i] != mp[idx]) {
                flag2 = false;
                break;
            }
        }
        cout << s << " -- is ";
        if (!flag1 && !flag2) cout << "not a palindrome." << endl;
        else if (flag1 && !flag2) cout << "a regular palindrome." << endl;
        else if (!flag1 && flag2) cout << "a mirrored string." << endl;
        else cout << "a mirrored palindrome." << endl;
        cout << endl;
    }
    return 0;
}