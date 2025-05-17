def decimal_translator_2(number, base):
    number = str(number).upper()
    result = 0
    for ch in number:
        if '0' <= ch <= '9':
            digit = ord(ch) - ord('0')
        elif 'A' <= ch <= 'Z':
            digit = ord(ch) - ord('A') + 10
        else:
            return None
        if digit >= base:
            return None
        result = result * base + digit
    return result

print(decimal_translator_2("1Z", 36))
print(decimal_translator_2("1A0", 9))