#include <bits/stdc++.h>
using namespace std;

using i64 = long long;
const i64 INF = LLONG_MAX / 2;

template <class T>
struct Vec {
    T x, y;

    Vec() = default;
    Vec(T x, T y) : x(x), y(y) {}

    Vec operator+(const Vec& b) const {
        return Vec(x + b.x, y + b.y);
    }

    Vec operator-(const Vec& b) const {
        return Vec(x - b.x, y - b.y);
    }

    T det(const Vec& b) const {
        return x * b.y - y * b.x;
    }

    T dot(const Vec& b) const {
        return x * b.x + y * b.y;
    }
};

template <class T>
class ConvexHull {
public:
    enum class Mode { Min, Max };

    explicit ConvexHull(Mode mode = Mode::Min) : mode(mode) {}

    void add(const Vec<T>& v) {
        if (!hull.empty() && hull.back().x == v.x) {
            if (mode == Mode::Min) {
                if (hull.back().y <= v.y) return;
            } else {
                if (hull.back().y >= v.y) return;
            }
            hull.pop_back();
        }

        while (hull.size() >= 2 && bad(hull[hull.size() - 2], hull.back(), v)) {
            hull.pop_back();
        }

        hull.push_back(v);
    }

    T query(const Vec<T>& p) const {
        int left = 0;
        int right = (int)hull.size() - 2;

        while (left <= right) {
            int mid = (left + right) / 2;

            T curr = p.dot(hull[mid]);
            T next = p.dot(hull[mid + 1]);

            if (mode == Mode::Min) {
                if (curr >= next) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                if (curr <= next) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return p.dot(hull[left]);
    }

private:
    Mode mode;
    vector<Vec<T>> hull;

    bool bad(const Vec<T>& a, const Vec<T>& b, const Vec<T>& c) const {
        T cross = (b - a).det(c - b);

        if (mode == Mode::Min) {
            return cross <= 0;
        } else {
            return cross >= 0;
        }
    }
};

template <class T>
class ConvexHullMono {
public:
    enum class Mode { Min, Max };

    explicit ConvexHullMono(Mode mode = Mode::Min) : mode(mode) {}

    bool empty() const {
        return hull.empty();
    }

    void add(const Vec<T>& v) {
        if (!hull.empty() && hull.back().x == v.x) {
            if (mode == Mode::Min) {
                if (hull.back().y <= v.y) return;
            } else {
                if (hull.back().y >= v.y) return;
            }
            hull.pop_back();
        }

        while (hull.size() >= 2 && bad(hull[hull.size() - 2], hull.back(), v)) {
            hull.pop_back();
        }

        hull.push_back(v);
    }

    T query(const Vec<T>& p) {
        while (hull.size() >= 2 && shouldPopFront(p, hull[0], hull[1])) {
            hull.pop_front();
        }

        return p.dot(hull.front());
    }

private:
    Mode mode;
    deque<Vec<T>> hull;

    bool bad(const Vec<T>& a, const Vec<T>& b, const Vec<T>& c) const {
        T cross = (b - a).det(c - b);

        if (mode == Mode::Min) {
            return cross <= 0;
        } else {
            return cross >= 0;
        }
    }

    bool shouldPopFront(const Vec<T>& p, const Vec<T>& a,
                        const Vec<T>& b) const {
        T va = p.dot(a);
        T vb = p.dot(b);

        if (mode == Mode::Min) {
            return va >= vb;
        } else {
            return va <= vb;
        }
    }
};

class Solution3500 {
public:
    long long minimumCost(vector<int>& nums, vector<int>& cost, int k) {
        int n = nums.size();

        vector<i64> sumNum(n + 1, 0);
        vector<i64> sumCost(n + 1, 0);

        for (int i = 1; i <= n; i++) {
            sumNum[i] = sumNum[i - 1] + nums[i - 1];
            sumCost[i] = sumCost[i - 1] + cost[i - 1];
        }

        vector<i64> f(n + 1, INF), nf(n + 1, INF);
        f[0] = 0;

        i64 ans = INF;
        for (int K = 1; K <= n; K++) {
            fill(nf.begin(), nf.end(), INF);
            // ConvexHull<i64> cht(ConvexHull<i64>::Mode::Min);  // O(log n)
            // query
            ConvexHullMono<i64> cht(
                ConvexHullMono<i64>::Mode::Min);  // O(1) query
            if (f[K - 1] < INF) {
                cht.add(Vec<i64>(sumCost[K - 1], f[K - 1]));
            }
            for (int i = K; i <= n; i++) {
                i64 x = sumNum[i] + (i64)k * K;
                Vec<i64> p(-x, 1);

                i64 best = cht.query(p);
                nf[i] = x * sumCost[i] + best;

                if (i < n && f[i] < INF) {
                    cht.add(Vec<i64>(sumCost[i], f[i]));
                }
            }
            ans = min(ans, nf[n]);
            swap(f, nf);
        }
        return ans;
    }
};