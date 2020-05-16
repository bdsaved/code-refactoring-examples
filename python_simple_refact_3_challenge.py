#Converting Integer to Roman Numerals

class RomanNumeralConv:
    @staticmethod
    def int_to_Roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(RomanNumeralConv.int_to_Roman(1))
print(RomanNumeralConv.int_to_Roman(4000))
print(RomanNumeralConv.int_to_Roman(9))