#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1500;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL n = N, ans;
    vector<int> primes = {2, 3, 5};
    unordered_set<LL> visited;
    priority_queue<LL, vector<LL>, greater<LL>> hp;
    hp.push(1);
    while (n--) {
        ans = hp.top(); hp.pop();
        for (int p : primes) {
            LL new_ans = ans * p;
            if (visited.find(new_ans) == visited.end()) {
                visited.insert(new_ans);
                hp.push(new_ans);
            }
        }
    }
    cout << "The 1500'th ugly number is " << ans << "." << endl;
    return 0;
}