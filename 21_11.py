# Numbers At Most N Given Digit Set

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = set(map(int, digits))
        sn = str(n)
        ln = len(sn)

        cnt = 0

        for l in range(1, ln):
            cnt += len(digits) ** l

        for i, dn in enumerate(sn):
            dn = int(dn)
            less_than = sum(d < dn for d in digits)
            cnt += less_than * len(digits) ** (ln - i - 1)
            if dn not in digits: break
            elif i == ln - 1: cnt += 1

        return cnt
        