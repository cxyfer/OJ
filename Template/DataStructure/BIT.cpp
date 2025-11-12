#include <bits/stdc++.h>
using namespace std;

class BIT {  // PURQ, 1-based
private:
    vector<int> tree;

public:
    BIT(int n) {
        tree = vector<int>(n + 1, 0);
    }

    void add(int k, int x) {  // 令 nums[k] += x
        for (; k < tree.size(); k += k & -k) tree[k] += x;
    }

    int preSum(int k) {  // 求 nums[:k+1] 之和
        int res = 0;
        for (; k > 0; k -= k & -k) res += tree[k];
        return res;
    }

    int query(int l, int r) {  // 求 nums[l:r+1] 之和
        if (l > r) return 0;
        return preSum(r) - preSum(l - 1);
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        // 離散化
        auto B = nums;
        sort(B.begin(), B.end());
        B.erase(unique(B.begin(), B.end()), B.end());
        int m = B.size();
        for (auto& x : nums)
            x = lower_bound(B.begin(), B.end(), x) - B.begin() + 1;

        // BIT
        BIT bit(m);
        vector<int> ans(n);
        for (int i = n - 1; i >= 0; i--) {
            ans[i] = bit.query(1, nums[i] - 1);
            bit.add(nums[i], 1);
        }
        return ans;
    }
};

class FenwickTree_PURQ1 {  // PURQ (Point Update Range Query), 0-based,
                           // initialization: O(nlogn)
private:
    int n;
    vector<int> tree;
    vector<int> nums;

public:
    FenwickTree_PURQ1(int n) {  // Not Initialize
        this->n = n;
        tree = vector<int>(n, 0);
    }
    FenwickTree_PURQ1(vector<int>& nums) {  // or
        n = nums.size();
        this->nums = nums;
        tree = vector<int>(n);
        for (int i = 0; i < n; i++) {  // initialization: O(nlogn)
            add(i, nums[i]);
        }
    }

    void add(int k, int x) {  // 令 nums[k] += x
        for (int i = k + 1; i <= n; i += i & -i) {
            tree[i - 1] += x;
        }
    }

    void update(int k, int x) {  // 令 nums[k] = x
        add(k, x - nums[k]);
        nums[k] = x;
    }

    int sum(int l, int r) {  // 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        return preSum(r) - preSum(l - 1);
    }

    int preSum(int k) {  // 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        int res = 0;
        for (int i = k + 1; i > 0; i -= i & -i) {
            res += tree[i - 1];
        }
        return res;
    }
};

class FenwickTree_PURQ2 {  // PURQ (Point Update Range Query), 1-based,
                           // initialization: O(n)
private:
    int n = 0;
    vector<int> tree;
    vector<int> nums;

public:
    FenwickTree_PURQ2(vector<int>& nums) {
        n = nums.size();
        this->nums = nums;
        tree = vector<int>(n + 1);      // 1-based
        for (int i = 1; i <= n; i++) {  // initialization: O(n)
            tree[i] += nums[i - 1];
            int nxt = i + (i & -i);  // 下一個關鍵區間的右端點
            if (nxt <= n) {
                tree[nxt] += tree[i];
            }
        }
    }

    void add(int k, int x) {  // 令 nums[k] += x
        for (int i = k + 1; i < tree.size(); i += i & -i) {
            tree[i] += x;
        }
    }

    void update(int k, int x) {  // 令 nums[k] = x
        add(k, x - nums[k]);
        nums[k] = x;
    }

    int sum(int l, int r) {  // 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        return preSum(r + 1) - preSum(l);
    }

    int preSum(int k) {  // 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        int s = 0;
        for (int i = k; i > 0; i -= i & -i) {
            s += tree[i];
        }
        return s;
    }
};

int main() {
    return 0;
}