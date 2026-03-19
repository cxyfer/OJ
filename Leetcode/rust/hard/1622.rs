/*
 * @lc app=leetcode id=1622 lang=rust
 *
 * [1622] Fancy Sequence
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
#[derive(Clone)]
pub struct LazySegmentTree<S, F> {
    n: usize,
    val: Vec<S>,
    lazy: Vec<F>,
    op: fn(&S, &S) -> S,
    e: S,
    mapping: fn(&F, &S, usize) -> S,
    composition: fn(&F, &F) -> F,
    id: F,
}

impl<S, F> LazySegmentTree<S, F>
where
    S: Clone,
    F: Clone + PartialEq,
{
    pub fn new(
        n: usize,
        op: fn(&S, &S) -> S,
        e: S,
        mapping: fn(&F, &S, usize) -> S,
        composition: fn(&F, &F) -> F,
        id: F,
    ) -> Self {
        let size = if n == 0 {
            0
        } else {
            1 << (usize::BITS - n.leading_zeros() + 1)
        };
        Self {
            n,
            val: vec![e.clone(); size],
            lazy: vec![id.clone(); size],
            op,
            e,
            mapping,
            composition,
            id,
        }
    }

    pub fn from_slice(
        nums: &[S],
        op: fn(&S, &S) -> S,
        e: S,
        mapping: fn(&F, &S, usize) -> S,
        composition: fn(&F, &F) -> F,
        id: F,
    ) -> Self {
        let n = nums.len();
        let mut tree = Self::new(n, op, e, mapping, composition, id);
        if n > 0 {
            tree.build(1, 1, n, nums);
        }
        tree
    }

    fn build(&mut self, o: usize, left: usize, right: usize, nums: &[S]) {
        if left == right {
            self.val[o] = nums[left - 1].clone();
            return;
        }
        let mid = left + (right - left) / 2;
        self.build(o * 2, left, mid, nums);
        self.build(o * 2 + 1, mid + 1, right, nums);
        self.pushup(o);
    }

    fn pushup(&mut self, o: usize) {
        let left_val = self.val[o * 2].clone();
        let right_val = self.val[o * 2 + 1].clone();
        self.val[o] = (self.op)(&left_val, &right_val);
    }

    fn _update(&mut self, o: usize, left: usize, right: usize, f: &F) {
        let seglen = right - left + 1;
        let current_val = self.val[o].clone();
        self.val[o] = (self.mapping)(f, &current_val, seglen);
        let current_lazy = self.lazy[o].clone();
        self.lazy[o] = (self.composition)(f, &current_lazy);
    }

    fn pushdown(&mut self, o: usize, left: usize, right: usize) {
        if self.lazy[o] == self.id || left == right {
            return;
        }
        let mid = left + (right - left) / 2;
        let f = self.lazy[o].clone();
        self._update(o * 2, left, mid, &f);
        self._update(o * 2 + 1, mid + 1, right, &f);
        self.lazy[o] = self.id.clone();
    }

    fn update(&mut self, o: usize, left: usize, right: usize, l: usize, r: usize, f: &F) {
        if l <= left && right <= r {
            self._update(o, left, right, f);
            return;
        }
        self.pushdown(o, left, right);
        let mid = left + (right - left) / 2;
        if l <= mid {
            self.update(o * 2, left, mid, l, r, f);
        }
        if r > mid {
            self.update(o * 2 + 1, mid + 1, right, l, r, f);
        }
        self.pushup(o);
    }

    fn query(&mut self, o: usize, left: usize, right: usize, l: usize, r: usize) -> S {
        if l <= left && right <= r {
            return self.val[o].clone();
        }
        self.pushdown(o, left, right);
        let mid = left + (right - left) / 2;
        let mut ans = self.e.clone();
        if l <= mid {
            let left_ans = self.query(o * 2, left, mid, l, r);
            ans = (self.op)(&ans, &left_ans);
        }
        if r > mid {
            let right_ans = self.query(o * 2 + 1, mid + 1, right, l, r);
            ans = (self.op)(&ans, &right_ans);
        }
        ans
    }

    pub fn apply(&mut self, l: usize, r: usize, f: F) {
        if self.n == 0 || l > r {
            return;
        }
        self.update(1, 1, self.n, l, r, &f);
    }

    pub fn prod(&mut self, l: usize, r: usize) -> S {
        if self.n == 0 || l > r {
            return self.e.clone();
        }
        self.query(1, 1, self.n, l, r)
    }

    pub fn all_prod(&self) -> S {
        if self.n == 0 {
            return self.e.clone();
        }
        self.val[1].clone()
    }
}

const MOD: i64 = (1e9 as i64) + 7;
const MAX_N: usize = (1e5 as usize) + 5;

fn op(a: &i64, b: &i64) -> i64 {
    (*a + *b) % MOD
}

fn mapping(f: &(i64, i64), x: &i64, seglen: usize) -> i64 {
    let (mul, add) = *f;
    let seglen = seglen as i64;
    ((*x * mul) % MOD + (add * seglen) % MOD) % MOD
}

fn composition(f: &(i64, i64), g: &(i64, i64)) -> (i64, i64) {
    let (mul2, add2) = *f;
    let (mul1, add1) = *g;
    ((mul2 * mul1) % MOD, (mul2 * add1 % MOD + add2) % MOD)
}

struct Fancy1 {
    idx: usize,
    lst: LazySegmentTree<i64, (i64, i64)>,
}
impl Fancy1 {
    fn new() -> Self {
        Self {
            idx: 0,
            lst: LazySegmentTree::new(MAX_N, op, 0, mapping, composition, (1, 0)),
        }
    }

    fn append(&mut self, val: i32) {
        self.idx += 1;
        self.lst.apply(self.idx, self.idx, (1, val as i64));
    }

    fn add_all(&mut self, inc: i32) {
        self.lst.apply(1, self.idx, (1, inc as i64));
    }

    fn mult_all(&mut self, m: i32) {
        self.lst.apply(1, self.idx, (m as i64, 0));
    }

    fn get_index(&mut self, idx: i32) -> i32 {
        let idx = idx as usize;
        if idx >= self.idx {
            return -1;
        }
        self.lst.prod(idx + 1, idx + 1) as i32
    }
}

fn pow(mut base: i64, mut exp: i64, m: i64) -> i64 {
    let mut res = 1;
    base %= m;
    while exp > 0 {
        if (exp & 1 == 1) {
            res = res * base % m;
        }
        base = base * base % m;
        exp >>= 1;
    }
    res
}

struct Fancy2 {
    arr: Vec<i64>,
    mul: i64,
    add: i64,
}

impl Fancy2 {
    fn new() -> Self {
        Self {
            arr: Vec::new(),
            mul: 1,
            add: 0,
        }
    }

    fn append(&mut self, val: i32) {
        let x = (val as i64 - self.add + MOD) % MOD * pow(self.mul, MOD - 2, MOD) % MOD;
        self.arr.push(x);
    }

    fn add_all(&mut self, inc: i32) {
        self.add = (self.add + inc as i64) % MOD;
    }

    fn mult_all(&mut self, m: i32) {
        self.mul = (self.mul * m as i64) % MOD;
        self.add = (self.add * m as i64) % MOD;
    }

    fn get_index(&self, idx: i32) -> i32 {
        let idx = idx as usize;
        if idx >= self.arr.len() {
            return -1;
        }
        ((self.arr[idx] * self.mul + self.add) % MOD) as i32
    }
}

// type Fancy = Fancy1;
type Fancy = Fancy2;
// @lc code=end
