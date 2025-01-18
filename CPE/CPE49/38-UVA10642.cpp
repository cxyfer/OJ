#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int calc(int x, int y) { // from (0, 0) to (x, y)
    int t = x + y;
    return (t-1) * (t) / 2 + t + x;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, tc=1, sx, sy, ex, ey;
    cin >> t;
    while (t--) {
        cin >> sx >> sy >> ex >> ey;
        cout << "Case " << tc++ << ": " << calc(ex, ey) - calc(sx, sy) << endl;
    }
    return 0;
}