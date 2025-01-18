/*
    tags: string, input, 紫書-Ch3, CPE49
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    int flag = 0;
    while (getline(cin, s)) {
        for (auto &ch: s){
            if (ch == '"') {
                cout << ((flag == 0)? "``" : "''");
                flag = 1 - flag;
            } else {
                cout << ch;
            }
        }
        cout << endl;
    }

    return 0;
}