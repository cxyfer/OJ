#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL MAXN = 1e12;
const LL MAXN_SQRT = sqrt(MAXN);
#define endl '\n'
#define all(x) x.begin(), x.end()

vector<LL> almost_primes;
vector<bool> is_prime(MAXN_SQRT + 1, true);

void init() {
    is_prime[0] = is_prime[1] = false;
    for (LL i = 2; i * i <= MAXN_SQRT; i++) {
        if (is_prime[i]) {
            for (LL j = i * i; j <= MAXN_SQRT; j += i) {
                is_prime[j] = false;
            }
        }
    }
    for (LL i = 2; i <= MAXN_SQRT; i++) {
        if (is_prime[i]) {
            LL x = i * i;
            while (x <= MAXN) {
                almost_primes.push_back(x);
                x *= i;
            }
        }
    }
    sort(all(almost_primes));
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    init();
    int t;
    cin >> t;
    while (t--) {
        LL lo, hi;
        cin >> lo >> hi;
        cout << upper_bound(all(almost_primes), hi) - lower_bound(all(almost_primes), lo) << endl;
    }
    return 0;
}