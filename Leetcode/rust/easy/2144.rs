/*
 * @lc app=leetcode id=2144 lang=rust
 *
 * [2144] Minimum Cost of Buying Candies With Discount
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn minimum_cost(mut cost: Vec<i32>) -> i32 {
        let n = cost.len();
        cost.sort_unstable_by(|a, b| b.cmp(a));
        let mut ans = 0;
        let mut i = 0;
        while i < n {
            ans += cost[i];
            if i + 1 < n {
                ans += cost[i + 1];
            }
            i += 3;
        }
        ans
    }
}
// @lc code=end

