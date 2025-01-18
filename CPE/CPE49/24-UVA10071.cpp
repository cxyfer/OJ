/*
    假設初速度為0，否則算不出來
    從v-t圖可以得在t秒內的位移為v*t/2，而在2t秒內的位移為v*t*2
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int v, t;
    while (cin >> v >> t) {
        cout << (v * t * 2) << endl;
    }
    return 0;
}