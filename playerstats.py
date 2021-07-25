import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Common Vizs - eFG%,  
## PG Vizs - PPG,APG Graph. Shooting Graph. Steals Graph.   
## SG Vizs - Shooting Graph, PPG Graph. Steals Graph 
## SF Vizs - Shooting Graph, PPG Graph. Steals Graph, Rebounding Graph, Block Graph, 
## PF Vizs - Rebounding Graph, Block Graph, 
## C Vizs - Rebound graph. Block Graph


## Below function to preprocess Player names

def newPlayerStats():
    #print(playertotals.head())
    for i in range(len(playertotals)):
        playertotals["Player"][i] = playertotals["Player"][i].split("\\")[0]
        playerpergame["Player"][i] = playerpergame["Player"][i].split("\\")[0]
        playeradvanced["Player"][i] = playeradvanced["Player"][i].split("\\")[0]
        playershooting["Player"][i] = playershooting["Player"][i].split("\\")[0]

    return


## Matching Function if input is not the full name
def matchPlayerName(pl):
    f = 0
    for i in range(len(playertotals)):
        if pl in playertotals.Player[i]:
            print("Player found in dataset : {}".format(playertotals.Player[i]))
            f = 1
            break
    if not f:
        print("Error: Player not found!") 
        return None,None
    return i,playertotals.Player[i]


## Returns the playing position of the player
def findPosition(pos,pl):
    return playertotals.Pos[pos]  

## Common Visualizations
#def commonViz(pl):





if __name__ == "__main__":

    playertotals = pd.read_excel("playerstats.xlsx",sheet_name="Player totals")
    playerpergame = pd.read_excel("playerstats.xlsx",sheet_name="Player per game")
    playeradvanced = pd.read_excel("playerstats.xlsx",sheet_name="Player Advanced")
    playershooting = pd.read_excel("playerstats.xlsx",sheet_name="Player Shooting")
    newPlayerStats()
    print("Enter Player name with first letter in Caps")
    pl = input()
    pos,pl = matchPlayerName(pl)
    position = findPosition(pos,pl)
    print("His position is : {}".format(position))
    #commonViz(pl)



