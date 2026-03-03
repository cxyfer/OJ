/*
 * @lc app=leetcode id=1470 lang=rust
 *
 * [1470] Shuffle the Array
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn shuffle(mut nums: Vec<i32>, n: i32) -> Vec<i32> {
        let msk = (1 << 10) - 1;
        let n = n as usize;
        for i in 0..n {
            nums[i << 1] |= (nums[i] & msk) << 10;
            nums[(i << 1) | 1] |= (nums[i + n] & msk) << 10;
        }
        for x in &mut nums { *x >>= 10; }
        nums
    }
}
// @lc code=end

