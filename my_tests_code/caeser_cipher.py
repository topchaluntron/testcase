def caesarCipher(s, k):
    sk = ''
    for i in s:
        if i.isalpha():
            if i.isupper():
                sk += chr((ord(i) - ord('A') + k) % 26 + ord('A'))
            else:
                sk += chr((ord(i) - ord('a') + k) % 26 + ord('a'))
        else:
            sk += i
    return sk