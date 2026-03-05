/*
 * @lc app=leetcode id=198 lang=rust
 *
 * [198] House Robber
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
struct Solution1;
impl Solution1 {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut memo = vec![-1; n];
        fn dfs(i: isize, nums: &[i32], memo: &mut [i32]) -> i32 {
            if i < 0 { return 0; }
            let idx = i as usize;
            if memo[idx] != -1 { return memo[idx]; }
            memo[idx] = std::cmp::max(dfs(i - 2, nums, memo) + nums[idx], dfs(i - 1, nums, memo));
            memo[idx]
        }
        dfs(n as isize - 1, &nums, &mut memo)
    }
}

struct Solution2;
impl Solution2 {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut f = vec![0; n + 2];
        for (i, &x) in nums.iter().enumerate() {
            f[i + 2] = std::cmp::max(f[i] + x, f[i + 1]);
        }
        f[n + 1]
    }
}

struct Solution3;
impl Solution3 {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let (mut f0, mut f1) = (0, 0);
        for x in nums {
            (f0, f1) = (f1, std::cmp::max(f0 + x, f1));
        }
        f1
    }
}

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        // Solution1::rob(nums)
        // Solution2::rob(nums)
        Solution3::rob(nums)
    }
}
// @lc code=end

