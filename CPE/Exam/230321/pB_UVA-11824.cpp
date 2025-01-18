#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MAX = 5e6;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        vector<LL> arr;
        LL x;
        while (cin >> x && x) {
            arr.push_back(x);
        }
        sort(arr.begin(), arr.end(), greater<LL>());
        LL cost = 0;
        for (int i = 0; i < arr.size(); i++) {
            LL cur = 1;
            for (int j = 0; j <= i; j++) {
                cur *= arr[i];
            }
            cost += 2 * cur;
        }
        cout << (cost <= MAX ? to_string(cost) : "Too expensive") << endl;
    }
    return 0;
}