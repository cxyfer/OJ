#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

unordered_map<char, pair<int, int>> DIR = {
    {'N', {-1, 0}},
    {'W', {0, -1}},
    {'S', {1, 0}},
    {'E', {0, 1}}
};

int main() {
    int N, R, C;
    string S;
    cin >> N >> R >> C >> S;
    
    set<pair<int, int>> st;
    st.insert({0, 0});
    int sx = 0, sy = 0;
    string ans = "";
    for (char d : S) {
        auto [dx, dy] = DIR[d];
        sx += dx;
        sy += dy;
        ans += st.count({sx - R, sy - C}) ? '1' : '0';
        st.insert({sx, sy});
    }
    cout << ans << endl;
    return 0;
}
