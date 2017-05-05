import json

def hScore(score):

    scoreDict = {}
    scoreDict["Your Score"] = score

    with open("HighScore.txt", "w") as outfile:
        json.dump(scoreDict, outfile)
