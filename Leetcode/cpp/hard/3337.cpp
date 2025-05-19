/*
 * @lc app=leetcode.cn id=3337 lang=cpp
 * @lcpr version=30204
 *
 * [3337] 字符串转换后的长度 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
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

class Solution {
public:
    int lengthAfterTransformations(string s, int t, vector<int>& nums) {
        vector<int> cnt(26, 0);
        for (char ch : s) cnt[ch - 'a']++;

        Matrix<LL> M(26, 26);
        for (int i = 0; i < 26; ++i)
            for (int k = 1; k <= nums[i]; ++k)
                M[i][(i + k) % 26] = 1;
 
        Matrix<LL> x(26, 1);
        for (int i = 0; i < 26; ++i) x[i][0] = 1;
        
        Matrix<LL> f = M.mul_pow(t, x);  // M^t * x
        LL ans = 0;
        for (int i = 0; i < 26; ++i) ans = (ans + f[i][0] * cnt[i]) % MOD;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abcyy"\n2\n[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]\n
// @lcpr case=end

// @lcpr case=start
// "azbk"\n1\n[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]\n
// @lcpr case=end

 */
