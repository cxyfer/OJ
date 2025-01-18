/*
 * @lc app=leetcode.cn id=633 lang=cpp
 *
 * [633] 平方数之和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;

class Solution1 {
public:
    bool judgeSquareSum(int c) {
        for (LL x = 0; x * x <= c; x++){
            double y = sqrt(c - x * x);
            if (y == (int)y){
                return true;
            }
        }
        return false;
    }
};

class Solution2 {
public:
    bool judgeSquareSum(int c) {
        LL l = 0, r = sqrt(c);
        while (l <= r){
            LL cur = l * l + r * r;
            if (cur == c){
                return true;
            } else if (cur > c){
                r--;
            } else {
                l++;
            }
        }
        return false;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end
