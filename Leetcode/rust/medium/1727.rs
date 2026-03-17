/*
 * @lc app=leetcode id=1727 lang=rust
 *
 * [1727] Largest Submatrix With Rearrangements
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
use itertools::Itertools;

struct Solution1;
impl Solution1 {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let n: usize = matrix[0].len();
        let mut ans: i32 = 0;
        let mut cols: Vec<i32> = vec![0; n];
        for row in matrix {
            for (j, &val) in row.iter().enumerate() {
                if val == 1 {
                    cols[j] += 1;
                } else {
                    cols[j] = 0;
                }
            }
            for (j, &h) in cols.iter().sorted_by(|a, b| b.cmp(a)).enumerate() {
                if h == 0 {
                    break;
                }
                ans = ans.max(h * (j as i32 + 1));
            }
        }
        ans
    }
}

struct Solution2;
impl Solution2 {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let n = matrix[0].len();
        let mut ans: i32 = 0;
        let mut idxs: Vec<usize> = (0..n).collect();
        let mut cols: Vec<i32> = vec![0; n];
        for row in matrix {
            let mut arr1: Vec<usize> = vec![];
            let mut arr2: Vec<usize> = vec![];
            for &idx in idxs.iter() {
                if row[idx] == 1 {
                    cols[idx] += 1;
                    arr1.push(idx);
                } else {
                    cols[idx] = 0;
                    arr2.push(idx);
                }
            }
            idxs = [arr1, arr2].concat();
            for (j, &idx) in idxs.iter().enumerate() {
                if cols[idx] == 0 {
                    break;
                }
                ans = ans.max(cols[idx] * (j as i32 + 1));
            }
        }
        ans
    }
}

impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        // Solution1::largest_submatrix(matrix)
        Solution2::largest_submatrix(matrix)
    }
}
// @lc code=end
