/*
 * @lc app=leetcode.cn id=239 lang=cpp
 * @lcpr version=30204
 *
 * [239] 滑动窗口最大值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * 1. Max Heap + Lazy Deletion : O(nlogn)
 * 使用 Max Heap 維護窗口內的元素，並且使用 Lazy Deletion 來刪除不在窗口內的元素

 * 2. Monotonic queue : O(n)
 * 使用 deque 保存 index，並且保證 deque 中的元素是遞增的
 * 如果新的元素比 deque 中的某些元素大，那麼這些元素永遠不可能成為最大值，因此將其從 deque 中刪除
 */
// @lc code=start
class Solution1 {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        priority_queue<pair<int, int>> pq;  // Max Heap，維護窗口內的元素
        for (int i = 0; i < k; i++) pq.emplace(nums[i], i);
        vector<int> ans;
        ans.push_back(pq.top().first);
        for (int i = k; i < n; i++) {
            pq.emplace(nums[i], i);
            while (pq.top().second <= i - k) pq.pop();
            ans.push_back(pq.top().first);
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        deque<int> dq;  // 從大到小的 Monotonic queue, 保存的是 index
        for (int i = 0; i < n; i++) {
            // 1. 插入，從 tail 移除比 nums[i] 小的數
            while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
            dq.push_back(i);
            // 2. 維護窗口範圍
            while (dq.front() <= i - k) dq.pop_front();
            // 3. 更新答案
            if (i >= k - 1) ans.push_back(nums[dq.front()]);
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

/*
// @lcpr case=start
// [1,3,-1,-3,5,3,6,7]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

 */

