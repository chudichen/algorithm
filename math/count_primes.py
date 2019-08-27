class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        # Create a list of all true values up to n.
        primes = [True] * n
        # initialize the first and second indices to False since 0 and 1 are not prime
        primes[0] = primes[1] = False
        # p is the current number we are on, we start at 2 since this is the first prime
        # count represents the number of primes we have in our list
        p, count = 2, 0

        # We optimize this loop by noticing we only have to iterate to the square of a number and check its primes,
        # checking any further is a waste of time as those numbers will be checked later
        while (p * p) <= n:
            # Check to see if this indict has been marked false if it hasnt lets dive into
            # it and check its multiples crossing them off
            if primes[p]:
                # we start at p*2 and increment by p.
                # Ex: 2 -> we start at 4 and increment by 2... 4,6,8,10....
                # we start at p*2 because everrything before will be checked off later, just another optimization
                for i in range(p * 2, n, p):
                    # check off everything
                    primes[i] = False
            # increment p
            p += 1
        # primes now hold True values for every value that is actually a Prime so just sum those
        return sum(primes)


if __name__ == '__main__':
    res = Solution().countPrimes(5)
    print(res)
