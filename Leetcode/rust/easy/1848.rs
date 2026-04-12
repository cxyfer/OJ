/*
 * @lc app=leetcode id=1848 lang=rust
 *
 * [1848] Minimum Distance to the Target Element
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        nums.iter()
            .enumerate()
            .filter(|&(_, &x)| x == target)
            .map(|(i, _)| (i as i32 - start).abs())
            .min()
            .unwrap()
    }
}
// @lc code=end
