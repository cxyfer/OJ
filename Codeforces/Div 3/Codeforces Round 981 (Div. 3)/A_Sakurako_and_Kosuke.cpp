/*
    模擬 / 奇偶性
    由於 n <= 100，因此可以直接模擬。
    但可以觀察到 Sakurako 會讓值變成負的奇數；而 Kosuke 會讓值變成正的偶數，
    因此可以直接判斷奇偶性即可。
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        cout << (n & 1 ? "Kosuke" : "Sakurako") << endl;
    }
    return 0;
}