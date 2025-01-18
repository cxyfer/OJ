// mp = {
//     'c': [2, 3, 4, 7, 8, 9, 10],
//     'd': [2, 3, 4, 7, 8, 9],
//     'e': [2, 3, 4, 7, 8],
//     'f': [2, 3, 4, 7],
//     'g': [2, 3, 4],
//     'a': [2, 3],
//     'b': [2],
//     'C': [3],
//     'D': [1, 2, 3, 4, 7, 8, 9],
//     'E': [1, 2, 3, 4, 7, 8],
//     'F': [1, 2, 3, 4, 7],
//     'G': [1, 2, 3, 4],
//     'A': [1, 2, 3],
//     'B': [1, 2],
// }

// t = int(input())
// for _ in range(t):
//     s = input()
//     cnt = [0] * 11
//     # st = set()
//     st = 0
//     for ch in s:
//         new_st = 0
//         for i in mp[ch]:
//             # if i not in st:
//             if not (1 << i) & st: # i not in set
//                 cnt[i] += 1
//             new_st |= 1 << i
//         # st = set(mp[ch])
//         st = new_st
//     print(*cnt[1:])

#include <bits/stdc++.h>
using namespace std;
const int N = 11;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, cnt[N];
    cin >> t;
    map<char, vector<int>> mp;
    mp['c'] = {2, 3, 4, 7, 8, 9, 10};
    mp['d'] = {2, 3, 4, 7, 8, 9};
    mp['e'] = {2, 3, 4, 7, 8};
    mp['f'] = {2, 3, 4, 7};
    mp['g'] = {2, 3, 4};
    mp['a'] = {2, 3};
    mp['b'] = {2};
    mp['C'] = {3};
    mp['D'] = {1, 2, 3, 4, 7, 8, 9};
    mp['E'] = {1, 2, 3, 4, 7, 8};
    mp['F'] = {1, 2, 3, 4, 7};
    mp['G'] = {1, 2, 3, 4};
    mp['A'] = {1, 2, 3};
    mp['B'] = {1, 2};
    while (t--) {
        string s;
        cin >> s;
        memset(cnt, 0, sizeof(cnt));
        int st = 0;
        for (char ch : s) {
            int new_st = 0;
            for (int i : mp[ch]) {
                if (!((1 << i) & st)){
                    cnt[i]++;
                }
                new_st |= (1 << i);
            }
            st = new_st;
        }
        for (int i = 1; i < N; i++) cout << cnt[i] << (i == N - 1 ? '\n' : ' ');
    }
    return 0;
}