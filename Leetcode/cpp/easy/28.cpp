/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 找出字符串中第一个匹配项的下标
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int strStr(string s, string t) {
        int n = s.size(), m = t.size();
        vector<int> pi(m);
        int ln = 0;
        for (int i = 1; i < m; i++) {
            while (ln && t[i] != t[ln])
                ln = pi[ln - 1];
            if (t[i] == t[ln])
                ln++;
            pi[i] = ln;
        }
        ln = 0;
        for (int i = 0; i < n; i++) {
            while (ln && s[i] != t[ln])
                ln = pi[ln - 1];
            if (s[i] == t[ln])
                ln++;
            if (ln == m)
                return i - m + 1;
        }
        return -1;
    }
};

class Solution2 {
private:
    const long long MOD = 1070777777;
    const long long BASE = []() {
        srand(time(0));
        return rand() % (int(1e9) - int(1e8)) + int(1e8);
    }();

public:
    int strStr(string s, string t) {
        int n = s.length(), m = t.length();
        if (n < m) return -1;

        // Rabin-Karp Rolling Hash
        vector<long long> P(m + 1, 1);  // P[i] = BASE^i % MOD
        vector<long long> H(m + 1, 0);  // H[i] = hash(s[:i])
        for (int i = 0; i < m; i++) {
            P[i + 1] = (P[i] * BASE) % MOD;
            H[i + 1] = (H[i] * BASE + t[i]) % MOD;
        }

        // Sliding window
        long long hs = 0;
        for (int i = 0; i < n; i++) {
            hs = (hs * BASE + s[i]) % MOD;  // add to window
            if (i >= m)  // remove from window, maintain window size m
                hs = (hs - s[i - m] * P[m] % MOD + MOD) % MOD;
            // compare hash and substring, if not consider collision, compare hash only
            if (i >= m - 1 && hs == H[m] && s.substr(i - m + 1, m) == t)
                return i - m + 1;
        }
        return -1;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

