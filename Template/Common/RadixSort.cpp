#include <bits/stdc++.h>
using namespace std;

/*
 * Radix Sort Template
*/

const int BIT = 32;
const int LEN = 8;
const int SIZE = 1 << LEN;
const int MASK = SIZE - 1;

void radixSort(vector<int>& vec) {
    int n = vec.size();
    vector<int> temp(n);
    vector<int> buckets(SIZE);
    
    for (int shift = 0; shift < BIT; shift += LEN) {
        fill(buckets.begin(), buckets.end(), 0);
        
        for (const auto& x : vec)
            buckets[(x >> shift) & MASK]++;
        
        for (int i = 1; i < SIZE; i++)
            buckets[i] += buckets[i - 1];
        
        for (int i = n - 1; i >= 0; i--)
            temp[--buckets[(vec[i] >> shift) & MASK]] = vec[i];
        
        swap(vec, temp);
    }
}

void radixSort(vector<pair<int, int>>& vec) {
    int n = vec.size();
    vector<pair<int, int>> temp(n);
    vector<int> buckets(SIZE);
    
    for (int shift = 0; shift < BIT; shift += LEN) {
        fill(buckets.begin(), buckets.end(), 0);
        
        for (const auto& x : vec)
            buckets[(x.first >> shift) & MASK]++;
        
        for (int i = 1; i < SIZE; i++)
            buckets[i] += buckets[i - 1];
        
        for (int i = n - 1; i >= 0; i--)
            temp[--buckets[(vec[i].first >> shift) & MASK]] = vec[i];
        
        swap(vec, temp);
    }
}

