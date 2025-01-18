#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e7 + 5;
#define endl '\n'

bool inited = false;
vector<bool> is_prime(N, true);
vector<LL> primes;
void init() {
    if (inited) return;
    inited = true;
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i < N; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j < N; j += i) {
                is_prime[j] = false;
            }
        }
    }
    for (int i = 2; i < N; i++) {
        if (is_prime[i]) primes.push_back(i);
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    init();
    LL n;
    while (cin >> n && n) {
        if (n < 0) n = -n;
        LL ans = -1, cnt = 0;
        for (LL p : primes) {
            if (p * p > n) break;
            if (n % p == 0) {
                while (n % p == 0) n /= p;
                ans = p;
                cnt++;
            }
        }
        if (n > 1) ans = n, cnt++;  
        cout << (cnt > 1 ? ans : -1) << endl;
    }
    return 0;
}