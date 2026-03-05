/*
 * @lc app=leetcode id=56 lang=rust
 *
 * [56] Merge Intervals
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_by_key(|interval| interval[0]);
        let mut ans: Vec<Vec<i32>> = Vec::new();
        for interval in intervals {
            let l = interval[0];
            let r = interval[1];
            if ans.is_empty() || l > ans.last().unwrap()[1] {
                ans.push(interval);
            } else {
                ans.last_mut().unwrap()[1] = r.max(ans.last().unwrap()[1]);
            }
        }
        ans
    }
}
// @lc code=end
