#include <bits/stdc++.h>
using namespace std;

class FenwickTree_PURQ1 { // PURQ (Point Update Range Query), 0-based, initialization: O(nlogn)
private:
    int n;
    vector<int> tree;
    vector<int> nums;
public:
    FenwickTree_PURQ1(int n) { // Not Initialize
        this->n = n;
        tree = vector<int>(n, 0);
    }
    FenwickTree_PURQ1(vector<int>& nums) { // or 
        n = nums.size();
        this->nums = nums;
        tree = vector<int>(n);
        for (int i = 0; i < n; i++) { // initialization: O(nlogn)
            add(i, nums[i]);
        }
    }

    void add(int k, int x) { // 令 nums[k] += x
        for (int i = k+1; i <= n; i += i & -i) {
            tree[i-1] += x;
        }
    }

    void update(int k, int x) { // 令 nums[k] = x
        add(k, x - nums[k]);
        nums[k] = x;
    }

    int sum(int l, int r) { // 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        return preSum(r) - preSum(l - 1);
    }

    int preSum(int k) { // 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        int res = 0;
        for (int i = k+1; i > 0; i -= i & -i) {
            res += tree[i-1];
        }
        return res;
    }
};

class FenwickTree_PURQ2 { // PURQ (Point Update Range Query), 1-based, initialization: O(n)
private:
    int n = 0;
    vector<int> tree;
    vector<int> nums;
public:
    FenwickTree_PURQ2(vector<int>& nums) {
        n = nums.size();
        this->nums = nums;
        tree = vector<int>(n + 1); // 1-based
        for (int i = 1; i <= n; i++) { // initialization: O(n)
            tree[i] += nums[i-1];
            int nxt = i + (i & -i); // 下一個關鍵區間的右端點
            if (nxt <= n) {
                tree[nxt] += tree[i];
            }
        }
    }

    void add(int k, int x) { // 令 nums[k] += x
        for (int i = k+1; i < tree.size(); i += i & -i) {
            tree[i] += x;
        }
    }

    void update(int k, int x) { // 令 nums[k] = x
        add(k, x - nums[k]);
        nums[k] = x;
    }

    int sum(int l, int r) { // 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        return preSum(r+1) - preSum(l);
    }

    int preSum(int k) { // 求前綴和: 求 nums[0] 到 nums[k] 的區間和
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