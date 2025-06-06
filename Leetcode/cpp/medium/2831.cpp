/*
 * @lc app=leetcode.cn id=2831 lang=cpp
 *
 * [2831] 找出最长等值子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Sliding window
        
        首先紀錄每個元素出現的位置，pos[x] 為元素 x 出現的位置列表，列表中的元素為該元素在原陣列中的下標。
        接著枚舉每個元素 x ，以該元素為窗口的左右邊界，根據題意，窗口內最多只有 k 個元素與當前枚舉的元素 x 不同
        令 left, right 為窗口的左右邊界，指向 pos[x] 之下標
        - 則 pos[x][right] - pos[x][left] + 1 為目前窗口在原陣列中的長度
        - right - left + 1 為目前窗口內元素 x 的數量
        - 兩者相減，即為窗口內非 x 元素的數量，也就是需要刪除的元素數量
    */
    int longestEqualSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> pos(n + 1); // 紀錄每個元素出現的位置，1 <= nums[i] <= nums.length
        for (int i = 0; i < n; i++) { 
            pos[nums[i]].push_back(i);
        }
        int ans = 0;
        for (int x = 1; x <= n; x++){
            if (pos[x].empty()) continue; // 若元素 x 不存在，則跳過
            int left = 0; // left, right 為窗口的左右邊界，是 pos[x] 中的下標
            for (int right = 0; right < pos[x].size(); right++) {
                while ((pos[x][right] - pos[x][left] + 1) - (right - left + 1) > k) { // 若不符合條件，則開始縮小窗口
                    left++;
                }
                ans = max(ans, right - left + 1); // 更新答案
            }
        }
        return ans;
    }
};
// @lc code=end

