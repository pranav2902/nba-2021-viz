import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

## Common Vizs - eFG%,  
## PG Vizs - PPG,APG Graph. Shooting Graph. Steals Graph.   
## SG Vizs - Shooting Graph, PPG Graph. Steals Graph 
## SF Vizs - Shooting Graph, PPG Graph. Steals Graph, Rebounding Graph, Block Graph, 
## PF Vizs - Rebounding Graph, Block Graph, 
## C Vizs - Rebound graph. Block Graph


## Current Issues
## Special characters in names, not detected. Workaround : Type rest of name or part of the name without the accented letter or copy from online.



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
    ct = (playertotals["Player"] == playertotals.Player[i]).sum()
    if not f:
        print("Error: Player not found!") 
        return None,None
    return i,playertotals.Player[i],ct


## Returns the playing position of the player
def findPosition(pos):
    return playertotals.Pos[pos]  
    


## Common Visualizations
def commonViz(pl,pos,position,ct):
    ## Quick plot of PPG vs FG%
    ## For  positions
    #style.use("seaborn-poster")
    if(ct > 1):
        fig,ax = plt.subplots(ct,1,figsize = (12*ct,12*ct),tight_layout = True)
        sns.set_style("darkgrid")
        for i in range(ct):
            posn = playerpergame["Pos"][pos+i]
            sns.scatterplot(data = playerpergame, x = playerpergame[playerpergame["Pos"] == posn]["PTS"],y = playerpergame[playerpergame["Pos"] == posn]["FG%"]*100,ax = ax[i],color = "g")
            ax[i].set_title("PPG vs FG Percent for {} in {}".format(playerpergame["Player"][pos+i],playerpergame["Tm"][pos+i]))
            ax[i].scatter(x = playerpergame["PTS"][pos+i],y = playerpergame["FG%"][pos+i]*100, color = "red")
        plt.show()
        plt.close()
    else:
        fig,ax = plt.subplots(ct,1,figsize = (20,20),tight_layout = True)
        sns.set_style("darkgrid")
        posn = playerpergame["Pos"][pos]
        sns.scatterplot(data = playerpergame, x = playerpergame[playerpergame["Pos"] == posn]["PTS"],y = playerpergame[playerpergame["Pos"] == posn]["FG%"]*100,ax = ax,color = "g")
        ax.set_title("PPG vs FG Percent for {} in {}".format(playerpergame["Player"][pos],playerpergame["Tm"][pos]))
        ax.scatter(x = playerpergame["PTS"][pos],y = playerpergame["FG%"][pos]*100, color = "red")
        plt.show()
        plt.close()
  



if __name__ == "__main__":

    playertotals = pd.read_excel("playerstats.xlsx",sheet_name="Player totals")
    playerpergame = pd.read_excel("playerstats.xlsx",sheet_name="Player per game")
    playeradvanced = pd.read_excel("playerstats.xlsx",sheet_name="Player Advanced")
    playershooting = pd.read_excel("playerstats.xlsx",sheet_name="Player Shooting")
    newPlayerStats()
    print("Enter Player name with first letter in Caps")
    pl = input()
    pos,pl,ct = matchPlayerName(pl)
    position = findPosition(pos)
    print("His position is : {}".format(position))
    commonViz(pl,pos,position,ct)




