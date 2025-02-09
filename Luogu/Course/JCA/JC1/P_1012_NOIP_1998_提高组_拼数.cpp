#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end(), [](const string &a, const string &b) {
        return a + b > b + a;
    });
    for (const auto &s : a) {
        cout << s;
    }
    cout << endl;
    return 0;
}