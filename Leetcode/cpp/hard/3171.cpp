/*
 * @lc app=leetcode.cn id=3171 lang=cpp
 *
 * [3171] 找到按位与最接近 K 的子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1a {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int ans = INT_MAX;
        unordered_set<int> st, st2;
        for (int x : nums) {
            st2.clear();
            for (int y : st)
                st2.insert(y | x);
            st2.insert(x);
            swap(st, st2);
            for (int y : st)
                ans = min(ans, abs(y - k));
        }
        return ans;
    }
};

class Solution1b {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;
        vector<int> st;
        for (int x : nums) {
            vector<int> st2 = {x};
            for (int y : st)
                if ((y | x) != st2.back())
                    st2.push_back(y | x);
            st = st2;
            for (int y : st)
                ans = min(ans, abs(y - k));
        }
        return ans;
    }
};

class Solution1c {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;
        for (int i = 0; i < n; i++) {
            ans = min(ans, abs(nums[i] - k));
            for (int j = i - 1; j >= 0; j--) {
                if ((nums[j] | nums[i]) == nums[j]) break;
                nums[j] |= nums[i];
                ans = min(ans, abs(nums[j] - k));
            }
        }
        return ans;
    }
};

class Solution2 {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;
        int left = 0, cur = 0;
        vector<int> cnt(32, 0);
        for (int right = 0; right < n; right++) {
            for (int b = 0; b < 32; b++) {
                if (nums[right] & (1 << b))
                    if (++cnt[b] == 1) cur |= 1 << b;
            }
            ans = min(ans, abs(cur - k));
            while (left < right && cur >= k) {
                for (int b = 0; b < 32; b++) {
                    if (nums[left] & (1 << b))
                        if (--cnt[b] == 0) cur &= ~(1 << b);
                }
                left++;
                ans = min(ans, abs(cur - k));
            }
        }
        return ans;
    }
};

class Solution3a {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;
        // Stack 由上到下保存 OR(nums[i...bottom]), OR(nums[i+1...bottom]) 之結果
        vector<int> st = {0};
        int left = 0, right_or = 0;
        for (int right = 0; right < n; right++) {
            right_or |= nums[right];
            while (left <= right && (st.back() | right_or) >= k) {
                ans = min(ans, (st.back() | right_or) - k);
                st.pop_back();
                left += 1;
                // 重新構建 Stack
                if (st.empty()) {
                    st.push_back(0);
                    for (int i = right; i >= left; i--)
                        st.push_back(st.back() | nums[i]);
                    right_or = 0;
                }
            }
            if (left <= right)
                ans = min(ans, k - (st.back() | right_or));
        }
        return ans;
    }
};

class Solution3b {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;
        // 原地使用 nums 作為 Stack，由上到下保存 OR(nums[i...bottom]), OR(nums[i+1...bottom]) 之結果
        int left = 0, bottom = 0, right_or = 0;
        for (int right = 0; right < n; right++) {
            right_or |= nums[right];
            while (left <= right && (nums[left] | right_or) >= k) {
                ans = min(ans, (nums[left] | right_or) - k);
                left += 1;
                // 重新構建 Stack
                if (bottom < left) {
                    for (int i = right - 1; i >= left; i--)
                        nums[i] |= nums[i + 1];
                    bottom = right;
                    right_or = 0;
                }
            }
            if (left <= right)
                ans = min(ans, k - (nums[left] | right_or));
        }
        return ans;
    }
};

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
        return tree[left_child] | tree[right_child];
    }

    int query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        int ans = 0;
        if (l <= mid) ans |= query(2 * o, left, mid, l, r);
        if (r > mid) ans |= query(2 * o + 1, mid + 1, right, l, r);
        return ans;
    }
};

class Solution4 {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        SegmentTree seg(nums);
        int ans = INT_MAX;
        for (int i = 1; i <= n; i++) {
            int left = i, right = n;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (seg.query(1, 1, n, i, mid) >= k) right = mid - 1;
                else left = mid + 1;
            }
            if (left <= n) ans = min(ans, seg.query(1, 1, n, i, left) - k);
            if (right >= i) ans = min(ans, k - seg.query(1, 1, n, i, right));
        }
        return ans;
    }
};

// using Solution = Solution1a;
// using Solution = Solution1b;
// using Solution = Solution2;
using Solution = Solution3a;
// using Solution = Solution3b;
// using Solution = Solution4;
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> nums = {1,8,9};
    int k = 7;
    cout << sol.minimumDifference(nums, k) << endl; // 1
    return 0;
}