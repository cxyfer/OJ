/*
 * @lc app=leetcode id=2946 lang=rust
 *
 * [2946] Matrix Similarity After Cyclic Shifts
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
struct Solution1;
impl Solution1 {
    pub fn are_similar(mat: Vec<Vec<i32>>, mut k: i32) -> bool {
        let n: usize = mat[0].len();
        let k: usize = (k as usize % n);
        k == 0 || mat.iter().all(|row| {
            *row == [&row[n - k..], &row[..n - k]].concat()
        })
    }
}

struct Solution2;
impl Solution2 {
    pub fn are_similar(mat: Vec<Vec<i32>>, mut k: i32) -> bool {
        mat.iter().all(|row| row.iter().enumerate().all(|(i, &x)| x == row[(i + k as usize) % row.len()]))
    }
}

impl Solution {
    pub fn are_similar(mat: Vec<Vec<i32>>, mut k: i32) -> bool {
        Solution1::are_similar(mat, k)
        // Solution2::are_similar(mat, k)
    }
}
// @lc code=end

