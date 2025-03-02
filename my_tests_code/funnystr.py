def funnyString(s):
    re = s[::-1]
    ascii_s = []
    ascii_re = []
    for i in range(len(s)):
        ascii_s.append(ord(s[i]))
        ascii_re.append(ord(re[i]))
    defference_s = []
    defference_re =[]
    for i in range(len(ascii_s)-1):
        defference_s.append(abs(ascii_s[i+1] - ascii_s[i]))
        defference_re.append(abs(ascii_re[i+1] - ascii_re[i]))
    for i in range(len(defference_s)):
        if defference_s[i] != defference_re[i]:
            return 'Not Funny'
    return 'Funny'
