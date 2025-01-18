/*
 * @lc app=leetcode.cn id=1103 lang=cpp
 *
 * [1103] 分糖果 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        int n = num_people;
        vector<int> ans(n, 0);
        int i = 0;
        while (candies > 0) {
            ans[i % n] += min(candies, i + 1);
            candies -= i + 1;
            i++;
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        int n = num_people;
        int m = (-1 + sqrt(8.0 * candies + 1.0)) / 2;
        int q = m / n, r = m % n;
        vector<int> ans(n, 0);
        for (int i = 0; i < n; i++) {
            ans[i] = q * (q - 1) / 2 * n + q * (i + 1);
            if (i < r) ans[i] += q * n + i + 1;
            else if (i == r) ans[i] += candies - m * (m + 1) / 2;
        }
        return ans;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// @lc code=end

