#include <bits/stdc++.h>
using namespace std;
const int N = 101;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    // 質數判定：埃氏篩(Sieve of Eratosthenes)
    bool is_prime[N];
    fill(is_prime, is_prime + N, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i < N; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j < N; j += i) {
                is_prime[j] = false;
            }
        }
    }
    vector<int> primes;
    for (int i = 0; i < N; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
        }
    }
    // Bottom-up DP
    int num_p = primes.size();
    int ans[N][num_p];
    memset(ans, 0, sizeof(ans));
    for (int i = 2; i < N; i++) {
        int tmp = i;
        for (int j = 0; j < num_p; j++) {
            ans[i][j] = ans[i - 1][j];
            if (tmp == 1) {
                continue;
            }
            while (tmp % primes[j] == 0) {
                ans[i][j]++;
                tmp /= primes[j];
            }
        }
    }
    // Output
    while (cin >> n && n) {
        cout << setw(3) << n << "! =";
        int idx = -1;
        for (int i = 0; i < num_p; i++) {
            if (ans[n][i] != 0) idx = i;
        }
        for (int i = 0; i <= idx; i++) {
            if (i > 0 and i % 15 == 0) {
                cout << endl << "      ";
            }
            cout << setw(3) << ans[n][i];
        }
        cout << endl;
    }
    return 0;
}