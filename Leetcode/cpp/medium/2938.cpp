/*
 * @lc app=leetcode.cn id=2938 lang=cpp
 *
 * [2938] 区分黑球与白球
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long minimumSteps(string s) {
        long long ans = 0;
        int left = 0, right = s.size() - 1;
        while (left < right) {
            while (left < right && s[left] == '0') left++;
            while (left < right && s[right] == '1') right--;
            if (left < right){
                ans += right - left;
                left++;
                right--;
            }
        }
        return ans;
    }
    long long solve2(string s) {
        int n = s.size(), cnt = 0;
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') cnt++;
            else ans += cnt;
        }
        return ans;
    }
};

class Solution2 {
public:
    long long minimumSteps(string s) {
        int n = s.size(), cnt = 0;
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') cnt++;
            else ans += cnt;
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

