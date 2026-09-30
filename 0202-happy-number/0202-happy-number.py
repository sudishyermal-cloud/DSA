class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            digit_sum = 0

            while n > 0:
                digit = n % 10
                digit_sum += digit ** 2
                n = n // 10

            n = digit_sum

        return True
        