/*
    Merge Interval 2 - Using Node structure
    3525. Find X Value of Array II
*/
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int prod;
    vector<int> cnt;
    Node(int prod, int k) : prod(prod), cnt(vector<int>(k, 0)) {}
};

class SegmentTree {
private:
    int n, k;
    vector<Node> tree;

public:
    SegmentTree(vector<int>& nums, int k) {
        this->n = nums.size();
        this->k = k;
        this->tree = vector<Node>(4 * n, Node(0, k));
        build(1, 1, n, nums);
    }

    void build(int o, int left, int right, vector<int>& nums) {
        if (left == right) {
            int prod = nums[left - 1] % k;
            tree[o].prod = prod;
            tree[o].cnt[prod] = 1;
            return;
        }
        int mid = left + (right - left) / 2;
        build(2 * o, left, mid, nums);
        build(2 * o + 1, mid + 1, right, nums);
        merge(tree[2 * o], tree[2 * o + 1], tree[o]);
    }

    // 直接修改 result，而非創建新的 Node
    void merge(Node& left, Node& right, Node& result) {
        result.prod = (left.prod * right.prod) % k;
        fill(result.cnt.begin(), result.cnt.end(), 0);
        for (int x = 0; x < k; x++) {
            result.cnt[x] += left.cnt[x];
            result.cnt[(left.prod * x) % k] += right.cnt[x];
        }
    }

    void update(int o, int left, int right, int idx, int val) {
        if (left == right) {
            int prod = val % k;
            tree[o].prod = prod;
            fill(tree[o].cnt.begin(), tree[o].cnt.end(), 0);
            tree[o].cnt[prod] = 1;
            return;
        }
        int mid = left + (right - left) / 2;
        if (idx <= mid)
            update(2 * o, left, mid, idx, val);
        else
            update(2 * o + 1, mid + 1, right, idx, val);
        merge(tree[2 * o], tree[2 * o + 1], tree[o]);
    }

    void query(int o, int left, int right, int l, int r, Node& result) {
        if (left == l && r == right) {
            result = tree[o];
            return;
        }
        int mid = (left + right) / 2;
        if (r <= mid) {
            query(2 * o, left, mid, l, r, result);
        } else if (mid < l) {
            query(2 * o + 1, mid + 1, right, l, r, result);
        } else {
            Node left_part(0, k), right_part(0, k);
            query(2 * o, left, mid, l, mid, left_part);
            query(2 * o + 1, mid + 1, right, mid + 1, r, right_part);
            merge(left_part, right_part, result);
        }
    }
};

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size(), m = queries.size();
        SegmentTree st(nums, k);
        vector<int> ans(m);
        
        Node result(0, k);
        for (int i = 0; i < m; i++) {
            int idx = queries[i][0], val = queries[i][1], start = queries[i][2], x = queries[i][3];
            st.update(1, 1, n, idx + 1, val);
            st.query(1, 1, n, start + 1, n, result);
            ans[i] = result.cnt[x];
        }
        return ans;
    }
};