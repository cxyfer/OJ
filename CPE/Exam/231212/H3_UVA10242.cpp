#include <bits/stdc++.h>
using namespace std;
#define endl "\n"

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    double x1, y1, x2, y2, x3, y3, x4, y4;
    while (cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4) {
        double x = 0, y = 0;
        if (x1 == x3 && y1 == y3) { // 重複點是p1, p3
            x = x2 + x4 - x1;
            y = y2 + y4 - y1;
        } else if (x1 == x4 && y1 == y4) { // 重複點是p1, p4
            x = x2 + x3 - x1;
            y = y2 + y3 - y1;
        } else if (x2 == x3 && y2 == y3) { // 重複點是p2, p3
            x = x1 + x4 - x2;
            y = y1 + y4 - y2;
        } else if (x2 == x4 && y2 == y4) { // 重複點是p2, p4
            x = x1 + x3 - x2;
            y = y1 + y3 - y2;
        }
        cout << fixed << setprecision(3) << x << " " << y << endl;
    }
    return 0;
}