struct Node {
    int cnt0, cnt1;
    long long res;
};

class SegmentTree {
private:
    int n, k;
    vector<int> nums;
    vector<Node> tree;

    void build(int o, int left, int right) {
        if (left == right) {
            tree[o] = {0, 0, 0};
            if (nums[left] == 0) {
                tree[o].cnt0++;
            } else {
                tree[o].cnt1++;
            }
            tree[o].res = (tree[o].cnt0 <= k || tree[o].cnt1 <= k) ? 1 : 0;
            return;
        }
        int mid = (left + right) / 2;
        build(2*o, left, mid);
        build(2*o+1, mid + 1, right);
        tree[o] = merge(tree[2*o], tree[2*o+1], left, mid, right);
    }

    Node merge(Node& left_part, Node& right_part, int left, int mid, int right) {
        Node res = {0, 0, 0};
        res.cnt0 = left_part.cnt0 + right_part.cnt0;
        res.cnt1 = left_part.cnt1 + right_part.cnt1;
        res.res = left_part.res + right_part.res;
        
        if (res.cnt0 <= k || res.cnt1 <= k) {
            res.res += (mid - left + 1) * (right - mid);
            return res;
        }

        int cnt0 = left_part.cnt0, cnt1 = left_part.cnt1;
        int l = left;
        for (int r = mid + 1; r <= right; ++r) {
            if (nums[r] == 0) {
                cnt0++;
            } else {
                cnt1++;
            }
            while (l <= mid && cnt0 > k && cnt1 > k) {
                if (nums[l] == 0) {
                    cnt0--;
                } else {
                    cnt1--;
                }
                l++;
            }
            res.res += mid - l + 1;
        }
        return res;
    }

    Node query(int o, int left, int right, int l, int r) {
        if (left == l && r == right) {
            return tree[o];
        }
        int mid = (left + right) / 2;
        if (r <= mid) {
            return query(2*o, left, mid, l, r);
        }
        if (mid < l) {
            return query(2*o+1, mid + 1, right, l, r);
        }
        Node left_part = query(2*o, left, mid, l, mid);
        Node right_part = query(2*o+1, mid+1, right, mid+1, r);
        return merge(left_part, right_part, l, mid, r);
    }

public:
    SegmentTree(const vector<int>& nums, int k) : n(nums.size()), k(k) {
        this->nums.push_back(0);
        this->nums.insert(this->nums.end(), nums.begin(), nums.end());
        tree.resize(4 * n);
        build(1, 1, n);
    }

    long long query(int l, int r) {
        return query(1, 1, n, l, r).res;
    }
};

class Solution {
public:
    vector<long long> countKConstraintSubstrings(string s, int k, vector<vector<int>>& queries) {
        int n = s.length();
        vector<int> nums;
        for (char c : s) {
            nums.push_back(c - '0');
        }
        SegmentTree st(nums, k);
        vector<long long> res(queries.size());
        for (int i = 0; i < queries.size(); ++i) {
            res[i] = st.query(queries[i][0] + 1, queries[i][1] + 1);
        }
        return res;
    }
};