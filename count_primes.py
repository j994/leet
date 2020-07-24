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

    def countPrimes(self, n: int) -> int:
        a = self.gen_primes(n)
        return len([x for x in a])


a = Solution()
b = a.countPrimes(1500000)
print(b)
