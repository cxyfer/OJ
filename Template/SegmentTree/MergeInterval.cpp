/*
    3187. Peaks in Array
    3161. Block Placement Queries
*/
#include <bits/stdc++.h>
using namespace std;

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