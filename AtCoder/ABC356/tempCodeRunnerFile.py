            N2 = (N - (1 << i)) | mask
            x = ((N2 >> (i + 1)) << i) | (N2 & mask)
            ans = (ans + x + 1) % MOD