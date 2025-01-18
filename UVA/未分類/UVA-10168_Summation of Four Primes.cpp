#include <bits/stdc++.h>
using namespace std;
const int N = 1e7 + 5;
#define endl '\n'

/*
哥德巴赫猜想：
任一大於2的偶數，都可表示成兩個質數之和。
*/

bool inited = false;
vector<bool> is_prime;
vector<int> primes;
void init() {
    if (inited) return;
    inited = true;
    is_prime.resize(N, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i < N; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * i; j < N; j += i) is_prime[j] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    init();
    int n;
    while (cin >> n) {
        if (n < 8) {
            cout << "Impossible." << endl;
            continue;
        }
        int f1, f2, f3, f4;
        if (n & 1) {
            f1 = 2, f2 = 3;
            n -= 5;
        } else {
            f1 = 2, f2 = 2;
            n -= 4;
        }
        for (int p : primes) {
            if (p >= n) break;
            if (n - p > 0 && is_prime[n - p]) {
                f3 = p, f4 = n - p;
                break;
            }
        }
        cout << f1 << " " << f2 << " " << f3 << " " << f4 << endl;
    }
    return 0;
}