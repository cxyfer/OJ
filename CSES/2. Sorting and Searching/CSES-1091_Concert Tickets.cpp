/*
    Binary Search + Multiset
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, x;
    cin >> n >> m;
    multiset<int> tickets;
    for (int i = 0; i < n; i++) {
        cin >> x;
        tickets.insert(x);
    }
    for (int i = 0; i < m; i++) {
        cin >> x;
        auto it = tickets.upper_bound(x);
        if (it == tickets.begin()) {
            cout << -1 << endl;
        } else {
            it--;
            cout << *it << endl;
            tickets.erase(it);
        }
    }
    return 0;
}