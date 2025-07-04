/*
 * @lc app=leetcode.cn id=3307 lang=cpp
 * @lcpr version=30204
 *
 * [3307] 找出第 K 个字符 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1a {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        auto f = [&](this auto&& f, long long k) {
            if (k == 1) return 0;
            int m = bit_width((uint64_t) k - 1);
            if (k < (1LL << (m - 1))) return f(k);
            else return operations[m - 1] + f(k - (1LL << (m - 1)));
        };
        return 'a' + f(k) % 26;
    }
};

class Solution1b {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        int m = bit_width((uint64_t) k - 1);
        int cnt = 0;
        for (int i = m - 1; i >= 0; --i) {
            if (k > (1LL << i)) {
                k -= (1LL << i);
                cnt += operations[i];
            }
        }
        return 'a' + cnt % 26;
    }
};

class Solution2 {
    public:
        char kthCharacter(long long k, vector<int>& operations) {
            int m = bit_width((uint64_t) k - 1);
            long long mask = 0;
            for (int i = 0; i < m; ++i)
                if (operations[i]) mask |= (1LL << i);
            return 'a' + __builtin_popcountll((k - 1) & mask) % 26;
        }
    };

// using Solution = Solution1a;
// using Solution = Solution1b;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// 5\n[0,0,0]\n
// @lcpr case=end

// @lcpr case=start
// 10\n[0,1,0,1]\n
// @lcpr case=end

 */

