/*
 * @lc app=leetcode id=3567 lang=rust
 *
 * [3567] Minimum Absolute Difference in Sliding Submatrix
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
use itertools::Itertools;

struct Solution1;
impl Solution1 {
    pub fn min_abs_diff(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let k: usize = k as usize;
        let (m, n): (usize, usize) = (grid.len(), grid[0].len());
        let mut ans: Vec<Vec<i32>> = vec![vec![0; n - k + 1]; m - k + 1];
        for i in 0..=(m - k) {
            for j in 0..=(n - k) {
                let mut arr: Vec<i32> = Vec::with_capacity(k * k);
                for r in i..(i + k) {
                    for c in j..(j + k) {
                        arr.push(grid[r][c]);
                    }
                }
                arr.sort_unstable();
                let mut min_d = i32::MAX;
                for (&x, &y) in arr.iter().tuple_windows() {
                    if x != y {
                        min_d = min_d.min(y - x);
                    }
                }
                ans[i][j] = if min_d != i32::MAX { min_d } else { 0 };
            }
        }
        ans
    }
}

use std::cmp::Reverse;
use std::collections::{BTreeSet, BinaryHeap, HashMap};

impl Solution {
    pub fn min_abs_diff(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let k: usize = k as usize;
        let (m, n): (usize, usize) = (grid.len(), grid[0].len());
        let mut ans: Vec<Vec<i32>> = vec![vec![0; n - k + 1]; m - k + 1];

        // 枚舉上邊界
        for u in 0..=(m - k) {
            // 計數器維護當前窗口內的元素出現次數
            let mut cnt: HashMap<i32, usize> = HashMap::new();
            // 有序集合維護當前窗口內的元素
            let mut sl: BTreeSet<i32> = BTreeSet::new();
            // 懶刪除堆維護最小的 (gap, a, b) 其中 a 和 b 是排序後相鄰的元素
            let mut hp: BinaryHeap<Reverse<(i32, i32, i32)>> = BinaryHeap::new();

            // 判斷 a 和 b 是否在 sl 中相鄰
            let is_valid = |sl: &BTreeSet<i32>, a: i32, b: i32| -> bool {
                if !sl.contains(&a) || !sl.contains(&b) {
                    return false;
                }
                sl.range(a..).nth(1) == Some(&b)
            };

            for right in 0..n {
                // 1. 入窗口
                for i in u..(u + k) {
                    let x = grid[i][right];
                    let count = cnt.entry(x).or_insert(0);
                    *count += 1;
                    if *count == 1 {
                        // 插入新值，會新增兩組 gap 到堆中
                        sl.insert(x);
                        if let Some(&pre) = sl.range(..x).next_back() {
                            hp.push(Reverse((x - pre, pre, x)));
                        }
                        if let Some(&nxt) = sl.range(x..).nth(1) {
                            hp.push(Reverse((nxt - x, x, nxt)));
                        }
                    }
                }

                if right < k - 1 {
                    continue;
                }

                // 2. 更新答案
                if sl.len() >= 2 {
                    // 懶刪除堆，刪除不在 sl 中的 gap
                    while let Some(&Reverse((_, a, b))) = hp.peek() {
                        if is_valid(&sl, a, b) {
                            break;
                        }
                        hp.pop();
                    }
                    if let Some(&Reverse((gap, _, _))) = hp.peek() {
                        ans[u][right - k + 1] = gap;
                    }
                }

                // 3. 出窗口
                for i in u..(u + k) {
                    let y = grid[i][right - k + 1];
                    let count = cnt.get_mut(&y).unwrap();
                    *count -= 1;
                    if *count == 0 {
                        // 刪除舊值，會新增一組 gap 到堆中
                        let pre = sl.range(..y).next_back().copied();
                        let nxt = sl.range(y..).nth(1).copied();
                        if let (Some(pre), Some(nxt)) = (pre, nxt) {
                            hp.push(Reverse((nxt - pre, pre, nxt)));
                        }
                        sl.remove(&y);
                        cnt.remove(&y);
                    }
                }
            }
        }
        ans
    }
}

impl Solution {
    pub fn min_abs_diff(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        // Solution1::min_abs_diff(grid, k)
        Solution2::min_abs_diff(grid, k)
    }
}
// @lc code=end
