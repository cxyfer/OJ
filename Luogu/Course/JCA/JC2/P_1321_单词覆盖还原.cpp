/*
    由於每個字元都不同，且最後至少存留一個字元，所以可以這樣貪
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    cin >> s;
    int x = 0, y = 0;
    s += "$$$";
    for (int i = 0; i < s.size() - 2; i++) {
        if (s[i] == 'b' || s[i + 1] == 'o' || s[i + 2] == 'y') x++;
        if (s[i] == 'g' || s[i + 1] == 'i' || s[i + 2] == 'r' || s[i + 3] == 'l') y++;
    }
    cout << x << endl << y << endl;
    return 0;
}