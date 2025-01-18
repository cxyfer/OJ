#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class Matrix {
public:
    int a, b, c, d, mask;
    Matrix(int a, int b, int c, int d, int mask) : a(a), b(b), c(c), d(d), mask(mask) {}
    Matrix operator*(const Matrix &other) {
        return Matrix(
            (a * other.a + b * other.c) & mask,
            (a * other.b + b * other.d) & mask,
            (c * other.a + d * other.c) & mask,
            (c * other.b + d * other.d) & mask,
            mask
        );
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    while (cin >> n >> m) {
        Matrix M(1, 1, 1, 0, (1 << m) - 1);
        Matrix X(1, 0, 0, 0, (1 << m) - 1);
        while (n) {
            if (n & 1) X = X * M;
            M = M * M;
            n >>= 1;
        }
        cout << X.b << endl;
    }
    return 0;
}