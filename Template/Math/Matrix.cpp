#include <bits/stdc++.h>
using namespace std;

// Matrix exponentiation by squaring

using LL = long long;
const int MOD = 1e9 + 7;

template <typename T>
class Matrix {
public:
    vector<vector<T>> mat;
    int rows, cols;

    Matrix() : rows(0), cols(0) {}

    Matrix(int r, int c, bool is_identity = false) : rows(r), cols(c) {
        mat.resize(r, vector<T>(c, 0));
        if (is_identity) {
            assert(r == c);
            for (int i = 0; i < r; ++i)
                mat[i][i] = 1;
        }
    }

    Matrix(const vector<vector<T>>& m) : mat(m) {
        rows = m.size();
        cols = m.empty() ? 0 : m[0].size();
    }

    Matrix operator*(const Matrix& other) const {
        assert(cols == other.rows);
        Matrix res(rows, other.cols);
        for (int i = 0; i < rows; ++i)
            for (int k = 0; k < cols; ++k) {
                if (mat[i][k] == 0) continue;
                for (int j = 0; j < other.cols; ++j)
                    res.mat[i][j] = (res.mat[i][j] + mat[i][k] * other.mat[k][j]) % MOD;
            }
        return res;
    }

    Matrix pow(LL k) const {
        assert(rows == cols);
        Matrix res(rows, cols, true);
        Matrix base = *this;
        while (k > 0) {
            if (k & 1)
                res = res * base;
            base = base * base;
            k >>= 1;
        }
        return res;
    }

    Matrix mul_pow(LL k, Matrix x) const {
        assert(cols == x.rows);
        
        Matrix res = x;
        Matrix base = *this;
        while (k > 0) {
            if (k & 1)
                res = base * res;
            base = base * base;
            k >>= 1;
        }
        return res;
    }

    vector<T>& operator[](int i) {
        return mat[i];
    }
};