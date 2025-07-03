/*
 * @lc app=leetcode.cn id=3304 lang=cpp
 * @lcpr version=30204
 *
 * [3304] 找出第 K 个字符 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

#include <ranges>
class Solution1 {
public:
    char kthCharacter(int k) {
        string s = "a";
        while (s.size() < k) {
            s += s | views::transform([](char c) { return c + 1; })
                   | ranges::to<string>();
        }
        return s[k - 1];
    }
};

class Solution2a {
public:
    char kthCharacter(int k) {
        auto f = [&](this auto&& f, int k) {
            if (k == 1) return 0;
            int m = bit_width((uint64_t) k - 1);
            if (k < (1 << (m - 1))) return f(k);
            else return 1 + f(k - (1 << (m - 1)));
        };
        return 'a' + f(k);
    }
};

class Solution2b {
public:
    char kthCharacter(int k) {
        int m = bit_width((uint64_t) k - 1);
        int cnt = 0;
        for (int i = m - 1; i >= 0; --i) {
            if (k > (1 << i)) {
                k -= (1 << i);
                cnt++;
            }
        }
        return 'a' + cnt;
    }
};

class Solution2c {
public:
    char kthCharacter(int k) {
        int m = bit_width((uint64_t) k - 1);
        int cnt = 0;
        for (int i = m - 1; i >= 0; --i) {
            if ((k - 1) >> i) {
                k -= (1 << i);
                cnt++;
            }
        }
        return 'a' + cnt;
    }
};

class Solution3 {
public:
    char kthCharacter(int k) {
        return 'a' + __builtin_popcount(k - 1);
    }
};

// using Solution = Solution1;
// using Solution = Solution2a;
// using Solution = Solution2b;
using Solution = Solution2c;
// using Solution = Solution3;
// @lc code=end



/*
// @lcpr case=start
// 5\n
// @lcpr case=end

// @lcpr case=start
// 10\n
// @lcpr case=end

 */

