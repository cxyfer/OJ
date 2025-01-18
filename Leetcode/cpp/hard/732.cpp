/*
 * @lc app=leetcode.cn id=732 lang=cpp
 *
 * [732] 我的日程安排表 III
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
struct SegNode {
    int val, lazy; // value, lazy tag
    SegNode() : val(0), lazy(0) {}
};

class SegmentTree {
public:
    unordered_map<int, SegNode*> tree;
    
    SegmentTree() {
        tree[1] = new SegNode();
    }

    // Update the range [l, r] with value v
    void update(int o, int left, int right, int l, int r, int v) {
        if (l <= left && right <= r) {
            tree[o]->lazy += v;
            tree[o]->val += v;
            return;
        }
        pushdown(o); // Push down lazy tags
        int mid = left + ((right - left) >> 1);
        if (l <= mid) update(o * 2, left, mid, l, r, v);
        if (r > mid) update(o * 2 + 1, mid + 1, right, l, r, v);
        pushup(o); // Push up node value
    }

    // Query the range [l, r]
    int query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return tree[o]->val;
        }
        // Ensure all lazy tags have been pushed down
        pushdown(o);
        // Calculate answer: maximum value in this problem
        int ans = 0;
        int mid = left + ((right - left) >> 1);
        if (l <= mid) ans = query(o * 2, left, mid, l, r);
        if (r > mid) ans = max(ans, query(o * 2 + 1, mid + 1, right, l, r));
        return ans;
    }

    // Push down lazy tags
    void pushdown(int o) {
        if (tree.find(o * 2) == tree.end()) tree[o * 2] = new SegNode();
        if (tree.find(o * 2 + 1) == tree.end()) tree[o * 2 + 1] = new SegNode();
        if (tree[o]->lazy != 0) {
            tree[o * 2]->lazy += tree[o]->lazy;
            tree[o * 2 + 1]->lazy += tree[o]->lazy;
            tree[o * 2]->val += tree[o]->lazy;
            tree[o * 2 + 1]->val += tree[o]->lazy;
            tree[o]->lazy = 0; // Clear current node's lazy tag
        }
    }

    // Push up node value
    void pushup(int o) {
        // Update method: maximum value in this problem
        tree[o]->val = max(tree[o * 2]->val, tree[o * 2 + 1]->val);
    }
};

class MyCalendarThree {
public:
    SegmentTree *tree;
    int MAXN;
    MyCalendarThree() {
        tree = new SegmentTree();
        MAXN = 1e9;
    }
    
    int book(int startTime, int endTime) {
        tree->update(1, 0, MAXN, startTime, endTime - 1, 1);
        return tree->query(1, 0, MAXN, 0, MAXN);
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime,endTime);
 */
// @lc code=end

