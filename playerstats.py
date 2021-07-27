from numpy.core.numeric import False_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from pandas import ExcelWriter
import os

## Common Vizs - PPG vs eFG%,  Make most of the stats here. Only specialized position vizs to be kept in different module
## PG Vizs - PPG,APG Graph. Shooting Graph. Steals Graph.   
## SG Vizs - Shooting Graph, PPG Graph. Steals Graph 
## SF Vizs - Shooting Graph, PPG Graph. Steals Graph, Rebounding Graph, Block Graph, 
## PF Vizs - Rebounding Graph, Block Graph, 
## C Vizs - Rebound graph. Block Graph


## Current Issues
## Special characters in names, not detected. Workaround : Type rest of name or part of the name without the accented letter or copy from online.
## Remove TOT rows from all sheets - Done. Then Save all the vizs under player folder. - Done.
## Check if player folder exists before doing viz. - Done.
## Modularize plots

## Create Player folder
def createFolder(pl):
    if(pl in os.listdir("player stats")):
        print("Player stats are present in ./{}/{}".format("player stats",pl))
    else:
        os.mkdir("./player stats/{}".format(pl))


## Below function to preprocess Player names - Preprocessing done
'''
def newPlayerStats():
    #print(playertotals.head())
    for i in range(len(playertotals)):
        playertotals["Player"][i] = playertotals["Player"][i].split("\\")[0]
        playerpergame["Player"][i] = playerpergame["Player"][i].split("\\")[0]
        playeradvanced["Player"][i] = playeradvanced["Player"][i].split("\\")[0]
        playershooting["Player"][i] = playershooting["Player"][i].split("\\")[0]
    writer = ExcelWriter("newplayerstats.xlsx")
    playertotals.to_excel(writer,"Player Totals",index=False)
    playerpergame.to_excel(writer,"Player per game",index=False)
    playeradvanced.to_excel(writer, "Player Advanced",index=False)
    playershooting.to_excel(writer, "Player Shooting",index=False)
    writer.save()
'''
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


## Remove TOT files - Done
'''
def betterFiles(playertotals,playerpergame,playeradvanced,playershooting):
    indices = []
    for i in range(len(playertotals)):
        if(playertotals["Tm"][i] == "TOT"):
            indices.append(i)    
    playertotals = playertotals.drop(indices)
    playerpergame = playerpergame.drop(indices)
    playeradvanced = playeradvanced.drop(indices)
    playershooting = playershooting.drop(indices)
    writer = ExcelWriter("newplayerstats.xlsx")
    playertotals.to_excel(writer,"Player Totals",index=False)
    playerpergame.to_excel(writer,"Player per game",index=False)
    playeradvanced.to_excel(writer, "Player Advanced",index=False)
    playershooting.to_excel(writer, "Player Shooting",index=False)
    writer.save()
'''



## Common Visualizations
def commonViz(pl,pos,position,ct):
    ## Quick plot of PPG vs FG%
    ## For  positions
    #style.use("seaborn-poster")
    #print(ct)
    if(ct > 1):
        fig,ax = plt.subplots(ct,1,figsize = (12*ct,12*ct),tight_layout = True)
        sns.set_style("darkgrid")
        for i in range(ct):
            posn = playerpergame["Pos"][pos+i]
            sns.scatterplot(data = playerpergame, x = playerpergame[playerpergame["Pos"] == posn]["PTS"],y = playerpergame[playerpergame["Pos"] == posn]["eFG%"]*100,ax = ax[i],color = "g")
            ax[i].set_title("PPG vs eFG Percent for {} in {}".format(playerpergame["Player"][pos+i],playerpergame["Tm"][pos+i]))
            ax[i].scatter(x = playerpergame["PTS"][pos+i],y = playerpergame["eFG%"][pos+i]*100, color = "red")
            ax[i].text(x = playerpergame["PTS"][pos+i]+0.3,y = playerpergame["eFG%"][pos+i]*100+0.3,s=playerpergame.Player[pos+i])
        plt.savefig("player stats/{}/Points vs Efficiency.png".format(pl))
        plt.show()
        plt.close()
    else:
        fig,ax = plt.subplots(ct,1,figsize = (20,20),tight_layout = True)
        sns.set_style("darkgrid")
        posn = playerpergame["Pos"][pos]
        sns.scatterplot(data = playerpergame, x = playerpergame[playerpergame["Pos"] == posn]["PTS"],y = playerpergame[playerpergame["Pos"] == posn]["eFG%"]*100,ax = ax,color = "g")
        ax.set_title("PPG vs eFG Percent for {} in {}".format(playerpergame["Player"][pos],playerpergame["Tm"][pos]))
        ax.scatter(x = playerpergame["PTS"][pos],y = playerpergame["eFG%"][pos]*100, color = "red")
        ax.text(x = playerpergame["PTS"][pos]+0.3,y = playerpergame["eFG%"][pos]*100+0.3,s=playerpergame.Player[pos])
        plt.savefig("player stats/{}/Points vs Efficiency.png".format(pl))
        plt.show()
        plt.close()
    ## Advanced stat Vizs
    if(ct > 1):
        fig,ax = plt.subplots(ct,1,figsize = (12*ct,12*ct),tight_layout = True)
        sns.set_style("darkgrid")
        for i in range(ct):
            posn = playerpergame["Pos"][pos+i]
            sns.scatterplot(data = playeradvanced, x = playeradvanced[playeradvanced["Pos"] == posn]["USG%"],y = playeradvanced[playeradvanced["Pos"] == posn]["TOV%"],ax = ax[i],color = "g")
            ax[i].set_title("USG vs TOV Percent for {} in {}".format(playeradvanced["Player"][pos+i],playeradvanced["Tm"][pos+i]))
            ax[i].scatter(x = playeradvanced["USG%"][pos+i],y = playeradvanced["TOV%"][pos+i], color = "red")
            ax[i].text(x = playeradvanced["USG%"][pos+i]+0.3,y = playeradvanced["TOV%"][pos+i]+0.3, s=playeradvanced.Player[pos+i])
        plt.savefig("player stats/{}/Usage vs Turnover %.png".format(pl))
        plt.show()
        plt.close()
    else:
        fig,ax = plt.subplots(1,1,figsize = (12,12),tight_layout = True)
        sns.set_style("darkgrid")
        posn = playerpergame["Pos"][pos]
        sns.scatterplot(data = playeradvanced, x = playeradvanced[playeradvanced["Pos"] == posn]["USG%"],y = playeradvanced[playeradvanced["Pos"] == posn]["TOV%"],ax = ax,color = "g")
        ax.set_title("USG vs TOV Percent for {} in {}".format(playeradvanced["Player"][pos],playeradvanced["Tm"][pos]))
        ax.scatter(x = playeradvanced["USG%"][pos],y = playeradvanced["TOV%"][pos], color = "red")
        ax.text(x = playeradvanced["USG%"][pos]+0.3,y = playeradvanced["TOV%"][pos]+0.3, s=playeradvanced.Player[pos])
        plt.savefig("player stats/{}/Usage vs Turnover %.png".format(pl))
        plt.show()
        plt.close()
    
    ## FG split for player
    if(playertotals.FG[pos] == 0):
        print("This player has not made a basket in the entire season")
    else:
        fig,axe= plt.subplots(ct,1,figsize = (12*ct,12*ct),tight_layout = True )
        fig.set_facecolor("black")
        labels = playershooting.columns[10:15].str.split("%")
        labels = [list(i) for i in zip(*list(labels))]
        #print(playershooting.head())
        #plt.title(playershooting.values[0][1],color = "w")
        if(ct > 1):
            for i in range(ct):
                axe[i].pie(data=playershooting,labels = labels[0],autopct='%1.2f%%',x = playershooting.values[pos+i][10:15],textprops={'color' : "w",'fontsize':12})
                axe[i].set_title("FG Split for {} in {}".format(playershooting.Player[pos+i],playershooting.Tm[pos+i]),color = "white",fontsize = 12)
        else:        
            axe.pie(data=playershooting,labels = labels[0],autopct='%1.2f%%',x = playershooting.values[pos][10:15],textprops={'color' : "w",'fontsize':12})
            axe.set_title("FG Split for {} in {}".format(playershooting.Player[pos],playershooting.Tm[pos]),color = "white",fontsize = 12)
        #axe[i][j].legend(labels=playershooting.columns[7:12], loc="center left", bbox_to_anchor = (3,3))

        plt.savefig("player stats/{}/Field goal split.png".format(pl),facecolor = "black")
        plt.show()
        plt.close()
    
    ## Modularizing plot making. To be done
    ## def makeplots(ct):

    

if __name__ == "__main__":
    playertotals = pd.read_excel("newplayerstats.xlsx",sheet_name="Player Totals")
    playerpergame = pd.read_excel("newplayerstats.xlsx",sheet_name="Player per game")
    playeradvanced = pd.read_excel("newplayerstats.xlsx",sheet_name="Player Advanced")
    playershooting = pd.read_excel("newplayerstats.xlsx",sheet_name="Player Shooting")
    #betterFiles(playertotals,playerpergame,playeradvanced,playershooting)
    #newPlayerStats()
    print("Enter Player name with first letter capitalized")
    pl = input()
    pos,pl,ct = matchPlayerName(pl)
    createFolder(pl)
    position = findPosition(pos)
    print("His position is : {}".format(position))
    commonViz(pl,pos,position,ct)




