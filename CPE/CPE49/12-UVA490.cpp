#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 105;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    int r = 0, c = 0;
    char mp[N][N];
    for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) mp[i][j] = '\0';
    
    while (getline(cin, s)) {
        int n = s.size();
        c = max(c, n);
        for (int i = 0; i < n; i++) mp[r][i] = s[i];
        for (int i = n; i < c; i++) mp[r][i] = ' '; // fill the rest of the row with space
        r++;
        
    }
    for (int i = 0; i < c; i++) {
        for (int j = r - 1; j >= 0; j--){
            if (mp[j][i] != '\0') cout << mp[j][i]; // 要寫檢查是不是'\0'，不然會印出空格
        }
        cout << endl;
    }
    return 0;
}