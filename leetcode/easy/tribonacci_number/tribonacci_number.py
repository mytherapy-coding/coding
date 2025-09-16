class Solution:
    def tribonacci(self, n: int) -> int:
        """
        recursion -> time complexity: O(1.8^n), space complexity: O(n)
        ---------
        def trib(n: int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            return trib(n-3) + trib(n-2) + trib(n-1)
        return trib(n)

        memoization -> time complexity: O(n), space complexity: O(n)
        -----------
        @cache
        def trib(n: int) -> int:
            if n == 0:
                return 0
            if n in (1, 2):
                return 1
            return trib(n-3) + trib(n-2) + trib(n-1)
        return trib(n)

        memoization -> time complexity: O(n), space complexity: O(n)
        ------------

        d = {0:0, 1:1, 2:1}
        def trib(n: int) -> int:
            if n not in d:
                d[n] = trib(n-3) + trib(n-2) + trib(n-1)
            return d[n]
        return trib(n)

        DP - dynamic programming(list) -> time complexity: O(n), space complexity: O(n)

        def trib(n: int) -> int:
            t = [0] + [1]*n
            for i in range(3, n+1):
                t[i] = t[i-3] + t[i-2] + t[i-1]
            return t[n]
        return trib(n)

        DP - dynamic programming(list) -> time complexity: O(n), space complexity: O(1)
        """

        def trib(n: int) -> int:
            if n == 0:
                return 0
            t0, t1, t2 = 0, 1, 1
            for i in range(3, n + 1):
                t3 = t2 + t1 + t0
                t0, t1, t2 = t1, t2, t3
            return t2

        return trib(n)
