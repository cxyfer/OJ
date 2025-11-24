#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

template<typename T, typename Op = function<T(T, T)>>
class SparseTable {
private:
    vector<vector<T>> st;
    Op merge;
    int n;
public:
    SparseTable(const vector<T>& data, Op op) : merge(op), n(data.size()) {
        if (n == 0) return;
        int max_log = __lg(n); 
        st.assign(n, vector<T>(max_log + 1));

        for (int i = 0; i < n; ++i)
            st[i][0] = data[i];

        for (int j = 1; j <= max_log; ++j)
            for (int i = 0; i + (1 << j) <= n; ++i)
                st[i][j] = merge(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
    }

    T query(int L, int R) {  // 0-indexed
        int k = __lg(R - L + 1);
        return merge(st[L][k], st[R - (1 << k) + 1][k]);
    }
};

int main() {
    // Example of usage
    vector<int> A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    auto func = [](int a, int b) { return max(a, b); };
    SparseTable<int, decltype(func)> st(A, func);
    cout << "Max of range [0, 9]: " << st.query(0, 9) << endl;
    cout << "Max of range [0, 4]: " << st.query(0, 4) << endl;
    cout << "Max of range [5, 9]: " << st.query(5, 9) << endl;
    return 0;
}