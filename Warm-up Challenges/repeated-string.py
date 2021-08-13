def repeatedString(s, n):
    length = len(s)

    a_in_s = s.count('a')
    repeat_times = n // length

    remainder = n % length
    a_in_s_remainder = s[0:remainder].count('a')

    return a_in_s * repeat_times + a_in_s_remainder

s = "abcac"
n = 10
print(repeatedString(s, n))