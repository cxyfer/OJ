#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int m, n, k, tmp;
    bool flag;
    while (cin >> m >> n) {
        k = 0;
        flag = (m > 1 && n > 1)? true : false;
        if (flag){
            tmp = m;
            while (tmp % n == 0) {
                k++;
                tmp /= n;
            }
            if (tmp != 1) {
                flag = false;
            }
        }
        if (flag) {
            for (int i=k; i>=0; i--) {
                cout << m << (i ? " " : "\n");
                m /= n;
            }
        } else {
            cout << "Boring!" << endl;
        }
    }
    return 0;
}