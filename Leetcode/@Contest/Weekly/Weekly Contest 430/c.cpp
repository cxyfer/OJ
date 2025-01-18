class Solution {
public:
    long long numberOfSubsequences(vector<int>& nums) {
        int n = nums.size();
        
        unordered_map<long long, vector<pair<int, int>>> left_pairs;
        for (int p = 0; p < n - 2; p++) {
            for (int r = p + 2; r < n; r++) {
                long long prod = (long long)nums[p] * nums[r];
                left_pairs[prod].push_back({p, r});
            }
        }
        
        unordered_map<long long, map<int, vector<int>>> right_map;
        for (int q = 0; q < n - 2; q++) {
            for (int s = q + 2; s < n; s++) {
                long long prod = (long long)nums[q] * nums[s];
                right_map[prod][q].push_back(s);
            }
        }
        
        for (auto& [prod, q_map] : right_map) {
            for (auto& [q, s_list] : q_map) {
                sort(s_list.begin(), s_list.end());
            }
        }
        
        long long ans = 0;
        for (const auto& [prod, pairs] : left_pairs) {
            if (right_map.find(prod) == right_map.end()) continue;
            
            const auto& q_dict = right_map[prod];
            for (const auto& [p, r] : pairs) {
                int q_min = p + 2;
                int q_max = r - 2;
                if (q_min > q_max) continue;
                
                auto q_start = q_dict.lower_bound(q_min);
                auto q_end = q_dict.upper_bound(q_max);
                
                for (auto it = q_start; it != q_end; ++it) {
                    const auto& s_list = it->second;
                    auto s_it = lower_bound(s_list.begin(), s_list.end(), r + 2);
                    ans += (s_list.end() - s_it);
                }
            }
        }
        return ans;
    }
};