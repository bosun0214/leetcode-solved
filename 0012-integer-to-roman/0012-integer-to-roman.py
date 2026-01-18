class Solution:
    def intToRoman(self, num: int) -> str:
        RomanDict = {}
        RomanDict[1] = 'I'
        RomanDict[5] = 'V'
        RomanDict[10] = 'X'
        RomanDict[50] = 'L'
        RomanDict[100] = 'C'
        RomanDict[500] = 'D'
        RomanDict[1000] = 'M'
        
        check = [[], [1],[1,1],[1,1,1],[1,5],[5],[5,1],[5,1,1],[5,1,1,1],[1,10]]
        answer = ''
        keys = list(RomanDict.keys())
        numlist = list(map(int, str(num)))
        for i in range(len(numlist)):
            checklist = check[numlist[i]]
            tmp = ''
            for c in checklist:
                tmp += RomanDict[c*10**(len(numlist)-i-1)]
            answer += tmp
        return answer