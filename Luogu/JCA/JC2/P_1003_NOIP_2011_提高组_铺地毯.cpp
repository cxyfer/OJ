#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Carpet {
    int a, b, g, k;
    Carpet() : a(0), b(0), g(0), k(0) {}
    Carpet(int a, int b, int g, int k) : a(a), b(b), g(g), k(k) {}
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<Carpet> carpets(n);
    for (auto &carpet : carpets) {
        cin >> carpet.a >> carpet.b >> carpet.g >> carpet.k;
    }
    int x, y;
    cin >> x >> y;
    for (int i = n - 1; i >= 0; --i) {
        auto &carpet = carpets[i];
        if (carpet.a <= x && x <= carpet.a + carpet.g && carpet.b <= y && y <= carpet.b + carpet.k) {
            cout << i + 1 << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}