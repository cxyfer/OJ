/*
 * @lc app=leetcode.cn id=2311 lang=cpp
 * @lcpr version=30204
 *
 * [2311] 小于等于 K 的最长二进制子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int BITS = 30;

class Solution1 {
public:
    int longestSubsequence(string s, int k) {
        int n = s.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            if (s[n - i - 1] == '1') {
                if (i > BITS || (1 << i) > k) continue;
                k -= 1 << i;
            }
            ans++;
        }
        return ans;
    }
};

class Solution2 {
public:
    int longestSubsequence(string s, int k) {
        int n = s.size(), ans = n;
        for (int i = 0; i < n; i++) {
            if (s[n - i - 1] == '1') {
                if (i > BITS || (1 << i) > k) {
                    ans -= count(s.begin(), s.begin() + n - i, '1');
                    break;
                }
                k -= 1 << i;
            }
        }
        return ans;
    }
};

class Solution3 {
public:
    int longestSubsequence(string s, int k) {
        int n = s.size(), ans = n;
        int v = 0;
        for (int i = max(n - BITS, 0); i < n; i++)
            v |= (s[i] == '1') << (n - i - 1);
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                if (n - i - 1 >= BITS) ans--;
                else if (v <= k) break;
                else v ^= 1 << (n - i - 1), ans--;
            }
        }
        return ans;
    }
};

// using Solution = Solution1;
// using Solution = Solution2;
using Solution = Solution3;
// @lc code=end

/*
// @lcpr case=start
// "1001010"\n5\n
// @lcpr case=end

// @lcpr case=start
// "00101001"\n1\n
// @lcpr case=end

 */

