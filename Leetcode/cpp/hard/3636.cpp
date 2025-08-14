/*
 * @lc app=leetcode.cn id=3636 lang=cpp
 * @lcpr version=30204
 *
 * [3636] 查询超过阈值频率最高元素
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
struct Query {
    int bid, l, r, th, qid;
    Query(int bid, int l, int r, int th, int qid) : bid(bid), l(l), r(r), th(th), qid(qid) {}
};

class Solution {
public:
    vector<int> subarrayMajority(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), q = queries.size();
        unordered_map<int, int> cnt;
        int min_val = -1, max_cnt = 0;

        auto add = [&](int x) {
            cnt[x]++;
            if (cnt[x] > max_cnt) {
                min_val = x;
                max_cnt = cnt[x];
            }
            else if (cnt[x] == max_cnt) {
                min_val = min(min_val, x);
            }
        };

        int BLK_SZ = ceil(n / sqrt(q * 2));
        vector<int> ans(q);
        vector<Query> qs;
        for (int qid = 0; qid < q; qid++) {
            const auto& query = queries[qid];
            int l = query[0], r = query[1], th = query[2];
            // 大區間離線，確保 l 和 r 不在同一個 block 中
            if (r - l + 1 > BLK_SZ) qs.emplace_back(l / BLK_SZ, l, r, th, qid);
            // 小區間暴力
            else {
                cnt.clear();
                min_val = -1, max_cnt = 0;
                for (int i = l; i <= r; i++) add(nums[i]);
                ans[qid] = (max_cnt >= th) ? min_val : -1;
            }
        }

        // 離線排序
        sort(qs.begin(), qs.end(), [](const Query& a, const Query& b) {
            if (a.bid != b.bid) return a.bid < b.bid;
            return a.r < b.r;  // 右端點從小到大
        });

        int l = 0, r = 0;
        for (int i = 0; i < qs.size(); i++) {
            const auto& q = qs[i];
            
            int l0 = (q.bid + 1) * BLK_SZ;
            // 遍歷到一個新的 block
            if (i == 0 || q.bid > qs[i - 1].bid) {
                r = l0;
                cnt.clear();
                min_val = -1, max_cnt = 0;
            }

            // 右端點從 r 向右移動到 qr（包含 qr）
            while (r <= q.r)
                add(nums[r++]);

            // 移動左端點前先備份
            int tmp_min_val = min_val, tmp_max_cnt = max_cnt;
            // 左端點從 l0 向左移動到 ql（不包含 l0）
            for (int i = q.l; i < l0; i++)
                add(nums[i]);
            ans[q.qid] = (max_cnt >= q.th) ? min_val : -1;

            // 回滾
            min_val = tmp_min_val, max_cnt = tmp_max_cnt;
            for (int i = q.l; i < l0; i++)
                cnt[nums[i]]--;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,1,2,2,1,1]\n[[0,5,4],[0,3,3],[2,3,2]]\n
// @lcpr case=end

// @lcpr case=start
// [3,2,3,2,3,2,3]\n[[0,6,4],[1,5,2],[2,4,1],[3,3,1]]\n
// @lcpr case=end

 */

