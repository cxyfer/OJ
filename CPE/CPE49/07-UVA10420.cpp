#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string country, line;
    int t;
    cin >> t;
    map<string, int> cnt; // sort by key
    while (t--) {
        cin >> country;
        cnt[country]++;
        getline(cin, line); // ignore the rest of the line
    }
    for (const auto &k : cnt) {
        cout << k.first << " " << k.second << endl;
    }
    return 0;
}