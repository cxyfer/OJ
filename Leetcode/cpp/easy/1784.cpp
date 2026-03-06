/*
 * @lc app=leetcode id=1784 lang=cpp
 *
 * [1784] Check if Binary String Has at Most One Segment of Ones
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution1 {
public:
    bool checkOnesSegment(string s) {
        return ranges::fold_left(views::pairwise(s), 0, [](int acc, auto pair) {
            auto [x, y] = pair;
            return acc + (x != y ? 1 : 0);
        }) <= 1;
    }
};

class Solution2 {
public:
    bool checkOnesSegment(string s) {
        return s.find("01") == string::npos;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

