/*
 * @lc app=leetcode id=485 lang=rust
 *
 * [485] Max Consecutive Ones
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        let mut i = 0;
        while i < n {
            while i < n && nums[i] != 1 { i += 1; }
            let j = i;
            while i < n && nums[i] == 1 { i += 1; }
            ans = ans.max(i - j);
        }
        ans as i32
    }
}
// @lc code=end

