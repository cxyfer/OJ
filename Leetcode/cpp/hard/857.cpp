/*
 * @lc app=leetcode.cn id=857 lang=cpp
 *
 * [857] 雇佣 K 名工人的最低成本
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        令 r = wage / quality，那麼選定一個 r0 ，每個工人的實際薪水就是 r0 * quality。
        而對 ri <= r0 的工人，他們的實際薪水就會比預期的最低薪水高，這裡可以靠舉例來理解。
        因此我們可以對所有工人按照 r 值進行排序，對於前 k 名工人，選定 rk 就能滿足他們的薪水要求。

        由於實際的薪水只跟選定的 r0 和 quality 有關，所以我們可以統計選定工人的 quality 總和 sum_q，並維護一個Max Heap，保存所有選定工人的 quality。
        在遇到一個新的工人時，雖然 ri 會比 r0 大，但是 quality 可能會比堆頂的 quality 小，這樣就可以更新堆頂 和 sum_q ，得到更優的答案。

        Reference:
            - https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/solutions/1815856/yi-bu-bu-ti-shi-ru-he-si-kao-ci-ti-by-en-1p00/
    */
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        int n = quality.size();
        vector<pair<int, int>> pairs; // 保存 quality 和 wage 的 pair
        for (int i = 0; i < n; i++) pairs.push_back({quality[i], wage[i]});
        sort(pairs.begin(), pairs.end(), [](pair<int, int>& a, pair<int, int>& b) { // 按照 r 值排序
            return (double)a.second / a.first < (double)b.second / b.first;
        });
        int sum_q = 0; // 選定的 k 名工人的 quality 總和
        priority_queue<int> hp; // Max Heap，保存選定的 k 名工人的 quality
        for (int i = 0; i < k; i++) {
            sum_q += pairs[i].first;
            hp.push(pairs[i].first);
        }
        double ans = sum_q * (double)pairs[k - 1].second / pairs[k - 1].first; // 初始化答案為前 k 名工人的薪水總和，選擇 r0 = rk
        for (int i = k; i < n; i++) { // 遍歷剩下的工人，雖然 ri > r0，但是 quality 可能比堆頂的 quality 小，可能有更優的答案
            if (pairs[i].first < hp.top()) { // 如果 quality 比堆頂小
                sum_q += pairs[i].first - hp.top(); // 更新堆頂和 sum_q
                hp.pop();
                hp.push(pairs[i].first);
                ans = min(ans, sum_q * (double)pairs[i].second / pairs[i].first); // 更新答案
            }
        }
        return ans;
    }
};
// @lc code=end

