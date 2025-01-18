#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

string WEEKDAY[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
int DAYS[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int pre_sum[13] = {0}; // prefix sum
int base = 5; // 2011/1/1 is Saturday, so start at Friday

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, m, d;
    cin >> t;
    for (int i = 1; i < 12; i++) {
        pre_sum[i] = pre_sum[i-1] + DAYS[i-1];
    }
    while (t--) {
        cin >> m >> d;
        int day = (base + pre_sum[m-1] + d) % 7;
        cout << WEEKDAY[day] << endl;
    }
    return 0;
}