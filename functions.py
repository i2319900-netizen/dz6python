def sum_distance(from_, to):
    if from_ > to:
        from_, to = to, from_
    return sum(range(from_, to + 1))


def trim_and_repeat(s, offset=0, repetitions=1):
    return s[offset:] * repetitions


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


print(sum_distance(1, 5))   # 1+2+3+4+5 = 15
print(sum_distance(5, 1))   # границы перепутаны местами, результат тот же
print(sum_distance(-3, 2))  # -3-2-1+0+1+2 = -3
print(sum_distance(7, 7))   # обе границы равны -> 7

print(trim_and_repeat("qwerty", 2, 3))  # ertyertyerty
print(trim_and_repeat("qwerty", 2))     # erty (одно повторение по умолчанию)
print(trim_and_repeat("qwerty"))        # qwerty (всё по умолчанию)

print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("qwerty"))                       # False
