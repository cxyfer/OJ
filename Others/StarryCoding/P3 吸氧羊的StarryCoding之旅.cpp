#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n);
    for(int i = 0; i < n; ++ i) cin >> A[i];

    vector<LL> L(n), R(n);
    stack<int> st;
    for(int i = 0; i < n; ++ i) {
        while(!st.empty() && A[st.top()] < A[i]) st.pop();
        L[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }
    while(!st.empty()) st.pop();

    for(int i = n - 1; i >= 0; -- i) {
        while(!st.empty() && A[st.top()] <= A[i]) st.pop();
        R[i] = st.empty() ? n : st.top();
        st.push(i);
    }

    LL ans = 0;
    for(int i = 0; i < n; ++ i) {
        ans += A[i] * (i - L[i]) * (R[i] - i);
    }
    cout << ans << endl;
    return 0;
}