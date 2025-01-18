#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string n;
    while (cin >> n && n != "0") {
        int s1 = 0, s2 = 0;
        for (int i = 0; i< n.size(); i++) {
            if (i & 1) s1 += n[i] - '0';
            else s2 += n[i] - '0';
        }
        cout << n << " is " << (abs(s1 - s2) % 11 ? "not " : "") << "a multiple of 11." << endl;
    }
    return 0;
}