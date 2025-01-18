/*
 * @lc app=leetcode.cn id=3200 lang=cpp
 *
 * [3200] 三角形的最大高度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int maxHeightOfTriangle(int red, int blue) {
        function<int(int, int)> check = [&](int x, int y) -> int {
            int cur = 1;
            while (x > 0 || y > 0) {
                if (cur & 1) {
                    if (x >= cur) {
                        x -= cur;
                    } else {
                        break;
                    }
                } else {
                    if (y >= cur) {
                        y -= cur;
                    } else {
                        break;
                    }
                }
                cur += 1;
            }
            return cur - 1;
        };
        return max(check(red, blue), check(blue, red));
    }
};

class Solution2 {
public:
    int maxHeightOfTriangle(int red, int blue) {
        function<int(int, int)> check = [&](int x, int y) -> int {
            int t1 = floor(sqrt(x));
            int t2 = floor((-1 + sqrt(1 + 4 * y)) / 2);
            return t1 > t2 ? t2 << 1 | 1 : t1 << 1;
        };
        return max(check(red, blue), check(blue, red));
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// @lc code=end

