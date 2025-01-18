#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL S, D, left, right, mid;
    while (cin >> S >> D) {
        left = 0, right = 1e9;
        while (left <= right) {
            mid = (left + right) / 2;
            if ((2 * S + mid) * (mid + 1) / 2 >= D) right = mid - 1;
            else left = mid + 1;
        }
        cout << S + left << endl;
    }
    return 0;
}