/*
 * @lc app=leetcode.cn id=3072 lang=cpp
 *
 * [3072] 将元素分配到两个数组中 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

/*
    1. Simulation + Binary Search
        每次查找跟插入都是 O(logn)，總共是 O(nlogn)
    2. Binary Indexed Tree (Fenwick Tree, BIT)
        Similar to 307. Range Sum Query - Mutable
        可以從模板修改而來，刪除初始化、update 方法、sum 方法
*/

class Solution1 {
public:
    vector<int> resultArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr1 = {nums[0]}, arr2 = {nums[1]}; // answer array
        vector<int> v1 = {nums[0]}, v2 = {nums[1]}; // sorted array
        for (int i = 2; i < n; i++) {
            int x = nums[i];
            int idx1 = upper_bound(v1.begin(), v1.end(), x) - v1.begin(), idx2 = upper_bound(v2.begin(), v2.end(), x) - v2.begin();
            int gc1 = arr1.size() - idx1, gc2 = arr2.size() - idx2;
            if (gc1 > gc2 || (gc1 == gc2 && arr1.size() <= arr2.size())) {
                arr1.push_back(x);
                v1.insert(v1.begin() + idx1, x);
            } else {
                arr2.push_back(x);
                v2.insert(v2.begin() + idx2, x);
            }
        }
        arr1.insert(arr1.end(), arr2.begin(), arr2.end());
        return arr1;
    }
};


class FenwickTree { // PURQ (Point Update Range Query), 0-based, initialization: O(nlogn)
private:
    int n = 0;
    vector<int> tree;
public:
    FenwickTree(int n) {
        this->n = n;
        tree = vector<int>(n, 0);
    }
    void add(int k, int x) { // 令 nums[k] += x
        for (int i = k+1; i <= n; i += i & -i) {
            tree[i-1] += x;
        }
    }
    int preSum(int k) { // 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        int res = 0;
        for (int i = k+1; i > 0; i -= i & -i) {
            res += tree[i-1];
        }
        return res;
    }
};

class Solution2 {
public:
    vector<int> resultArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> sorted_nums = nums; // 離散化
        sort(sorted_nums.begin(), sorted_nums.end());
        sorted_nums.erase(unique(sorted_nums.begin(), sorted_nums.end()), sorted_nums.end()); // 去重
        int m = sorted_nums.size();
        vector<int> arr1 = {nums[0]}, arr2 = {nums[1]};
        FenwickTree bit1(m+1), bit2(m+1);
        int idx1 = lower_bound(sorted_nums.begin(), sorted_nums.end(), nums[0]) - sorted_nums.begin();
        int idx2 = lower_bound(sorted_nums.begin(), sorted_nums.end(), nums[1]) - sorted_nums.begin();
        bit1.add(idx1, 1);
        bit2.add(idx2, 1);
        for (int i = 2; i < n; i++) {
            int idx = lower_bound(sorted_nums.begin(), sorted_nums.end(), nums[i]) - sorted_nums.begin();
            int gc1 = arr1.size() - bit1.preSum(idx); // bit1.preSum(v) 表示 <= v 的元素個數，故 len(arr1) - bit1.preSum(v) 表示 > v 的元素個數
            int gc2 = arr2.size() - bit2.preSum(idx);
            if (gc1 > gc2 || (gc1 == gc2 && arr1.size() <= arr2.size())) {
                arr1.push_back(nums[i]);
                bit1.add(idx, 1);
            } else {
                arr2.push_back(nums[i]);
                bit2.add(idx, 1);
            }
        }
        arr1.insert(arr1.end(), arr2.begin(), arr2.end());
        return arr1;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// @lc code=end

