#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

bool cmp(pair<char, int> a, pair<char, int> b) {
    if (a.second == b.second) {
        return a.first < b.first;
    }
    return a.second > b.second;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    string s;
    
    cin >> t;
    unordered_map<char, int> cnt;
    getline(cin, s); // ignore the rest of the line

    while (t--) {
        getline(cin, s);
        for (char ch : s) {
            if (isalpha(ch)) {
                cnt[toupper(ch)]++;
            }
        }
    }
    // Convert map to a vector of pairs for sorting
    vector<pair<char, int>> cntVec(cnt.begin(), cnt.end());

    // Sort the vector based on the frequency and then alphabetically
    sort(cntVec.begin(), cntVec.end(), cmp);

    for (const auto &kv : cntVec) {
        cout << kv.first << " " << kv.second << endl;
    }
    return 0;
}