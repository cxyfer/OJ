/*
 * @lc app=leetcode id=3187 lang=cpp
 *
 * [3187] Peaks in Array
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

class FenwickTree { // PURQ (Point Update Range Query), 1-based, initialization: O(n)
private:
    int n = 0;
    vector<int> tree;
public:
    vector<int> nums;
    FenwickTree(vector<int>& nums) {
        n = nums.size();
        this->nums = nums;
        tree = vector<int>(n + 1); // 1-based
        for (int i = 1; i <= n; i++) { // initialization: O(n)
            tree[i] += nums[i-1];
            int nxt = i + (i & -i); // 下一個關鍵區間的右端點
            if (nxt <= n) {
                tree[nxt] += tree[i];
            }
        }
    }

    void add(int k, int x) { // 令 nums[k] += x
        for (int i = k+1; i < tree.size(); i += i & -i) {
            tree[i] += x;
        }
    }

    void update(int k, int x) { // 令 nums[k] = x
        add(k, x - nums[k]);
        this->nums[k] = x;
    }

    int sum(int l, int r) { // 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        if (l > r) return 0; // 本題中會出現 l > r 的情況
        return preSum(r+1) - preSum(l);
    }

    int preSum(int k) { // 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        int s = 0;
        for (int i = k; i > 0; i -= i & -i) {
            s += tree[i];
        }
        return s;
    }
};
class Solution1 {
public:
    vector<int> countOfPeaks(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> peaks(n, 0);
        for (int i = 1; i < n-1; i++)
            if (nums[i-1] < nums[i] && nums[i] > nums[i+1])
                peaks[i] = 1;
        FenwickTree bit(peaks);
        vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int l = q[1], r = q[2];
                ans.push_back(bit.sum(l+1, r-1)); // 不包含頭尾
            } else {
                int idx = q[1], val = q[2];
                nums[idx] = val;
                for (int i = idx-1; i <= idx+1; i++) { // 更新 idx-1, idx, idx+1 三個位置
                    if (i <= 0 || i >= n-1) continue;
                    if (nums[i-1] < nums[i] && nums[i] > nums[i+1]) { // 現在是峰值
                        if (bit.nums[i] == 0) // 之前不是峰值
                            bit.update(i, 1);
                    } else { // 現在不是峰值
                        if (bit.nums[i] == 1) // 之前是峰值
                            bit.update(i, 0);
                    }
                }
            }
        }
        return ans;
    }
};

class SegmentTree {
private:
    vector<int> nums;
    vector<int> tree;
public:
    SegmentTree(vector<int>& nums) {
        int n = nums.size();
        this->nums = vector<int>(n + 1, 0);
        for (int i = 1; i <= n; i++) this->nums[i] = nums[i - 1]; // 1-indexed
        this->tree = vector<int>(4 * n, 0);
        build(1, 1, n);
    }

    void build(int o, int left, int right) {
        if (left == right) {
            tree[o] = 0;
            return;
        }
        int mid = (left + right) / 2;
        build(2 * o, left, mid);
        build(2 * o + 1, mid + 1, right);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1], left, mid, right);
    }

    int merge(int l, int r, int left, int mid, int right) {
        int res = l + r;
        if (mid - 1 >= left && nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1] ||
            mid + 2 <= right && nums[mid] < nums[mid+1] && nums[mid+1] > nums[mid+2])
            res += 1;
        return res;
    }

    void update(int o, int left, int right, int idx, int val) {
        if (left == right) {
            nums[idx] = val;
            tree[o] = 0;
            return;
        }
        int mid = (left + right) / 2;
        if (idx <= mid) update(2 * o, left, mid, idx, val);
        else update(2 * o + 1, mid + 1, right, idx, val);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1], left, mid, right);
    }

    int query(int o, int left, int right, int l, int r) {
        if (left == l && r == right) return tree[o];
        int mid = (left + right) / 2;
        if (r <= mid) return query(2 * o, left, mid, l, r);  // 只需要查詢左半部分
        if (mid < l) return query(2 * o + 1, mid + 1, right, l, r);  // 只需要查詢右半部分
        int left_part = query(2 * o, left, mid, l, mid);  // 左半部分
        int right_part = query(2 * o + 1, mid + 1, right, mid + 1, r);  // 右半部分
        return merge(left_part, right_part, l, mid, r);  // 合併左右兩部分
    }
};

class Solution2 {
public:
    vector<int> countOfPeaks(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        SegmentTree seg(nums);
        vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int l = q[1], r = q[2];
                ans.push_back(seg.query(1, 1, n, l+1, r+1));
            } else {
                int idx = q[1], val = q[2];
                seg.update(1, 1, n, idx+1, val);
            }
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> nums = {9,9,7,7};
    vector<vector<int>> queries = {{1,1,2},{1,2,3},{2,0,6},{2,2,3},{2,0,9},{2,2,8},{1,0,2}};
    vector<int> ans = sol.countOfPeaks(nums, queries);
    for (int i = 0; i < ans.size(); i++) cout << ans[i] << "\t\n"[i==ans.size()-1]; // [0,0,0]
    return 0;
}
