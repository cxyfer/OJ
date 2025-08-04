/*
 * @lc app=leetcode.cn id=904 lang=cpp
 * @lcpr version=30204
 *
 * [904] 水果成篮
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1a {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();
        unordered_map<int, int> cnt;
        int ans = 0, left = 0;
        for (int right = 0; right < n; ++right) {
            cnt[fruits[right]]++;
            while (cnt.size() > 2) {
                cnt[fruits[left]]--;
                if (cnt[fruits[left]] == 0) cnt.erase(fruits[left]);
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};

class Solution1b {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();
        vector<int> cnt(n + 1);
        int ans = 0, left = 0, tot = 0;
        for (int right = 0; right < n; ++right) {
            if (++cnt[fruits[right]] == 1) tot++;
            while (tot > 2)
                if (--cnt[fruits[left++]] == 0) tot--;
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};

// using Solution = Solution1a;
using Solution = Solution1b;
// @lc code=end



/*
// @lcpr case=start
// [1,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,3,3,1,2,1,1,2,3,3,4]\n
// @lcpr case=end

 */

