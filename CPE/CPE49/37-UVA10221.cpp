#include <bits/stdc++.h>
using namespace std;
const double BASE = 6440.0;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    double s, a, radian, arc, chord;
    string typ;
    while (cin >> s >> a >> typ) {
        if (typ == "min") a /= 60;
        if (a > 180) a = 360 - a;
        radian = a * M_PI / 180.0; // or pi = acos(-1)
        arc = (BASE + s) * radian;
        chord = (BASE + s) * sin(radian / 2.0) * 2.0;
        cout << fixed << setprecision(6) << arc << " " << chord << endl;
    }
    return 0;
}