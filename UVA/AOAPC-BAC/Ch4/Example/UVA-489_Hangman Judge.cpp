#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int round;
    while (cin >> round && round != -1) {
        cin.ignore(1024, '\n');
        string s, g;
        getline(cin, s);
        getline(cin, g);
        int visited[26] = {0}, cnt = 0, wrong = 0;
        for (char ch : s) {
            int idx = ch - 'a';
            if (!visited[idx]) {
                cnt++;
                visited[idx] = 1;
            }
        }
        for (char ch : g) {
            int idx = ch - 'a';
            if (visited[idx] == 1) {
                visited[idx] = 2;
                cnt--;
                if (cnt == 0) break;
            } else if (visited[idx] == 0) {
                wrong++;
                visited[idx] = -1;
                if (wrong >= 7) break;
            }
        }
        cout << "Round " << round << endl;
        if (wrong >= 7) cout << "You lose." << endl;
        else if (cnt == 0) cout << "You win." << endl;
        else cout << "You chickened out." << endl;  
    }
    return 0;
}