#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll calculate_string_operations(ll N, vector<string> strs) {
    unordered_map<string, ll> prefix;
    unordered_map<string, ll> suffix;

    for (string s : strs) {
        for (ll j = 1; j <= s.size(); ++j) {
            prefix[s.substr(0, j)] += 1;
        }
        for (ll j = s.size()-1; j >= 0; --j) {
            suffix[s.substr(j)] += 1;
        }
    }

    ll NN = 0;
    for (string s : strs) {
        NN += s.size();
    }

    ll ans = NN * (N*2);
    for (string s : strs) {
        for (ll j = 1; j <= s.size(); ++j) {
            string sub = s.substr(0, j);
            reverse(sub.begin(), sub.end());
            ans -= suffix[sub];
        }
        for (ll j = s.size()-1; j >= 0; --j) {
            string sub = s.substr(j);
            reverse(sub.begin(), sub.end());
            ans -= prefix[sub];
        }
    }

    return ans;
}

int main() {
    ll N;
    cin >> N;

    vector<string> strs(N);
    for (ll i = 0; i < N; ++i) {
        cin >> strs[i];
    }

    cout << calculate_string_operations(N, strs) << endl;

    return 0;
}