word = "hello"
needle = "ll"

def strStr(word , needle):
    i = 0
    n = len(needle)
    if(word==needle):
        return 0
    while(i+n<=len(word)):
        if(word[i:i+n]==needle):
            return i
        else:
            i += 1
    return -1
