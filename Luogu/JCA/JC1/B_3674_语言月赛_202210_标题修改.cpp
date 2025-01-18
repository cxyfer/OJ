#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    getline(cin, s);
    int n = s.size();
    int i = 0, j = 0;
    while (i < n) {
        if (!isalpha(s[i])) {
            i++;
            continue;
        }
        j = i;
        while (j < n && isalpha(s[j])) {
            if ((j - i) & 1) {
                s[j] = tolower(s[j]);
            } else {
                s[j] = toupper(s[j]);
            }
            j++;
        }
        i = j;
    }
    cout << s << endl;
    return 0;
}
