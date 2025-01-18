#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int x;
    priority_queue<int> hp1; // max heap, <= median
    priority_queue<int, vector<int>, greater<int>> hp2; // min heap, > median
    while (cin >> x) {
        if (hp1.size() == hp2.size()) {
            if (!hp2.empty() && x > hp2.top()) {
                hp1.push(hp2.top());
                hp2.pop();
                hp2.push(x);
            } else {
                hp1.push(x);
            }
        } else {
            if (x < hp1.top()) {
                hp2.push(hp1.top());
                hp1.pop();
                hp1.push(x);
            } else {
                hp2.push(x);
            }
        }
        if (hp1.size() == hp2.size()) {
            // cout << (hp1.top() + hp2.top()) / 2 << endl;
            cout << hp1.top() + (hp2.top() - hp1.top()) / 2 << endl; // avoid overflow
        } else {
            cout << hp1.top() << endl;
        }
    }
    return 0;
}