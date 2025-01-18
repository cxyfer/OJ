#include <bits/stdc++.h>
using namespace std;
const int MAXN = 505;
#define endl '\n'

const int DLEN = 4;
const int BASE = pow(10.0, DLEN);

class BigInt {
    vector<int> v;
    int sign;
    int ln;
public:
    BigInt() : sign(1), ln(1) { v.resize(1, 0); }
    BigInt(int n) {
        // Handle negative numbers
        sign = n >= 0 ? 1 : -1;
        n = n >= 0 ? n : -n;
        
        // Handle zero case
        if (n == 0) {
            ln = 1;
            v.resize(1);
            v[0] = 0;
            return;
        }
        
        // Convert to string first for easier processing
        string s = to_string(n);
        ln = (s.length() + DLEN - 1) / DLEN;
        v.resize(ln);
        
        // Process digits in groups of DLEN
        int pos = 0;
        for (int i = s.length() - 1; i >= 0; i -= DLEN) {
            int temp = 0;
            for (int j = max(0, i - DLEN + 1); j <= i; j++) {
                temp = temp * 10 + (s[j] - '0');
            }
            v[pos++] = temp;
        }
    }
    BigInt(const string& s) {
        if (s.empty()) {
            sign = 1;
            ln = 1;
            v.resize(1, 0);
            return;
        }
        
        int start = 0;
        sign = 1;
        if (s[0] == '-') {
            sign = -1;
            start = 1;
        }
        
        ln = (s.length() - start + DLEN - 1) / DLEN;
        v.resize(ln);
        
        int pos = 0;
        for (int i = s.length() - 1; i >= start; i -= DLEN) {
            int val = 0;
            for (int j = max(start, i - DLEN + 1); j <= i; j++) {
                val = val * 10 + (s[j] - '0');
            }
            v[pos++] = val;
        }
        
        while (ln > 1 && v[ln - 1] == 0) {
            ln--;
        }
        v.resize(ln);
    }
    BigInt operator+(const BigInt& other) const {
        // If signs are different, convert to subtraction
        if (sign != other.sign) {
            BigInt temp = other;
            temp.sign = -temp.sign;
            return *this - temp;
        }
        
        // Initialize result
        BigInt res;
        res.sign = sign;  // Same sign as operands
        res.ln = max(ln, other.ln) + 1;  // +1 for possible carry
        res.v.resize(res.ln);
        
        // Add corresponding digits
        int carry = 0;
        for (int i = 0; i < res.ln - 1; i++) {
            int sum = carry;
            if (i < ln) sum += v[i];
            if (i < other.ln) sum += other.v[i];
            
            if (sum >= BASE) {
                carry = 1;
                sum -= BASE;
            } else {
                carry = 0;
            }
            res.v[i] = sum;
        }
        
        // Handle final carry
        res.v[res.ln - 1] = carry;
        
        // Remove leading zeros
        while (res.ln > 1 && res.v[res.ln - 1] == 0) {
            res.ln--;
        }
        res.v.resize(res.ln);
        
        return res;
    }
    
    BigInt operator-(const BigInt& other) const {
        // If signs are different, convert to addition
        if (sign != other.sign) {
            BigInt temp = other;
            temp.sign = -temp.sign;
            return *this + temp;
        }
        
        // Compare absolute values
        bool swapped = false;
        const BigInt *a = this;
        const BigInt *b = &other;
        
        if (abs_less(*this, other)) {
            swap(a, b);
            swapped = true;
        }
        
        // Initialize result
        BigInt res;
        res.sign = swapped ? -sign : sign;
        res.ln = a->ln;
        res.v.resize(res.ln);
        
        // Subtract corresponding digits
        int borrow = 0;
        for (int i = 0; i < res.ln; i++) {
            int diff = a->v[i] - borrow;
            if (i < b->ln) diff -= b->v[i];
            
            if (diff < 0) {
                diff += BASE;  // Changed from 10000 to BASE
                borrow = 1;
            } else {
                borrow = 0;
            }
            res.v[i] = diff;
        }
        
        // Remove leading zeros
        while (res.ln > 1 && res.v[res.ln - 1] == 0) {
            res.ln--;
        }
        res.v.resize(res.ln);
        
        // Handle zero case
        if (res.ln == 1 && res.v[0] == 0) {
            res.sign = 1;
        }
        
        return res;
    }

    BigInt operator*(const BigInt& other) const {
        if ((ln == 1 && v[0] == 0) || (other.ln == 1 && other.v[0] == 0)) {
            return BigInt(0);
        }
        
        BigInt res;
        res.sign = sign * other.sign;
        res.ln = ln + other.ln;
        res.v.resize(res.ln, 0);
        
        for (int i = 0; i < ln; i++) {
            if (v[i] == 0) continue;
            long long carry = 0;
            for (int j = 0; j < other.ln || carry; j++) {
                long long cur = carry;
                if (j < other.ln) {
                    cur += (long long)v[i] * other.v[j];
                }
                if (i + j < res.ln) {
                    cur += res.v[i + j];
                }
                
                if (i + j >= res.ln) {
                    res.v.push_back(cur % BASE);
                    res.ln++;
                } else {
                    res.v[i + j] = cur % BASE;
                }
                carry = cur / BASE;
            }
        }
        
        while (res.ln > 1 && res.v[res.ln - 1] == 0) {
            res.ln--;
        }
        res.v.resize(res.ln);
        
        return res;
    }

    friend ostream& operator<<(ostream& out, const BigInt& num) {
        if (num.sign == -1) out << '-';
        
        // Print first group without leading zeros
        out << num.v[num.ln - 1];
        
        // Print remaining groups with leading zeros
        for (int i = num.ln - 2; i >= 0; i--) {
            out << setfill('0') << setw(DLEN) << num.v[i];
        }
        return out;
    }

    BigInt abs() const {
        BigInt res = *this;
        res.sign = 1;
        return res;
    }

private:
    // Helper function to compare absolute values
    static bool abs_less(const BigInt& a, const BigInt& b) {
        if (a.ln != b.ln) return a.ln < b.ln;
        for (int i = a.ln - 1; i >= 0; i--) {
            if (a.v[i] != b.v[i]) {
                return a.v[i] < b.v[i];
            }
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<BigInt> f(n + 1);
    f[0] = f[1] = BigInt(1);
    for (int i = 2; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            f[i] = f[i] + f[j] * f[i - j - 1];
        }
    }
    cout << f[n] << endl;
    return 0;
}