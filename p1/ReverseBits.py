#leetcode 190. Reverse Bits
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = [0] * 32
        k = 0
        while n != 0:
            bits[31 - k] = (n % 2)
            k += 1
            n //= 2
        s = 0

        while len(bits) != 0:
            t = bits.pop()
            if t == 1:
                a = 1
                for i in range(len(bits)):
                    a *= 2
                s += a
        return s

if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(1))