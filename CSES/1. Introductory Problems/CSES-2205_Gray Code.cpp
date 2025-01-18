#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

vector<int> gray_code(int n) {
    if (n == 0) {
        return {0};
    }
    vector<int> prev = gray_code(n - 1);
    vector<int> ans;
    for (int x : prev) {
        ans.push_back(x);
    }
    for (int i = prev.size() - 1; i >= 0; i--) {
        ans.push_back((1 << (n - 1)) + prev[i]);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<int> ans = gray_code(n);
    for (int x : ans) {
        cout << bitset<32>(x).to_string().substr(32 - n) << endl;
    }
    return 0;
}