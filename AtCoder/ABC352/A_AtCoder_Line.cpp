#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N, X, Y, Z;
    cin >> N >> X >> Y >> Z;
    if (X > Y) swap(X, Y);
    cout << (X <= Z && Z <= Y ? "Yes" : "No") << endl;
    return 0;
}
