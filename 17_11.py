# Mirror Reflection

class Solution:
	def mirrorReflection(self, p: int, q: int) -> int:
		def gcd(p, q):
			if p % q == 0:
				return q

			return gcd(q, p % q)

		if p == q:
			return 1

		lca = p * q // gcd(p, q)
		x, y = lca // q, lca // p
		if x % 2 == 1:
			return y % 2

		return 2 if y % 2 else 1
		