#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;
#define endl '\n'

int digit_sum(int n) {
    int res = 0;
    while (n > 0) {
        res += n % 10;
        n /= 10;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    vector<bool> is_prime(N, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i < N; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j < N; j += i) {
                is_prime[j] = false;
            }
        }
    }
    vector<int> s(N, 0);
    for (int i = 2; i < N; i++) {
        if (is_prime[i] && is_prime[digit_sum(i)]) {
            s[i] = s[i - 1] + 1;
        } else {
            s[i] = s[i - 1];
        }
    }
    int t, l, r;
    cin >> t;
    while (t--) {
        cin >> l >> r;
        cout << s[r] - s[l - 1] << endl;
    }
    return 0;
}