/*
 * @lc app=leetcode.cn id=2176 lang=cpp
 * @lcpr version=30204
 *
 * [2176] 统计数组中相等且可以被整除的数对
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int countPairs(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                ans += (nums[i] == nums[j]) && (i * j) % k == 0;
        return ans;
    }
};

const int MX = 105;
vector<vector<int>> divisors;
auto init = []() {
    divisors.resize(MX);
    for (int i = 1; i < MX; i++)
        for (int j = i; j < MX; j += i)
            divisors[j].push_back(i);
    return 0;
}();

class Solution2 {
public:
    int countPairs(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, unordered_map<int, int>> cnt;
        vector<int> divs = divisors[k];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += cnt[nums[i]][k / gcd(i, k)];
            for (int d : divs)
                if (i % d == 0) cnt[nums[i]][d]++;
        }
        return ans;
    }
};

using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [3,1,2,2,2,1,3]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n1\n
// @lcpr case=end

 */

