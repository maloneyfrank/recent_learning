import math
class Primes:
    @staticmethod
    def stream():
        yield 2
        yield 3
        yield 5
        yield 7
        sieve = {}
        ps = Primes.stream()
        next(ps)
        next(ps)
        p = 3
        i = 9
        while True:
            s = sieve.get(i)
            if s is not None:
                del sieve[i]
            else:
                if i < p * p:
                    yield i
                    i += 2
                    continue
                s = 2 * p
                p = next(ps)

            k = i + s
            while k in sieve:
                k += s
            sieve[k] = s

            i += 2
