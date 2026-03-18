/*
 * @lc app=leetcode id=3070 lang=rust
 *
 * [3070] Count Submatrices with Top-Left Element and Sum Less Than k
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
struct Solution1;
impl Solution1 {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let mut ans: i32 = 0;
        let mut s = vec![vec![0; n + 1]; m + 1];
        for (i, row) in grid.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + val;
                if s[i + 1][j + 1] <= k {
                    ans += 1;
                }
            }
        }
        ans
    }
}

struct Solution2;
impl Solution2 {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = grid[0].len();
        let mut ans: i32 = 0;
        let (mut f, mut nf) = (vec![0; n + 1], vec![0; n + 1]);
        for (i, row) in grid.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                nf[j + 1] = f[j + 1] + nf[j] - f[j] + val;
                if nf[j + 1] <= k {
                    ans += 1;
                }
            }
            std::mem::swap(&mut f, &mut nf);
        }
        ans
    }
}

impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        // Solution1::count_submatrices(grid, k)
        Solution2::count_submatrices(grid, k)
    }
}
// @lc code=end

