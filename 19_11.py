class Solution:
    def decodeString(self, s: str) -> str:
        t=''
        for i in range(len(s)):
            if s[i]!=']':
                t+=s[i]
            else:
                f,n='',''
                while t and t[-1]!='[':
                    f,t=t[-1]+f,t[:-1]
                t=t[:-1]
                while t and t[-1] in '0123456789':
                    n,t=t[-1]+n,t[:-1]
                t+=f*int(n)
        return t