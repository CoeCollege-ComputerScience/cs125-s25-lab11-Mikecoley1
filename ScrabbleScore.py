def makeScrabbleDict():
    d = {}
    d[1] = "AEIOULNSTR"
    d[2] = "DG"
    d[3] = "BCMP"
    d[4] = "FHVWY"
    d[5] = "K"
    d[8] = "JX"
    d[10] = "QZ"

    scoreDict = {}
    for k,v in d.items():
        for letter in v:
            scoreDict[letter] = k
    return scoreDict

def scoreWord(word):
    word = word.upper()
    sd = makeScrabbleDict()
    score = 0
    for letter in word:
        score += sd[letter]

    return score

print(scoreWord("lovely"))


# Note - add your code here if you completed the "Competency" option on the quiz
def topNWords(length, numWords):
    print("To do if outlined on quiz")

