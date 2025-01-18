#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    vector<int> tail = {A[0]};
    for (int i = 1; i < n; i++) {
        if (A[i] > tail.back()) tail.push_back(A[i]);
        else {
            int pos = lower_bound(tail.begin(), tail.end(), A[i]) - tail.begin();
            tail[pos] = A[i];
        }
    }
    cout << tail.size() << endl;
    return 0;
}