#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int w, h;
    while (cin >> w >> h){
        vector<pair<int, int>> data;
        if (w > h) swap(w, h);
        data.push_back({w, h});
        for (int i = 1; i < 6; i++){
            cin >> w >> h;
            if (w > h) swap(w, h);
            data.push_back({w, h});
        }
        bool flag = true;
        sort(data.begin(), data.end());
        for (int i = 0; i < 6; i += 2){
            if (data[i] != data[i+1]){
                flag = false;
                break;
            }
        }
        int a = data[0].first, b = data[0].second, c = data[2].second;
        if (!(a == data[2].first && b == data[4].first && c == data[4].second)){
            flag = false;
        }
        if (flag){
            cout << "POSSIBLE" << endl;
        }else{
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
