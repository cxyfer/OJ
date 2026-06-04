/*
 * @lc app=leetcode id=3751 lang=rust
 *
 * [3751] Total Waviness of Numbers in Range I
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn total_waviness(num1: i32, num2: i32) -> i32 {
        let high: Vec<i32> = num2
            .to_string()
            .bytes()
            .map(|b| (b - b'0') as i32)
            .collect();
        let n: usize = high.len();
        let diff: usize = n - num1.to_string().len();
        let low: Vec<i32> = format!("{:0>width$}", num1.to_string(), width = n)
            .bytes()
            .map(|b| (b - b'0') as i32)
            .collect();
        let mut memo = HashMap::new();

        fn dfs(
            i: usize,
            pre1: i32,
            pre2: i32,
            cnt: i64,
            limit_low: bool,
            limit_high: bool,
            n: usize,
            diff: usize,
            low: &[i32],
            high: &[i32],
            memo: &mut HashMap<(usize, i32, i32, i64, bool, bool), i64>,
        ) -> i64 {
            if i == n {
                return cnt
            }

            let key = (i, pre1, pre2, cnt, limit_low, limit_high);
            if let Some(&value) = memo.get(&key) {
                return value;
            }

            let lo = if limit_low { low[i] } else { 0 };
            let hi = if limit_high { high[i] } else { 9 };
            let mut res = 0;

            if i < diff && limit_low {
                res += dfs(
                    i + 1,
                    pre1,
                    pre2,
                    cnt,
                    limit_low && low[i] == 0,
                    limit_high && high[i] == 0,
                    n,
                    diff,
                    low,
                    high,
                    memo,
                );
            }

            let start = if i < diff && limit_low { 1 } else { lo };
            for d in start..=hi {
                let is_waviness = (pre1 != -1
                    && pre2 != -1
                    && ((pre1 < pre2 && pre2 > d) || (pre1 > pre2 && pre2 < d)))
                    as i64;
                res += dfs(
                    i + 1,
                    pre2,
                    d,
                    cnt + is_waviness,
                    limit_low && d == lo,
                    limit_high && d == hi,
                    n,
                    diff,
                    low,
                    high,
                    memo,
                );
            }

            let value = res;
            memo.insert(key, value);
            value
        }

        dfs(0, -1, -1, 0, true, true, n, diff, &low, &high, &mut memo) as i32
    }
}
// @lc code=end

