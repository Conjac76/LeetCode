class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading/trailing whitespace

        if not s:
            return 0

        sign = 1
        i = 0

        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            i += 1

        result = 0

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Apply bounds on the result
        if result < -2147483648:
            return -2147483648
        elif result > 2147483647:
            return 2147483647

        return result