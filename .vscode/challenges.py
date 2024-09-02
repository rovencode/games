def findTheDifference(s: str, t: str) -> str:
        if len(s) > len(t):
            return(s[len(s)-(len(s)-len(t))])
        else:
            return(t[len(t)-(len(t)-len(s))])
print(findTheDifference("abcdefg", "abcd")) # e