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
            tree[o] = nums[left];
            return;
        }
        int mid = (left + right) / 2;
        build(2 * o, left, mid);
        build(2 * o + 1, mid + 1, right);
        tree[o] = merge(2 * o, 2 * o + 1);
    }

    int merge(int left_child, int right_child) {
        return tree[left_child] & tree[right_child];
    }

    int query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        int ans = (1 << 30) - 1;
        if (l <= mid) ans &= query(2 * o, left, mid, l, r);
        if (r > mid) ans &= query(2 * o + 1, mid + 1, right, l, r);
        return ans;
    }
};

class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        SegmentTree seg(nums);
        int ans = (1 << 30) - 1;
        for (int i = 1; i <= n; i++) {
            int left = i, right = n;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (seg.query(1, 1, n, i, mid) >= k) left = mid + 1;
                else right = mid - 1;
            }
            ans = min(ans, abs(seg.query(1, 1, n, i, left) - k));
            if (right != 0) ans = min(ans, abs(k - seg.query(1, 1, n, i, right)));
        }
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 4, 5};
    cout << sol.minimumDifference(nums, 3) << endl; // 1
    nums = {1, 2, 1, 2};
    cout << sol.minimumDifference(nums, 2) << endl; // 0
    nums = {1};
    cout << sol.minimumDifference(nums, 10) << endl; // 9
    nums = {5, 13, 90, 92, 49};
    cout << sol.minimumDifference(nums, 10) << endl; // 2
}