/*
 * @lc app=leetcode.cn id=3515 lang=cpp
 * @lcpr version=30204
 *
 * [3515] 带权树中的最短路径
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
template<typename T>
struct SegNode {
    SegNode *ls, *rs; // left child, right child
    T val, lazy; // value, lazy tag
    SegNode() : ls(nullptr), rs(nullptr), val(0), lazy(0) {}
};

template<typename T>
class SegmentTree {
public:
    SegNode<T> *root;
    
    SegmentTree() {
        root = new SegNode<T>();
    }

    SegmentTree(vector<T> &nums) {
        root = new SegNode<T>();
        build(root, 1, nums.size(), nums);
    }

    void build(SegNode<T> *node, int left, int right, vector<T> &nums) {
        if (left == right) {
            node->val = nums[left - 1]; // assert nums is 0-indexed
            return;
        }
        int mid = left + ((right - left) >> 1);
        node->ls = new SegNode<T>();
        node->rs = new SegNode<T>();
        build(node->ls, left, mid, nums);
        build(node->rs, mid + 1, right, nums);
        pushup(node); // Push up node value
    }

    // Update the range [l, r] with value v
    void update(SegNode<T> *node, int left, int right, int l, int r, T v) {
        if (l <= left && right <= r) {
            // Update node value (Customized)
            _update(node, left, right, v);
            return;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        if (l <= mid) update(node->ls, left, mid, l, r, v);
        if (r > mid) update(node->rs, mid + 1, right, l, r, v);
        pushup(node); // Push up node value
    }

    // Update node value (Customized)
    void _update(SegNode<T> *node, int left, int right, T v) {
        node->val += v * (right - left + 1);
        node->lazy += v;
    }

    // Query the range [l, r]
    T query(SegNode<T> *node, int left, int right, int l, int r) {
        if (l <= left && right <= r) {
            return node->val;
        }
        pushdown(node, left, right);
        int mid = left + ((right - left) >> 1);
        // Calculate answer (Customized)
        T ans = 0;
        if (l <= mid) ans += query(node->ls, left, mid, l, r);
        if (r > mid) ans += query(node->rs, mid + 1, right, l, r);
        return ans;
    }

    // Push down lazy tags
    void pushdown(SegNode<T> *node, int left, int right) {
        if (node->ls == nullptr) node->ls = new SegNode<T>();
        if (node->rs == nullptr) node->rs = new SegNode<T>();
        if (node->lazy != 0) {
            int mid = left + ((right - left) >> 1);
            // Update node value (Customized)
            _update(node->ls, left, mid, node->lazy);
            _update(node->rs, mid + 1, right, node->lazy);
            node->lazy = 0;
        }
    }

    // Push up node value
    void pushup(SegNode<T> *node) {
        // Update method (Customized)
        node->val = node->ls->val + node->rs->val;
    }
};

class Solution {
public:
    vector<int> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        vector<vector<pair<int, int>>> g(n + 1);
        for (auto &edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            g[u].emplace_back(v, w);
            g[v].emplace_back(u, w);
        }

        vector<int> dist(n + 1), dfns(n + 1), dfne(n + 1), weight(n + 1);
        int time = 0;  // timestamp, 1-indexed
        auto dfs = [&](this auto &&dfs, int u, int fa, int d) -> void {
            dfns[u] = ++time;
            dist[u] = d;
            for (auto [v, w] : g[u]) {
                if (v == fa) continue;
                weight[v] = w;  // store weight at child node
                dfs(v, u, d + w);
            }
            dfne[u] = time;
        };
        dfs(1, 0, 0);
        
        SegmentTree<long long> st;
        vector<int> ans;
        for (auto &query : queries) {
            int op = query[0];
            if (op == 1) {
                int u = query[1], v = query[2], w = query[3];
                if (dist[u] > dist[v]) swap(u, v);  // let v be the child node
                st.update(st.root, 1, n, dfns[v], dfne[v], w - weight[v]);
                weight[v] = w;  // update weight
            } else {
                int x = query[1];
                ans.push_back(dist[x] + st.query(st.root, 1, n, dfns[x], dfns[x]));
            }
        }
        return ans;
    }
};
// @lc code=end

/*
// @lcpr case=start
// 2\n[[1,2,7]]\n[[2,2],[1,1,2,4],[2,2]]\n
// @lcpr case=end

// @lcpr case=start
// 3\n[[1,2,2],[1,3,4]]\n[[2,1],[2,3],[1,1,3,7],[2,2],[2,3]]\n
// @lcpr case=end

// @lcpr case=start
// 4\n[[1,2,2],[2,3,1],[3,4,5]]\n[[2,4],[2,3],[1,2,3,3],[2,2],[2,3]]\n
// @lcpr case=end

 */

