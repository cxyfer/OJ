/*
 * @lc app=leetcode.cn id=3258 lang=cpp
 *
 * [3258] 统计满足 K 约束的子字符串数量 I
 */

// @lc code=start
class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        int n = s.size();
        int ans = 0, left = 0;
        vector<int> cnt(2, 0);
        for (int right = 0; right < n; right++) {
            cnt[s[right] - '0']++;
            while (cnt[0] > k && cnt[1] > k) {
                cnt[s[left] - '0']--;
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }
};
// @lc code=end

