#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int x;
    vector<int> arr;
    while (cin >> x) {
        arr.push_back(x);
        sort(arr.begin(), arr.end());
        int n = arr.size();
        if (n % 2 == 0) {
            cout << arr[n / 2 - 1] + (arr[n / 2] - arr[n / 2 - 1]) / 2 << endl;
        } else {
            cout << arr[n / 2] << endl;
        }
    }
    return 0;
}