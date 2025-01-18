/*
 * @lc app=leetcode.cn id=3161 lang=cpp
 *
 * [3161] 物块放置查询
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

/*
    維護三個性質
    - ld: left distance, 從左邊到最近的障礙物的距離，無障礙物為 -1
    - rd: right distance, 從右邊到最近的障礙物的距離，無障礙物為 -1
    - mx: 最大可放置的連續物體長度，單點為 0
        - 若無障礙物， [1, 2] 區間可放置的最大長度為 1
*/
class Node {
public:
    int ld, rd, mx;
    Node() : ld(-1), rd(-1), mx(0) {}
    Node(int ld, int rd, int mx) : ld(ld), rd(rd), mx(mx) {}
};

class SegmentTree {
private:
    vector<Node> tree;
public:
    SegmentTree(int n) {
        this->tree = vector<Node>(4 * n, Node());  // (ld, rd, mx)
        build(1, 0, n);
    }

    void build(int o, int left, int right) {
        if (left == right) {
            tree[o] = {-1, -1, 0};  // (ld, rd, mx)
            return;
        }
        int mid = (left + right) / 2;
        build(2 * o, left, mid);
        build(2 * o + 1, mid + 1, right);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1], left, mid, right);
    }

    Node merge(Node l, Node r, int left, int mid, int right) {
        Node res = Node(l.ld, r.rd, 0);

        int t = 1;  // 中間的部分最大可放置的連續物體長度
        t += (l.rd == -1 ? (mid - left) : l.rd);  // 從中間往左延伸
        t += (r.ld == -1 ? (right - (mid + 1)) : r.ld);  // 從中間往右延伸
        res.mx = max({l.mx, r.mx, t});  // [left, right] 區間最大可放置的連續物體長度

        if (l.ld == -1) {
            res.ld = (r.ld == -1) ? -1 : (mid - left + 1 + r.ld);  // 往右延伸
        }
        if (r.rd == -1) {
            res.rd = (l.rd == -1) ? -1 : (right - (mid + 1) + 1 + l.rd);  // 往左延伸
        }
        return res;
    }

    void update(int o, int left, int right, int idx, int val) {
        if (left == right) {
            tree[o] = {0, 0, 0};  // (ld, rd, mx)
            return;
        }
        int mid = (left + right) / 2;
        if (idx <= mid) update(2 * o, left, mid, idx, val);
        else update(2 * o + 1, mid + 1, right, idx, val);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1], left, mid, right);
    }

    Node query(int o, int left, int right, int l, int r) {
        if (left == l && r == right) return tree[o];
        int mid = (left + right) / 2;
        if (r <= mid) return query(2 * o, left, mid, l, r);  // 只需要查詢左半部分
        if (mid < l) return query(2 * o + 1, mid + 1, right, l, r);  // 只需要查詢右半部分
        Node left_part = query(2 * o, left, mid, l, mid);  // 左半部分
        Node right_part = query(2 * o + 1, mid + 1, right, mid + 1, r);  // 右半部分
        return merge(left_part, right_part, l, mid, r);  // 合併左右兩部分
    }
};

class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        int n = min((int)5e4, 3 * (int)queries.size());
        SegmentTree seg(n);
        vector<bool> ans;
        for (auto& q : queries) {
            int op = q[0], x = q[1];
            if (op == 1) {
                seg.update(1, 0, n, x, 0);
            } else {
                int sz = q[2];
                ans.push_back(seg.query(1, 0, n, 0, x).mx >= sz);
            }
        }
        return ans;
    }
};
// @lc code=end

