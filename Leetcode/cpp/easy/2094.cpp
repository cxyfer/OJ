/*
 * @lc app=leetcode.cn id=2094 lang=cpp
 * @lcpr version=30204
 *
 * [2094] 找出 3 位偶数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> cnt(10);
        for (auto x : digits) cnt[x]++;
        vector<int> ans;
        for (int i = 100; i <= 999; i += 2) {
            int a = i / 100, b = i / 10 % 10, c = i % 10;
            cnt[a]--; cnt[b]--; cnt[c]--;
            if (cnt[a] >= 0 && cnt[b] >= 0 && cnt[c] >= 0)
                ans.push_back(i);
            cnt[a]++; cnt[b]++; cnt[c]++;
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> cnt(10);
        for (auto x : digits) cnt[x]++;

        vector<int> ans;
        auto dfs = [&](this auto &&dfs, int i, int x) -> void {
            if (i == 3) {
                if (x % 2 == 0) ans.push_back(x);
                return;
            }
            for (int j = 0; j < 10; j++) {
                if (i == 0 && j == 0 || cnt[j] <= 0) continue;
                cnt[j]--;
                dfs(i + 1, x * 10 + j);
                cnt[j]++;
            }
            return;
        };
        dfs(0, 0);
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [2,1,3,0]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,8,8,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,7,5]\n
// @lcpr case=end

 */

