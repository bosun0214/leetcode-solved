class Solution:
    def romanToInt(self, s: str) -> int:
        RomanDict = {}
        RomanDict['I'] = 1
        RomanDict['V'] = 5
        RomanDict['X'] = 10
        RomanDict['L'] = 50
        RomanDict['C'] = 100
        RomanDict['D'] = 500
        RomanDict['M'] = 1000

        answer = 0
        i=0
        while i < len(s):
            if i+1 < len(s) and RomanDict[s[i]] < RomanDict[s[i+1]]:
                answer += (RomanDict[s[i+1]]-RomanDict[s[i]])
                i+=2
            else:
                answer += RomanDict[s[i]]
                i+=1
        return answer