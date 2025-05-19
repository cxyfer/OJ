/*
 * @lc app=leetcode.cn id=3335 lang=cpp
 * @lcpr version=30204
 *
 * [3335] 字符串转换后的长度 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int MOD = 1e9 + 7;

class Solution1 {
public:
    int lengthAfterTransformations(string s, int t) {
        array<int, 26> f, nf;
        for (char ch : s) f[ch - 'a']++;

        for (int i = 0; i < t; i++) {
            nf.fill(0);
            for (int j = 0; j < 26; j++) {
                if (j == 25) {
                    nf[0] = (nf[0] + f[j]) % MOD;
                    nf[1] = (nf[1] + f[j]) % MOD;
                } else {
                    nf[j + 1] = (nf[j + 1] + f[j]) % MOD;
                }
            }
            swap(f, nf);
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) ans = (ans + f[i]) % MOD;
        return ans;

    }
};

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

Matrix<LL> M(26, 26);
vector<Matrix<LL>> pow_M(32);
auto init = []() {
    for (int i = 0; i < 26; i++) {
        if (i == 25) {
            M[i][0] = 1;
            M[i][1] = 1;
        } else {
            M[i][i + 1] = 1;
        }
    }

    pow_M[0] = M;
    for (int i = 1; i < 32; i++)
        pow_M[i] = pow_M[i - 1] * pow_M[i - 1];
    return 0;
}();

class Solution2 {
public:
    int lengthAfterTransformations(string s, int t) {
        vector<int> cnt(26);
        for (char ch : s) cnt[ch - 'a']++;
        Matrix<LL> f(26, 1);
        for (int i = 0; i < 26; i++) f[i][0] = 1;
        int k = 0;
        while (t > 0) {
            if (t & 1) f = pow_M[k] * f;
            t >>= 1;
            k++;
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) ans = (ans + f[i][0] * cnt[i]) % MOD;
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

/*
// @lcpr case=start
// "abcyy"\n2\n
// @lcpr case=end

// @lcpr case=start
// "azbk"\n1\n
// @lcpr case=end

 */

