/*
N, R, C = map(int, input().split())
S = input()
DIR = {"N": (-1, 0), "W": (0, -1), "S": (1, 0), "E": (0, 1)}

st = set([(0, 0)])
sx = sy = 0
ans = ""
for d in S:
    dx, dy = DIR[d]
    sx += dx
    sy += dy
    ans += '1' if (sx - R, sy - C) in st else '0'
    st.add((sx, sy))
print(ans)
*/

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    int N, R, C;
    string S;
    cin >> N >> R >> C >> S;
    
    map<char, pair<int, int>> DIR = {
        {'N', {-1, 0}},
        {'W', {0, -1}},
        {'S', {1, 0}},
        {'E', {0, 1}}
    };
    
    set<pair<int, int>> st;
    st.insert({0, 0});
    int sx = 0, sy = 0;
    string ans = "";
    for (char d : S) {
        auto [dx, dy] = DIR[d];
        sx += dx;
        sy += dy;
        ans += st.find({sx - R, sy - C}) != st.end() ? '1' : '0';
        st.insert({sx, sy});
    }
    cout << ans << endl;
    return 0;
}
