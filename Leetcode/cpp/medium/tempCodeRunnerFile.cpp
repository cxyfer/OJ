           for (int k = 1; k <= i - st; k++){
                groups[idx][k] += (i - st) - k + 1; // 長度為 k 的子串有 i - st - k + 1 個
            }