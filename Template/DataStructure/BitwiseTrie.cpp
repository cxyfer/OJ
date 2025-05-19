#include <bits/stdc++.h>
using namespace std;

/*
Bitwise Trie

Example:
- CSES-1655 Maximum Xor Subarray
*/

class TrieNode {
public:
    TrieNode* ch[2];
    TrieNode() {
        ch[0] = ch[1] = nullptr;
    }
};

class BitwiseTrie {
public:
    TrieNode* root;
    int B;
    BitwiseTrie(int bitlen = 30) {
        root = new TrieNode();
        B = bitlen;
    }

    void insert(int x) {
        TrieNode* node = root;
        for (int i = B; i >= 0; i--) {
            int b = (x >> i) & 1;
            if (node->ch[b] == nullptr)
                node->ch[b] = new TrieNode();
            node = node->ch[b];
        }
    }

    int max_xor(int x) {
        TrieNode* node = root;
        int res = 0;
        for (int i = B; i >= 0; i--) {
            int b = (x >> i) & 1;
            if (node->ch[b ^ 1] != nullptr) {
                res |= (1 << i);
                node = node->ch[b ^ 1];
            } else {
                node = node->ch[b];
            }
        }
        return res;
    }
        
};