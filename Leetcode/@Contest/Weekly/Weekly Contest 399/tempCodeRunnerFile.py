        n = len(nums)
        ans = 0
        dp = [0] * max(n, 2)
        dp[0] = max(0, nums[0])
        if n > 1:
            dp[1] = max(dp[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        for pos, x in queries:
            nums[pos] = x
            if pos == 0:
                dp[0] = max(0, nums[0])
                if n > 1:
                    dp[1] = max(dp[0], nums[1])
            elif pos == 1 and n > 1:
                dp[1] = max(dp[0], nums[1])
            for i in range(max(2, pos), n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            ans = (ans + dp[-1]) % MOD
        
        return ans