#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    string s, t;
    cin >> n;
    while (n--) {
        cin >> s;
        t = "^";
        for (char ch : s) {
            t += "#";
            t += ch;
        }
        t += "#$";

        vector<int> halfLen(t.size() - 2, 0);
        halfLen[1] = 1;
        int boxM = 0, boxR = 0, hl = 1;
        int max_i = 0;
        for (int i = 2; i < halfLen.size(); i++) {
            hl = 1;
            if (i < boxR) {
                hl = min(halfLen[boxM * 2 - i], boxR - i);
            }
            while (t[i - hl] == t[i + hl]) {
                hl++;
                boxM = i;
                boxR = i + hl;
            }
            halfLen[i] = hl;
            if (hl > halfLen[max_i]) {
                max_i = i;
            }
        }
        cout << halfLen[max_i] - 1 << endl;
    }
    return 0;
}