import requests
import json


def get_driver_standings(prev=None):
    standings = []
    if prev == None:
        data = requests.get("https://ergast.com/api/f1/current/driverStandings.json")
    else:
        data = requests.get(f"https://ergast.com/api/f1/{prev}/driverStandings.json")
    names = data.json()["MRData"]["StandingsTable"]["StandingsLists"][0]
    for name in names["DriverStandings"]:
        standings.append(
            (
                f'{name["Driver"]["givenName"]} {name["Driver"]["familyName"]}: {name["points"]} points'
            )
        )
    return "\n\n".join(standings)


def get_constructor_standings(prev=None):
    standings = []
    if prev == None:
        data = requests.get(
            "https://ergast.com/api/f1/current/constructorStandings.json"
        )
    else:
        data = requests.get(
            f"https://ergast.com/api/f1/{prev}/constructorStandings.json"
        )
    names = data.json()["MRData"]["StandingsTable"]["StandingsLists"][0]
    for name in names["ConstructorStandings"]:
        standings.append((f'{name["Constructor"]["name"]}: {name["points"]} points'))
    return "\n\n".join(standings)


def get_race_season(prev=None):
    season = []
    if prev == None:
        data = requests.get("https://ergast.com/api/f1/current.json")
    else:
        data = requests.get(f"https://ergast.com/api/f1/{prev}.json")
    names = data.json()["MRData"]["RaceTable"]
    for name in names["Races"]:
        season.append(
            f'{name["round"]}  {name["raceName"]} -- {name["Circuit"]["Location"]["country"]}'
        )
    return "\n\n".join(season)


def get_race_schedule(round=None, sprint=None):
    if round == None:
        data = requests.get(f"https://ergast.com/api/f1/current/next.json")
    else:
        data = requests.get(f"https://ergast.com/api/f1/current/{round}.json")
    try:
        if data.json()["MRData"]["RaceTable"]["Races"][0]["Sprint"]:
            sprint = True
    except KeyError:
        sprint = False
    current_season = data.json()["MRData"]["RaceTable"]["Races"][0]["season"]
    current_round = data.json()["MRData"]["RaceTable"]["Races"][0]["round"]
    race_name = data.json()["MRData"]["RaceTable"]["Races"][0]["raceName"]
    fp1_date = data.json()["MRData"]["RaceTable"]["Races"][0]["FirstPractice"]["date"]
    fp1_time = data.json()["MRData"]["RaceTable"]["Races"][0]["FirstPractice"]["time"]
    fp2_date = data.json()["MRData"]["RaceTable"]["Races"][0]["SecondPractice"]["date"]
    fp2_time = data.json()["MRData"]["RaceTable"]["Races"][0]["SecondPractice"]["time"]
    qualifying_date = data.json()["MRData"]["RaceTable"]["Races"][0]["Qualifying"][
        "date"
    ]
    qualifying_time = data.json()["MRData"]["RaceTable"]["Races"][0]["Qualifying"][
        "time"
    ]
    race_date = data.json()["MRData"]["RaceTable"]["Races"][0]["date"]
    race_time = data.json()["MRData"]["RaceTable"]["Races"][0]["time"]
    if sprint == False:
        fp3_date = data.json()["MRData"]["RaceTable"]["Races"][0]["ThirdPractice"][
            "date"
        ]
        fp3_time = data.json()["MRData"]["RaceTable"]["Races"][0]["ThirdPractice"][
            "time"
        ]
        return f"Season: {current_season}\nRound: {current_round}\nRace: {race_name}\
                \n\nFP1 date: {fp1_date}\nFP1 time: {fp1_time}\n\nFP2 date: {fp2_date}\nFP2 time: {fp2_time}\
                \n\nFP3 date: {fp3_date}\nFP3 time: {fp3_time}\n\nQualifying date: {qualifying_date}\
                \nQualifying time: {qualifying_time}\n\nGrand Prix date: {race_date}\nGrand Prix time: {race_time}"
    elif sprint == True:
        sprint_date = data.json()["MRData"]["RaceTable"]["Races"][0]["Sprint"]["date"]
        sprint_time = data.json()["MRData"]["RaceTable"]["Races"][0]["Sprint"]["time"]
        return f"Season: {current_season}\nRound: {current_round}\nRace: {race_name}\
                \n\nFP1 date: {fp1_date}\nFP1 time: {fp1_time}\n\nQualifying date: {qualifying_date}\
                \nQualifying time: {qualifying_time}\n\nFP2 date: {fp2_date}\nFP2 time: {fp2_time}\
                \n\nSprint date: {sprint_date}\nSprint time: {sprint_time}\
                \n\nGrand Prix date: {race_date}\nGrand Prix time: {race_time}"


def get_race_results(prev=None):
    results = []
    if prev == None:
        data = requests.get("https://ergast.com/api/f1/current/last/results.json")
    else:
        data = requests.get(f"https://ergast.com/api/f1/current/{prev}/results.json")
    names = data.json()["MRData"]["RaceTable"]["Races"][0]
    round = data.json()["MRData"]["RaceTable"]["Races"][0]["round"]
    race = data.json()["MRData"]["RaceTable"]["Races"][0]["raceName"]
    results.append(f"Round: {round}")
    results.append(race)
    for name in names["Results"]:
        results.append(
            f'{name["position"]} {name["Driver"]["familyName"]} {name["points"]}'
        )
    return "\n\n".join(results)


def get_teams():
    drivers = []
    constructors = []
    data = requests.get("https://ergast.com/api/f1/current/driverStandings.json")
    names = data.json()["MRData"]["StandingsTable"]["StandingsLists"][0]
    for name in names["DriverStandings"]:
        drivers.append(f'{name["Driver"]["givenName"]} {name["Driver"]["familyName"]}')
    for name in names["DriverStandings"]:
        constructors.append(f'{name["Constructors"][0]["name"]}')
    teams = dict(zip(drivers, constructors))
    by_driver_name = []
    for team in sorted(teams.keys()):
        by_driver_name.append(f"{team}: {teams[team]}")
    return "\n\n".join(by_driver_name)


def get_help():
    return f"List of bot commands:\
            \n\n'$hello': Welcome message\
            \n\n'$driver': Current driver standings. Append '-YYYY' where 'YYYY' is a year between 1950 - current season.\
            \n\n'$constructor': Current constructor standings. Append '-YYYY' where 'YYYY' is a year between 1958 - current season.\
            \n\n'$season': Current season races. Append '-YYYY' where 'YYYY' is a year between 1950 - current season.\
            \n\n'$schedule': Next race schedule. Append '-X' where 'X' is the round of the current season you wish to view the schedule of.\
            \n\n'$result': Most recent race results. Append '-X' where 'X' is the round of the current season you wish to view the results of.\
            \n\n'$team': Current driver pairings on the grid ordered by driver names (first)."
