#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class TrieNode {
public:
    TrieNode* child[2];
    int cnt;
    bool is_end;
    TrieNode() {
        child[0] = child[1] = nullptr;
        cnt = 0;
        is_end = false;
    }

    void insert(const string& s) {
        TrieNode* node = this;
        for (char ch : s) {
            int idx = ch - '0';
            if (node->child[idx] == nullptr) {
                node->child[idx] = new TrieNode();
            }
            node = node->child[idx];
        }
        node->is_end = true;
        node->cnt += 1;
    }

    bool search_prefix(const string& s) {
        TrieNode* node = this;
        for (char ch : s) {
            if (node->is_end) return true;
            int idx = ch - '0';
            node = node->child[idx];
        }
        return node->cnt > 1;
    }
};
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase = 1;
    string s;
    vector<string> words;
    while (cin >> s) {
        TrieNode root = TrieNode();
        words.clear();
        root.insert(s);
        words.push_back(s);
        while (cin >> s && s != "9") {
            root.insert(s);
            words.push_back(s);
        }
        bool flag = false;
        for (string s : words) {
            if (root.search_prefix(s)) {
                flag = true;
                break;
            }
        }
        if (flag) {
            cout << "Set " << kase << " is not immediately decodable" << endl;
        } else {
            cout << "Set " << kase << " is immediately decodable" << endl;
        }
        kase++;
    }
    return 0;
}