class Solution:
    def toHex(self, num: int) -> str:
        def convertToHex(s):
            k = 3
            total = 0

            for i in s:
                total = total + int(i) * (2 ** k)
                k = k - 1

            if total <= 9:
                return str(total)
            else:
                if total == 10:
                    return 'a'
                elif total == 11:
                    return 'b'
                elif total == 12:
                    return 'c'
                elif total == 13:
                    return 'd'
                elif total == 14:
                    return 'e'
                elif total == 15:
                    return 'f'

        if num == 0:
            return "0"

        if num < 0:
            num = num & 0xffffffff

        binary = ""

        while num > 0:
            t = num % 2
            binary = str(t) + binary
            num = num // 2

        while len(binary) % 4 != 0:
            binary = "0" + binary

        res = ""

        for i in range(0, len(binary), 4):
            s = binary[i:i+4]
            res = res + convertToHex(s)

        res = res.lstrip("0")

        return res