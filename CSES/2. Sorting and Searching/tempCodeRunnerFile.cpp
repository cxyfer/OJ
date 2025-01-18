/*
    跟 CSES-1660 基本上一樣，只是測試資料卡了雜湊碰撞
*/
#include <bits/stdc++.h>
#include <random>
using namespace std;
using LL = long long;
#define endl '\n'

std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<LL> dis(1, 1e9);
LL BASE = dis(gen);

class Wrapper {
private:
    static const LL BASE;
    LL value; // 新增這行
public:
    Wrapper(LL x) : value(x) {}
    size_t operator()(LL x) const {
        return std::hash<LL>{}((x ^ BASE) + BASE);
    }
    bool operator==(const Wrapper& other) const {
        return value == other.value;
    }
    bool operator<(const Wrapper& other) const {
        return value < other.value;
    }
    LL getValue() const { return value; }
};
const LL Wrapper::BASE = BASE;

namespace std {
    template <>
    struct hash<Wrapper> {
        size_t operator()(const Wrapper& w) const {
            return hash<LL>{}((w.getValue() ^ Wrapper::BASE) + Wrapper::BASE);
        }
    };
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x, a;
    cin >> n >> x;
    LL ans = 0, s = 0;
    unordered_map<Wrapper, int> cnt;
    cnt[Wrapper(0)] = 1;
    for (int i = 0; i < n; i++) {
        cin >> a;
        s += a;
        ans += cnt[Wrapper(s - x)];
        cnt[Wrapper(s)]++;
    }
    cout << ans << endl;
    return 0;
}
