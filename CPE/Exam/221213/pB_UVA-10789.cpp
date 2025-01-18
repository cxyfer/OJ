#include <bits/stdc++.h>
using namespace std;
const int N = 2005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    // Sieve of Eratosthenes
    bool is_prime[N];
    memset(is_prime, 1, sizeof(is_prime));
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i < N; i++) {
        if (is_prime[i]) {
            for (int j = i*i; j < N; j += i) {
                is_prime[j] = false;
            }
        }
    }
    // Main
    int t, kase=1; cin >> t;
    while (t--) {
        string s; cin >> s;
        map<char, int> cnt;
        for (char c : s) cnt[c]++;
        vector<char> ans;
        for (auto const &x : cnt){
            if (is_prime[x.second]) ans.push_back(x.first);
        }
        cout << "Case " << kase++ << ": " << (ans.empty() ? "empty" : string(ans.begin(), ans.end())) << endl;
    }
    return 0;
}