# Team satisfaction discord evaluator

This is a discord Bot created in an objectif to evaluate every Team's member spirit of a group project. The bot sends once a week a group of messages in order to evaluate chosen criterias : Motivation, Workload, Work environment, productivity.

Every member adds an evaluation from 0 to 10. These values are then stored in a JSON and graphical representations can be generated to check the variation of each of these criterias during the project. 

For each member we can generate a graphical representation of the evolution of each criteria during the project :
 - Motivation variation in respect of weeks
 - Workload variation in respect of weeks
 - Productivity variation in respect of weeks
 - Work environment variation in respect of weeks

We can also generate a summary (one graph) of the whole team's performance which is simply the mean of the values entered each week for each criteria.

You should provide the bot with the discord id of the members and of the channel. To get the Discord ID of a channel/User, you need to enable the Developer Mode in Discord. Here's how:

- Open Discord and navigate to the "User Settings" (the gear icon in the bottom left corner of the screen).
- Scroll down to the "Appearance" section and toggle the switch for "Developer Mode".
- With Developer Mode enabled, right-click on the channel/User you want to get the ID for and select "Copy ID". This will copy the channel's Discord ID to your clipboard.


## Used Libraries and API's :


## To do : 
This is a first version of my fully functional bot. It requires some updates primarily for :
-  An automatic addition of Team-members Ids to the script. Currently it should be provided manually to the bot.py script. Check commented elements in code
-  An automatic addition of the channel's Id to the script. Currently it should be provided manually to the bot.py script. Check commented elements in code

## For virtualenv to install all files in the requirements.txt file.

* cd to the directory where requirements.txt is located
* activate your virtualenv
* run: pip install -r requirements.txt in your shell
