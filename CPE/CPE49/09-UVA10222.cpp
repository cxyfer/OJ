#include <bits/stdc++.h>
using namespace std;
#define endl '\n';

string keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./";

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    int idx;
    while (getline(cin, s)) { // must use getline to read the whole line
        for (char ch : s) {
            idx = keyboard.find(tolower(ch));
            if (idx != -1){
                cout << keyboard[idx - 2];
            }
            else{
                cout << ch;
            }
        }
        cout << endl;
    }
    return 0;
}