#include <bits/stdc++.h>
using namespace std;
const int N = 26;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int cnt1[N], cnt2[N];
    string s1, s2;
    while (cin >> s1 >> s2){
        memset(cnt1, 0, sizeof(cnt1));
        memset(cnt2, 0, sizeof(cnt2));
        for (char ch : s1) cnt1[ch - 'A']++;
        for (char ch : s2) cnt2[ch - 'A']++;
        sort(cnt1, cnt1 + N);
        sort(cnt2, cnt2 + N);
        bool flag = true;
        for (int i = 0; i < N && flag; i++){
            if (cnt1[i] != cnt2[i]) flag = false;
        }
        cout << (flag ? "YES" : "NO") << endl;
    }
    return 0;
}