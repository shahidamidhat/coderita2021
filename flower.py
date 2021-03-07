'''As Women's Day is coming, Geek decided to give one flower to each woman he knows.
Geek knows K women. Geek's neighbour has a garden in which there are N flowers and each flower has a beauty associated with it i.e. ith flower has B[i] beauty. Geek wants to pluck exactly K flowers from his neighbour's garden such that the sum of beauties of all flowers he plucked is maximum but to not get caught he can't pluck more than one flower in a row, more formally he can't pluck two flowers if they are adjacent.
Your task is to find maximum sum of beauty of all flowers Geek can get.'''
def dp(self, i, j, N, K, B, cache):
        if j >= K:
            return 0
        if i >= N:
            return -10**15
        if cache[i][j] != -10**18:
            return cache[i][j]
        cache[i][j] = max(B[i] + self.dp(i + 2, j + 1, N, K, B, cache),self.dp(i + 1, j, N, K, B, cache))
        return cache[i][j]
    def maximumBeauty(self, N, K, B):
        cache = [[-10**18 for j in range(K)] for i in range(N)]
        ans = self.dp(0, 0, N, K, B, cache);
        return ans
