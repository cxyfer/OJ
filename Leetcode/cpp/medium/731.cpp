/*
 * @lc app=leetcode.cn id=731 lang=cpp
 *
 * [731] 我的日程安排表 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Node {
public:
    int val, lazy; // value, lazy tag
    Node() : val(0), lazy(0) {}
};

class SegmentTree {
public:
    unordered_map<int, Node*> tree;
    
    SegmentTree() {
        tree[1] = new Node();
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
        int mid = left + ((right - left) >> 1);
        // Calculate answer: maximum value in this problem
        int ans = 0;
        if (l <= mid) ans = query(o * 2, left, mid, l, r);
        if (r > mid) ans = max(ans, query(o * 2 + 1, mid + 1, right, l, r));
        return ans;
    }

    // Push down lazy tags
    void pushdown(int o) {
        if (tree.find(o * 2) == tree.end()) tree[o * 2] = new Node();
        if (tree.find(o * 2 + 1) == tree.end()) tree[o * 2 + 1] = new Node();
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

class MyCalendarTwo {
public:
    SegmentTree st;
    int root, MAX;
    MyCalendarTwo() {
        st = SegmentTree();
        root = 1;
        MAX = 1e9;
    }
    
    bool book(int start, int end) {
        if (st.query(root, 0, MAX, start, end-1) >= 2) {
            return false;
        }
        st.update(root, 0, MAX, start, end-1, 1);
        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */
// @lc code=end

int main() {
    cout << "start" << endl;
    MyCalendarTwo obj = MyCalendarTwo();
    cout << obj.book(10, 20) << endl; // True
    cout << obj.book(50, 60) << endl; // True
    cout << obj.book(10, 40) << endl; // True
    cout << obj.book(5, 15) << endl; // False
    cout << obj.book(5, 10) << endl; // True
    cout << obj.book(25, 55) << endl; // True
    return 0;
}
