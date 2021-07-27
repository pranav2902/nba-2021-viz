# NBA 2021 Visualizations
This repo consists of:
1. Code to generate CSV file of Player/team/event mentions on the subreddit r/nba over the time duration of the 2020-21 NBA season.
2. Code to visualize the ranking of players in different statistics, among the players in his position.
3. Code to visualize team statistics.

Instructions
1. Run playernews_reddit.py
2. Give the name of the player/team/event you are interested in
3. The CSV file with post information is obtained in playerRedditData folder.


Basic Team Visualizations added:
1. Dunks and Layups vs 3pts Made
2. % of FG taken with distance
3. Assist to Turnover plot
4. Rebound split

To/Do
1. Special characters in names, not detected - Workaround : Type rest of name or part of the name without the accented letter or copy from online.
2. Remove TOT rows from all sheets - Done. Then Save all the vizs under player folder. - Done.
3. Check if player folder exists before doing viz. - Done.
4. Modularize plots 
