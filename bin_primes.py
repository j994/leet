class Solution:
    def gen_primes(self, n):
        D = {}
        q = 2
        while q < n:
            if q not in D:
                yield q
                D[q*q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1

    def countPrimeSetBits(self, L: int, R: int) -> int:
        a = self.gen_primes(21)
        primes = [p for p in a]
        print(primes)
        count = 0
        for x in range(L, R + 1):
            if bin(x).count('1') in primes:
                count += 1
        return count


sol = Solution()
b = sol.countPrimeSetBits(567, 607)
print(b)
