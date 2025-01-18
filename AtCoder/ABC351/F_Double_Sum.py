"""
    BIT(Fenwick Tree)
"""

class BIT:
    def __init__(self, n):
        self.d = [0] * (n + 1)
        
    def ins(self, x, v):
        while x < len(self.d):
            self.d[x] += v
            x += x & -x
            
    def qq(self, x):
        res = 0
        while x:
            ret += self.d[x]
            x -= x & -x
        return res
# #include<iostream>
# #include<algorithm>
# #include<vector>
# #define SZ(X) ((int)(X).size())
# using namespace std;
# struct BIT {
#     vector<long long> d;
#     void init(int n) {
#         d.resize(n + 1);
#     }
#     void ins(int x, long long v) {
#         for(; x < d.size(); x += x & -x) {
#             d[x] += v;
#         }
#     }
#     long long qq(int x) {
#         long long ret = 0;
#         for(; x; x -= x & -x) {
#             ret += d[x];
#         }
#         return ret;
#     }
# } bit[2];
# int main() {
#     cin.tie(0);
#     ios_base::sync_with_stdio(false);
#     int N;
#     cin >> N;
#     vector<int> A(N);
#     for(int i = 0; i < N; i++) {
#         cin >> A[i];
#     }
#     vector<int> tmp(A);
#     sort(tmp.begin(), tmp.end());
#     bit[0].init(N);
#     bit[1].init(N);
#     long long ans = 0;
#     for(int x: A) {
#         int p = lower_bound(tmp.begin(), tmp.end(), x) - tmp.begin() + 1;
#         int num = bit[0].qq(p);
#         ans += num * 1ll * x - bit[1].qq(p);
#         bit[0].ins(p, 1);
#         bit[1].ins(p, x);
#     }
#     cout << ans << '\n';
# }