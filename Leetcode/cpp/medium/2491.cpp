/*
 * @lc app=leetcode.cn id=2491 lang=cpp
 *
 * [2491] 划分技能点相等的团队
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long dividePlayers(vector<int>& skill) {
        int n = skill.size();
        sort(skill.begin(), skill.end());
        int target = skill[0] + skill[n - 1];
        long long ans = 0;
        for (int i = 0; i < n / 2; i++) {
            if (skill[i] + skill[n - i - 1] != target) return -1;
            ans += (long long) skill[i] * skill[n - i - 1];
        }
        return ans;
    }
};

class Solution2 {
public:
    long long dividePlayers(vector<int>& skill) {
        int n = skill.size(), m = n / 2;
        int s = accumulate(skill.begin(), skill.end(), 0);
        if (s % m != 0) return -1;
        int target = s / m;
        unordered_map<int, int> cnt;
        for (int x : skill) cnt[x]++;
        long long ans = 0;
        for (auto [k, v] : cnt) {
            if (cnt[target - k] != v) return -1;
            ans += (long long) k * (target - k) * v;
        }
        return ans / 2;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> skill = {3, 2, 5, 1, 3, 4};
    cout << sol.dividePlayers(skill) << endl;
    return 0;
}