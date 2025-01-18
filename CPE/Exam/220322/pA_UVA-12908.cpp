#include <bits/stdc++.h>
using namespace std;
const int MAX_S = 1e8 + 5;
#define endl '\n'

void solve1(){ // 1. Simulation
    int n;
    while (cin >> n && n){
        int i = 0, s = 0;
        while (s <= n) s += ++i;
        cout << s-n << ' ' << i << endl;
    }
}

void solve2(){ // 2. Binary Search
    vector<int> acc(1, 0); // acc = [0] + [1, 3, 6, 10, 15, ...] (累積和)
    int i = 0, s = 0;
    while (s <= MAX_S){
        s += ++i;
        acc.push_back(s);
    }
    int n;
    while (cin >> n && n){
        auto it = upper_bound(acc.begin(), acc.end(), n);
        int idx = it - acc.begin();
        cout << *it - n << ' ' << idx << endl;
    }
}

void solve3(){ // 3. Math
    int s;
    while (cin >> s && s){
        int n = (int(sqrt(8*s+1)) - 1) / 2 + 1;
        int x = n * (n + 1) / 2 - s;
        cout << x << ' ' << n << endl;
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    // solve1();
    // solve2();
    solve3();
    return 0;
}