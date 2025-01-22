#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;

struct Node {
    int mx, mn;
};

class SegmentTree {
private:
    vector<int> nums;
    vector<Node> tree;
public:
    SegmentTree(vector<int>& nums) {
        int n = nums.size();
        this->nums = vector<int>(n + 1, 0);
        for (int i = 1; i <= n; i++) this->nums[i] = nums[i - 1]; // 1-indexed
        this->tree = vector<Node>(4 * n, Node(-INF, INF));
        build(1, 1, n);
    }

    void build(int o, int left, int right) {
        if (left == right) {
            tree[o] = Node(nums[left], nums[left]);
            return;
        }
        int mid = (left + right) / 2;
        build(2 * o, left, mid);
        build(2 * o + 1, mid + 1, right);
        tree[o] = merge(tree[2 * o], tree[2 * o + 1]);
    }

    Node merge(Node left_child, Node right_child) {
        int mx = max(left_child.mx, right_child.mx);
        int mn = min(left_child.mn, right_child.mn);
        return Node(mx, mn);
    }

    Node query(int o, int left, int right, int l, int r) {
        if (l <= left && right <= r) return tree[o];
        int mid = (left + right) / 2;
        Node ans = Node(-INF, INF);
        if (l <= mid) ans = merge(ans, query(2 * o, left, mid, l, r));
        if (r > mid) ans = merge(ans, query(2 * o + 1, mid + 1, right, l, r));
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n);
    vector<pair<int, int>> pos(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
        pos[i] = {A[i], i + 1};
    }
    sort(pos.begin(), pos.end());

    SegmentTree st(A);

    int ans = INF;
    int l = pos[0].second, r = pos[0].second;
    for (int i = 0; i < n; i++) {
        l = min(l, pos[i].second);
        r = max(r, pos[i].second);
        Node mid = st.query(1, 1, n, l, r);
        Node left = l > 1 ? st.query(1, 1, n, 1, l - 1) : Node(-INF, INF);
        Node right = r < n ? st.query(1, 1, n, r + 1, n) : Node(-INF, INF);
        int mx = max({left.mx, mid.mx * 2, right.mx});
        int mn = min({left.mn, mid.mn * 2, right.mn});
        ans = min(ans, mx - mn);
    }
    cout << ans << '\n';
    return 0;
}