class Solution:
    def isValid(self , s: str) -> bool:
        open_bracket=['(','{','[']
        close_bracket=[')','}',']']
        d=dict(zip(close_bracket,open_bracket))
        if(s[0] in close_bracket or s[-1] in open_bracket):
            return False
        index = 0
        result = []
        while(index<len(s)):
            if(s[index] in open_bracket):
                result.append(s[index])

            else:
                need=d[s[index]]
                if(len(result)>0 and result[-1]==need):
                    result.pop()
                else:
                    return False
            index += 1
        if(len(result)==0):
            return True
        else:
            return False
