/*
 * @lc app=leetcode id=1855 lang=rust
 *
 * [1855] Maximum Distance Between a Pair of Values
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n: usize = nums1.len();
        let mut ans: i32 = 0;
        let mut i: usize = 0;
        for (j, &y) in nums2.iter().enumerate() {
            while i < n && nums1[i] > y {
                i += 1;
            }
            if i == n {
                break;
            }
            ans = ans.max((j as i32) - (i as i32));
        }
        ans
    }
}
// @lc code=end

