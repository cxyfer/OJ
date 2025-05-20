/*
 * @lc app=leetcode.cn id=3362 lang=cpp
 * @lcpr version=30204
 *
 * [3362] 零数组变换 III
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), m = queries.size();
        vector<int> diff(n + 1);
        // 按照左端點排序
        sort(queries.begin(), queries.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        // Max Heap 保存右端點
        priority_queue<int> hp;
        int s = 0, k = 0;
        for (int i = 0; i < n; ++i) {
            // 累加差分
            s += diff[i];
            // 將所有左端點在 i 之前的 queries 加入堆中
            while (k < m && queries[k][0] <= i)
                hp.push(queries[k++][1]);
            // 如果需要額外的 queries，則選擇能覆蓋更多未考慮位置的 query
            while (s < nums[i] && !hp.empty()) {
                int r = hp.top(); hp.pop();
                if (r >= i) {
                    s++;
                    diff[r + 1]--;
                }
            }
            // 如果無法滿足 nums[i] 的數量，則返回 -1
            if (s < nums[i])
                return -1;
        }
        // 最後 hp 的大小即為最多可以刪除的 queries 數量
        return hp.size();
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,0,2]\n[[0,2],[0,2],[1,1]]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1]\n[[1,3],[0,2],[1,3],[1,2]]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n[[0,3]]\n
// @lcpr case=end

 */

