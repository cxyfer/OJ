/*
 * @lc app=leetcode.cn id=2286 lang=cpp
 *
 * [2286] 以组为单位订音乐会的门票
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
struct SegNode {
    long long sum, max; // 只有 sum 會用到 long long
    SegNode() : sum(0), max(0) {}
};
class SegmentTree {
private:
    vector<int> nums;
    vector<SegNode> tree;
public:
    SegmentTree(vector<int>& nums) {
        int n = nums.size();
        this->nums = vector<int>(n + 1, 0);
        for (int i = 1; i <= n; i++) this->nums[i] = nums[i - 1]; // 1-indexed
        this->tree = vector<SegNode>(1 << (__lg(n) + 2));
        build(1, 1, n);
    }

    void build(int o, int left, int right) {
        if (left == right) {
            tree[o].sum = nums[left];
            tree[o].max = nums[left];
            return;
        }
        int mid = (left + right) / 2;
        build(2 * o, left, mid);
        build(2 * o + 1, mid + 1, right);
        tree[o].sum = tree[2 * o].sum + tree[2 * o + 1].sum;
        tree[o].max = max(tree[2 * o].max, tree[2 * o + 1].max);
    }

    void update(int o, int left, int right, int idx, int val) {
        if (left == right) {
            nums[idx] += val;
            tree[o].sum += val;
            tree[o].max += val;
            return;
        }
        int mid = (left + right) / 2;
        if (idx <= mid) update(2 * o, left, mid, idx, val);
        else update(2 * o + 1, mid + 1, right, idx, val);
        tree[o].sum = tree[2 * o].sum + tree[2 * o + 1].sum;
        tree[o].max = max(tree[2 * o].max, tree[2 * o + 1].max);
    }

    SegNode query(int o, int left, int right, int l, int r) {
        if (left == l && r == right) return tree[o];
        int mid = (left + right) / 2;
        if (r <= mid) return query(2 * o, left, mid, l, r);  // 只需要查詢左半部分
        if (mid < l) return query(2 * o + 1, mid + 1, right, l, r);  // 只需要查詢右半部分
        SegNode left_part = query(2 * o, left, mid, l, mid);  // 左半部分
        SegNode right_part = query(2 * o + 1, mid + 1, right, mid + 1, r);  // 右半部分
        SegNode res;
        res.sum = left_part.sum + right_part.sum;
        res.max = max(left_part.max, right_part.max);
        return res;
    }

    int query_first(int o, int left, int right, int l, int r, int k) {
        if (tree[o].max < k) return -1;
        if (left == right) return left;
        int mid = (left + right) / 2;
        if (l <= mid && tree[2 * o].max >= k) return query_first(2 * o, left, mid, l, r, k);
        if (r > mid) return query_first(2 * o + 1, mid + 1, right, l, r, k);
        return -1;
    }
};

class BookMyShow {
public:
    int n, m;
    SegmentTree* seg;
    BookMyShow(int n, int m) {
        this->n = n;
        this->m = m;
        vector<int> nums(n, m);
        this->seg = new SegmentTree(nums);
    }
    
    vector<int> gather(int k, int maxRow) {
        // 從第 1 橫列開始找，直到找到一橫列的剩餘座位數 >= k
        int r = seg->query_first(1, 1, n, 1, maxRow + 1, k);
        if (r == -1) return {};
        int c = m - seg->query(1, 1, n, r, r).sum; // 單個橫排的剩餘座位數不會超過 int 範圍
        seg->update(1, 1, n, r, -k); // 更新剩餘座位數
        return {r - 1, c};
    }
    
    bool scatter(int k, int maxRow) {
        // 先檢查在 [1, maxRow + 1] 橫列的剩餘座位數總和，若小於 k，則無法滿足條件
        if (seg->query(1, 1, n, 1, maxRow + 1).sum < k) return false;
        // 從第一個有空位的橫排開始，逐個橫排填入座位
        while (k > 0) {
            int r = seg->query_first(1, 1, n, 1, maxRow + 1, 1); // 找到第一個有空位的橫排
            int left = min(k, (int) seg->query(1, 1, n, r, r).sum); // 需要使用的座位數
            seg->update(1, 1, n, r, -left); // 更新剩餘座位數
            k -= left;
        }
        return true;
    }
};

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow* obj = new BookMyShow(n, m);
 * vector<int> param_1 = obj->gather(k,maxRow);
 * bool param_2 = obj->scatter(k,maxRow);
 */
// @lc code=end

int main() {
    BookMyShow* obj = new BookMyShow(2, 5);
    cout << obj->gather(4, 0) << endl;
    cout << obj->gather(2, 0) << endl;
    cout << obj->scatter(5, 1) << endl;
    cout << obj->scatter(5, 1) << endl;
    return 0;
}