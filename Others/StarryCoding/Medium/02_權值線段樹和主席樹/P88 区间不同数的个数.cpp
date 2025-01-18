#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

/*
   可持久化權值線段樹
*/

template<typename T>
struct SegNode {
   SegNode *ls, *rs; // left child, right child
   T val; // value
   SegNode() : ls(nullptr), rs(nullptr), val(0) {}
};

template<typename T>
class SegmentTree {
public:
   int n;
   vector<T> A;
   vector<SegNode<T>*> roots;

   SegmentTree(vector<T> &A) {
       this->n = A.size();
       this->A = A;
       roots.push_back(new SegNode<T>());
       build(0, n);
   }

   void build(int left, int right) {
       for (int i = 0; i < A.size(); i++) {
           roots.push_back(insert(roots.back(), left, right, A[i]));
       }
   }

   // 在區間 [left, right] 插入值 v，返回新的根節點
   SegNode<T>* insert(SegNode<T> *prev, int left, int right, T v) {
       SegNode<T> *node = new SegNode<T>();
       *node = *prev; // 複製舊的節點
       
       if (left == right) {
           node->val++;
           return node;
       }
       
       int mid = left + ((right - left) >> 1);
       if (v <= mid) {
           if (!prev->ls) prev->ls = new SegNode<T>();
           node->ls = insert(prev->ls, left, mid, v);
       } else {
           if (!prev->rs) prev->rs = new SegNode<T>();
           node->rs = insert(prev->rs, mid + 1, right, v);
       }
       pushup(node);
       return node;
   }

   // Push up node value
   void pushup(SegNode<T> *node) {
       // Update method (Customized)
       node->val = 0;
       if (node->ls) node->val += node->ls->val;
       if (node->rs) node->val += node->rs->val;
   }

   // Query the sum of the interval [l, r] in data range [prev + 1, node]
   T querySum(SegNode<T> *node, SegNode<T> *prev, int left, int right, int l, int r) {
       if (!node) node = new SegNode<T>();
       if (!prev) prev = new SegNode<T>();
       if (l <= left && right <= r) return node->val - prev->val;
       int mid = left + ((right - left) >> 1);
       T res = 0;
       if (l <= mid) res += querySum(node->ls, prev->ls, left, mid, l, r);
       if (r > mid) res += querySum(node->rs, prev->rs, mid + 1, right, l, r);
       return res;
   }

   // Query the k-th smallest element in data range [prev + 1, node]
   T queryKth(SegNode<T> *node, SegNode<T> *prev, int left, int right, int k) {
       if (left == right) return left;
       int mid = left + ((right - left) >> 1);
       int leftCnt = (node->ls ? node->ls->val : 0) - (prev->ls ? prev->ls->val : 0);
       if (prev->ls == nullptr) prev->ls = new SegNode<T>();
       if (prev->rs == nullptr) prev->rs = new SegNode<T>();
       if (k <= leftCnt) {
           return queryKth(node->ls, prev->ls, left, mid, k);
       } else {
           return queryKth(node->rs, prev->rs, mid + 1, right, k - leftCnt);
       }
   }
};

int main() {
   ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
   int n, q; cin >> n >> q;
   vector<int> A(n);
   for (int i = 0; i < n; i++) cin >> A[i];
   unordered_map<int, int> last; // last[x] 表示 x 上一次出現的位置
   vector<int> L(n, 0); // L[i] 表示 A[i] 上一次出現的位置
   for (int i = 0; i < n; i++) {
       L[i] = (last.count(A[i]) ? last[A[i]] : 0);
       last[A[i]] = i + 1;
   }
   SegmentTree<int> seg(L);
   int l, r;
   while (q--) {
       cin >> l >> r;
       cout << seg.querySum(seg.roots[r], seg.roots[l - 1], 0, n, 0, l - 1) << endl;
   }
   return 0;
}