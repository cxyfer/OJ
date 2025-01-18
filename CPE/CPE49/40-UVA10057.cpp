#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x, y, z;
    while (cin >> n) {
        vector<int> A(n);
        for (auto &x: A) cin >> x;
        sort(A.begin(), A.end());
        if (n & 1){
            x = A[n / 2];
            y = 0;
            for (auto &a: A) y += (a == x); 
            z = 1;
        } else {
            x = A[n / 2 - 1];
            y = 0;
            for (auto &a: A) y += (a == x || a == A[n / 2]);
            z = A[n / 2] - A[n / 2 - 1] + 1;
        }
        cout << x << " " << y << " " << z << endl;
    }
    return 0;
}