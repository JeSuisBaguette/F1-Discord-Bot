# **F1 Discord Bot**

### **Created by:**
JeSuisBaguette

##  **Project Description:**

This is a discord bot which upon receiving commands, sends a channel text message with information related to the current F1 season or the seasons prior.  

## **File Structure:**

### **Bot.py:**

Contains code that interacts with the Discord API. Houses all functions and classes necessary to make the bot run in context of Discord.

### **Data.py:**

Contains code that queries the API containing all the data parsed and sent through the bot. All data presented is accessed from the [Ergast Developer API](https://ergast.com/mrd/). Functions accomplishing the return of specifc data/statistics from the API is housed here.

### **Requirements.txt:**

Contains the pip-installable libraries and their respective versions used in the project which are required for it to run.

## **Documentation:**

### **Classes and methods:**

The bot.py file subclasses from the Discord Client class and uses async methods to respond to commands issued to the bot in a text channel. All bot commands are prefixed with "$" and additional parameters are designated through the use of "-".

### **Functions:**

Queries to the [Ergast Developer API](https://ergast.com/mrd/) is handled through the use of functions in the data.py file. A brief rundown of the purposes of the functions are provided below:

**get_driver_standings():** 

Returns a list of the current driver's championship standings if no parameters are set. Otherwise, returns the driver's championship standings of the specified season. Valid years are from 1950 onwards until the current season. 

**get_constructor_standings():**

Returns a list of the current constructor's championship standings if no parameters are set. Otherwise, returns the constructor's championship standings of the specified season. Valid years are from 1958 onwards until the current season. 

**get_race_season():**

Retrurns a list of all the races this current season by default. Includes round number, race name, and country. If parameters are specified, the function returns a list of all races held for the season entered. Valid years are from 1950 onwards until the current season. 

**get_race_schedule():**

If no parameters are given, this function returns the schedule of the next race in the surrent season. If the round number is given as a parameter, the schedule for the given round of this season will be returned instead. Unlike the previous functions, the scope of this function is only extended to the current season and not any seasons before it. The schedule is presented in order of UTC time, and is compatible between both normal weekends and sprint weekends. The valid range for this function are the number of rounds that are present in the current season.  

**get_race_results():**

Similar to the get_race_schedule() function, this function is also limited to only the current season. When called with no parameters, the function will return the race results (finishing position, point scored) of the drivers of the most recent race. If a round number is passed in as a parameter, the function will return the race result of the round that has been specified. The valid range for this function are the rounds that have already been completed this season. 

**get_teams():**

This function takes in no additional parameters. The purpose of this function is to return a list of driver names (assorted in alphabetical order by first name) and the constructor that the driver currently drives for.  

**get_help():**

This is a non-API related help function housed in the bot.py file that returns a text stating the way to call the aforementioned functions through commands on Discord, and the specific parameters (if any) which they accept. 

## **Remarks:**

You are free to use the code as you'd like. My intention was to create a bot that is able to provide me with the necessary information I might want to view throughout the season. Special thanks to [Ergast Developer API](https://ergast.com/mrd/) as this project would not have been possible without access to the data. 