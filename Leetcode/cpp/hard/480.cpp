/*
 * @lc app=leetcode.cn id=480 lang=cpp
 *
 * [480] 滑动窗口中位数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        1. Multiset + Binart Search

        2. Two Heaps + Hash Table + Lazy Deletion
        Extended from 295. Find Median from Data Stream
        由於窗口大小固定為 k ，因此可以使用 Lazy Deletion 來實現刪除操作
        但這樣會讓我們不能單純用左右兩個堆的大小來判斷插入時的位置，
        不過在窗口大小固定後，左右兩邊的實際大小就固定了，可以從被刪除的數字的所在的位置來判斷插入的位置。
        Time: O(nlogk)
    */
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        // return solve1(nums, k);
        return solve2(nums, k);
    }
    vector<double> solve1(vector<int>& nums, int k) {
        int n = nums.size();
        vector<double> ans;
        multiset<int> st(nums.begin(), nums.begin() + k); // 初始化大小為 K 的窗口
        auto mid = next(st.begin(), k / 2); // 每次都用 next 找中位數會 TLE，所以用 iterator 來記錄
        for (int r = k; r <= n; r++) {
            double median = ((double)(*mid) + (double)(*prev(mid, 1 - k % 2))) / 2;
            ans.push_back(median);
            if (r == n) break;
            st.insert(nums[r]);
            if (nums[r] < *mid) mid--; // 左邊多一個數字，左移指標
            if (nums[r - k] <= *mid) mid++; // 左邊少一個數字，右移指標
            st.erase(st.lower_bound(nums[r - k])); // 用 Binary Search 找到要刪除的數字
        }
        return ans;
    }
    vector<double> solve2(vector<int>& nums, int k) {
        int n = nums.size();
        vector<double> ans;
        priority_queue<int> l; // max heap，保存 <= median 的數字
        priority_queue<int, vector<int>, greater<int>> r; // min heap，保存 > median 的數字
        unordered_map<int, int> cnt; // Lazy deletion，保存要刪除的數字及其應該刪除的次數

        auto get_median = [&]() {
            // Lazy deletion，若堆頂的數字已經被標記為刪除，則刪除
            while (!l.empty() && cnt[l.top()] > 0) {
                cnt[l.top()]--; 
                l.pop();
            }
            while (!r.empty() && cnt[r.top()] > 0) {
                cnt[r.top()]--; 
                r.pop();
            }
            return k & 1 ? l.top() : ((long long) l.top() + r.top()) / 2.0; // 窗口大小固定為 k ，以其奇偶性來判斷中位數
        };

        auto insert = [&](int num, bool toLeft) {
            if (toLeft) {
                r.push(num); 
                l.push(r.top());
                r.pop();
            }
            else {
                l.push(num); 
                r.push(l.top());
                l.pop();
            }
        };
        for (int i = 0; i < k; i++) { // 初始化窗口
            insert(nums[i], l.size() == r.size()); // 根據當前數量為偶數/奇數，加入到左邊/右邊
        }
        ans.push_back(get_median());
        for (int i = k; i < n; i++) {
            cnt[nums[i - k]]++; // 出窗口，標記為刪除
            insert(nums[i], nums[i - k] <= l.top()); // 根據被刪除的數字在左邊還是右邊，插入新的數字到同側
            ans.push_back(get_median());
        }
        return ans;
    }
};
// @lc code=end
