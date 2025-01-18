/*
    同餘定理 + 線段樹

    若兩個數A、B ，滿足 A % M == B % M，則兩個數的差值 (A - B) % M == 0，即 M 是 (A - B) 的因數。
    故求最大的 M 等同求兩數之差的最大公因數，可以計算 diffs 陣列，其中 diffs[i] = abs(A[i+1] - A[i])。

    而求區間 [l, r] 的最大 M 值，等同求 diffs[l] ~ diffs[r-1] 的最大公因數，這可以用線段樹維護。
*/

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

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
        return gcd(tree[left_child], tree[right_child]);
    }

    int query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        int ans = 0;
        if (l <= mid) ans = gcd(ans, query(2 * o, left, mid, l, r));
        if (r > mid) ans = gcd(ans, query(2 * o + 1, mid + 1, right, l, r));
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, q, l, r;
    cin >> t;
    while (t--) {
        cin >> n >> q;
        vector<int> A(n);
        for (int i = 0; i < n; ++i) cin >> A[i];
        vector<int> diffs(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            diffs[i] = abs(A[i + 1] - A[i]);
        }
        SegmentTree* st = (n > 1) ? new SegmentTree(diffs) : nullptr;
        vector<int> ans;
        while (q--) {
            cin >> l >> r;
            if (n == 1 || l == r) ans.push_back(0);
            else ans.push_back(st->query(1, 1, n - 1, l, r - 1));
        }
        for (int x : ans) cout << x << " ";
        cout << endl;
        delete st;
    }
    return 0;
}