def alternatingCharacters(s):
    delete = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            delete +=1
        else :
            pass
    return delete

