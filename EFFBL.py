import requests
import math
import DBInterface
from datetime import datetime

today = datetime.now()
day = int(today.strftime("%d"))
month = int(today.strftime("%m"))
year = int(today.strftime("%Y"))
hour = int(today.strftime("%H"))
minute = int(today.strftime("%M"))


key_array_alt1 = ["9e3c092599mshc4ed6c2082ef471p1d46adjsn81d3ca68f92b",'ec33e994a5msh5a847f6eac534c4p144bfajsnb9c356e592f8',
             'fd753f8337msh6768cb09a1571dfp129eb4jsn088b0a565f13',"fc16bc3fcbmsh2bd0c21eb41d819p1f2dc1jsn4a3594b43f68",
             "b30decb8a3msh0e215bf075bcfd9p120b27jsnc33dc960d635"]
key_array = ["371bac7cffmsh31634f82fd36d9ap1a0645jsn6664e16822f2"]
key_array_alt = ['ec33e994a5msh5a847f6eac534c4p144bfajsnb9c356e592f8','9e3c092599mshc4ed6c2082ef471p1d46adjsn81d3ca68f92b'
             "bdfabe5c78msh76b10012304fc3ap15e381jsnb650fc877a9b",
             "8c373e544bmsh1d9d7c59989b976p1b36c5jsn05ba612ac940",
             'fd753f8337msh6768cb09a1571dfp129eb4jsn088b0a565f13', "08f605d0a1msha4d33ad7ecb493fp12dfaajsn91deb60e82"]


def nonetozero(var):
    if var is None:
        return 0
    return var


def concededpoint(position, conceded, timepoints):
    if conceded == 0:
        if position == "F" or position == "M":
            concededp = 3
        elif position == "D":
            concededp = 7
        else:
            concededp = 8

    elif conceded == 1:
        if position == "F" or position == "M":
            concededp = 2
        elif position == "D":
            concededp = 3
        else:
            concededp = 4

    elif conceded == 2:
        if position == "F" or position == "M" or position == "D":
            concededp = 1
        else:
            concededp = 2

    elif conceded == 3:
        if position == "G":
            concededp = 1
        else:
            concededp = 0

    else:
        concededp = 0

    if timepoints == 0:
        return concededp
    else:
        return math.ceil(concededp / 2)


def formatpoints(value):
    if value is None or value <= 2:
        return 0
    elif 2 < value < 5:
        return 1
    elif 4 < value < 7:
        return 2
    else:
        return 3


def playerpoints(playersmatchdata):
    pointarray = []
    for playermatchdata in playersmatchdata:
        pointsarray = []
        mins = playermatchdata[3]
        if mins is None or mins == 0:
            mins = 0
            conceded = 0
        elif mins > 60:
            mins = 4
            conceded = concededpoint(playermatchdata[4], playermatchdata[10], 0)
        else:
            mins = 2
            conceded = concededpoint(playermatchdata[4], playermatchdata[10], 1)
        pointsarray.append(mins)
        pointsarray.append(conceded)

        shotson = playermatchdata[8]
        formatpoints(shotson)
        pointsarray.append(formatpoints(shotson))

        saves = playermatchdata[12]
        formatpoints(saves)
        pointsarray.append(formatpoints(saves))

        keypasses = playermatchdata[13]
        formatpoints(keypasses)
        pointsarray.append(formatpoints(keypasses))

        tackls = playermatchdata[14]
        formatpoints(tackls)
        pointsarray.append(formatpoints(tackls))

        blocks = playermatchdata[15]
        formatpoints(blocks)
        pointsarray.append(formatpoints(blocks))

        interceptions = playermatchdata[16]
        formatpoints(interceptions)
        pointsarray.append(formatpoints(interceptions))

        dribbles = playermatchdata[17]
        formatpoints(dribbles)
        pointsarray.append(formatpoints(dribbles))

        yellowcard = playermatchdata[21]
        if yellowcard is None:
            yellowcard = 0
        else:
            yellowcard *= -2
        pointsarray.append(yellowcard)
        redcard = playermatchdata[22]
        if redcard is None:
            redcard = 0
        else:
            redcard *= -4
        pointsarray.append(redcard)

        missed = playermatchdata[26]
        if missed is None:
            missed = 0
        else:
            missed *= -5
        pointsarray.append(missed)

        saved = playermatchdata[27]

        if saved is None:
            saved = 0
        else:
            saved *= 5
        pointsarray.append(saved)

        position = playermatchdata[4]
        goal = 5
        assist = 5
        if position == 'M':
            assist = 7
        if position == 'F':
            goal = 7

        goals = playermatchdata[9]
        if goals is None:
            goals = 0
            pointsarray.append(goals)
        else:
            goals *= goal
            pointsarray.append(goals)
        goalassist = playermatchdata[11]
        if goalassist is None:
            goalassist = 0
            pointsarray.append(goalassist)
        else:
            goalassist *= assist
            pointsarray.append(goalassist)

        totalpoint = 0

        for point in pointsarray:
            totalpoint += point

        pointsarray.append(totalpoint)
        pointsarray.append(playermatchdata[1])
        pointsarray.append(playermatchdata[28])
        pointarray.append(pointsarray)

    return pointarray


def playerstats(output):
    playersmatchdata = []
    response = output['response']
    team_status = 'H'
    for team in response:
        concededoverride = team['players'][0]['statistics'][0]['goals']['conceded']

        players = team['players']
        for player in players:
            playermatchdata = []
            playermatchdata.append(player['player']['id'])  # 0
            playermatchdata.append(player['player']['name'])  # 1
            playermatchdata.append(player['player']['photo'])  # 2
            playermatchdata.append(nonetozero(player['statistics'][0]['games']['minutes']))  # 3
            playermatchdata.append(player['statistics'][0]['games']['position'])  # 4
            playermatchdata.append(player['statistics'][0]['games']['number'])  # 5
            playermatchdata.append(nonetozero(player['statistics'][0]['games']['rating']))  # 6
            playermatchdata.append(nonetozero(player['statistics'][0]['offsides']))
            playermatchdata.append(nonetozero(player['statistics'][0]['shots']['on']))  # 8
            playermatchdata.append(nonetozero(player['statistics'][0]['goals']['total']))  # 9
            playermatchdata.append(nonetozero(concededoverride))   # 10 concededoverride
            playermatchdata.append(nonetozero(player['statistics'][0]['goals']['assists']))  # 11
            playermatchdata.append(nonetozero(player['statistics'][0]['goals']['saves']))  # 12
            playermatchdata.append(nonetozero(player['statistics'][0]['passes']['key']))  # 13
            playermatchdata.append(nonetozero(player['statistics'][0]['tackles']['total']))  # 14
            playermatchdata.append(nonetozero(player['statistics'][0]['tackles']['blocks']))  # 15
            playermatchdata.append(nonetozero(player['statistics'][0]['tackles']['interceptions']))  # 16
            playermatchdata.append(nonetozero(player['statistics'][0]['dribbles']['success']))  # 17
            playermatchdata.append(nonetozero(player['statistics'][0]['dribbles']['past']))
            playermatchdata.append(nonetozero(player['statistics'][0]['fouls']['drawn']))
            playermatchdata.append(nonetozero(player['statistics'][0]['fouls']['committed']))
            playermatchdata.append(nonetozero(player['statistics'][0]['cards']['yellow']))  # 21
            playermatchdata.append(nonetozero(player['statistics'][0]['cards']['red']))  # 22
            playermatchdata.append(nonetozero(player['statistics'][0]['penalty']['won']))  # 23
            playermatchdata.append(nonetozero(player['statistics'][0]['penalty']['commited']))  # 24
            playermatchdata.append(nonetozero(player['statistics'][0]['penalty']['scored'])) # 25
            playermatchdata.append(nonetozero(player['statistics'][0]['penalty']['missed']))  # 26
            playermatchdata.append(nonetozero(player['statistics'][0]['penalty']['saved'])) # 27
            playermatchdata.append(team_status)
            playersmatchdata.append(playermatchdata)
        team_status = 'A'
    # print(playersmatchdata)
    return playersmatchdata


def playerdataapi(matchId):
    #curr_index = DBInterface.get_curr_index(key_array.__len__())
    if DBInterface.api_call_limit_exceeded():
        return 0

    url = "https://api-football-beta.p.rapidapi.com/fixtures/players"

    querystring = {"fixture": matchId}

    headers = {
        'x-rapidapi-key': "371bac7cffmsh31634f82fd36d9ap1a0645jsn6664e16822f2",
        'x-rapidapi-host': "api-football-beta.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    #DBInterface.insert_api_call(1, curr_index)

    output = response.json()
    #print(output)
    return output


def fixturedataapi(teamid, fromdate, todate):
    #curr_index = DBInterface.get_curr_index(key_array.__len__())
    # ("current index", curr_index)
    # if curr_index == -1:
    #     print('calls_exceeded')
    #     return 0

    url = "https://api-football-beta.p.rapidapi.com/fixtures"

    querystring = {"to": todate, "season": "2021", "from": fromdate, "team": teamid}
    #print(curr_index)
    headers = {
        'x-rapidapi-key': "371bac7cffmsh31634f82fd36d9ap1a0645jsn6664e16822f2",
        'x-rapidapi-host': "api-football-beta.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #DBInterface.insert_api_call(2, curr_index)
    fixtureoutput = response.json()

    matchdetails = []
    #print(fixtureoutput)
    matchresponse = fixtureoutput['response']

    for match in matchresponse:
        matchdetail = []
        matchdetail.append(match['fixture']['id'])  # 0
        matchdetail.append(match['fixture']['date'])  # 1
        date_time_obj = datetime.strptime(match['fixture']['date'], "%Y-%m-%dT%H:%M:%S%z")  # 2
        matchdetail.append(date_time_obj.day)
        matchdetail.append(date_time_obj.month)  # 3
        matchdetail.append(date_time_obj.year)  # 4
        matchdetail.append(match['fixture']['referee'])  # 5
        matchdetail.append(match['fixture']['venue']['id'])
        matchdetail.append(match['fixture']['venue']['name'])  # 7
        matchdetail.append(match['fixture']['venue']['city'])
        matchdetail.append(match['fixture']['status']['short'])  # 9
        matchdetail.append(match['league']['id']) #10
        matchdetail.append(match['league']['name'])  # 11
        matchdetail.append(match['league']['round'])
        matchdetail.append(nonetozero(match['league']['flag']))
        matchdetail.append(match['league']['country'])  # 14
        matchdetail.append(match['league']['logo'])
        matchdetail.append(match['league']['season'])
        matchdetail.append(match['teams']['home']['id'])  # 17
        matchdetail.append(match['teams']['home']['name'])
        matchdetail.append(match['teams']['home']['logo'])  # 19
        matchdetail.append(match['teams']['away']['id'])
        matchdetail.append(match['teams']['away']['name'])
        matchdetail.append(match['teams']['away']['logo'])
        matchdetail.append(match['goals']['home'])
        matchdetail.append(match['goals']['away'])  # 24
        matchdetails.append(matchdetail)

    return matchdetails


def league_match_data(fromdate,todate,league_id):
    #curr_index = DBInterface.get_curr_index(key_array.__len__())
    # ("current index", curr_index)
    # if curr_index == -1:
    #     print('calls_exceeded')
    #     return 0

    url = "https://api-football-beta.p.rapidapi.com/fixtures"

    querystring = {"to": todate, "season": "2021", "from": fromdate, "league" : league_id}
    # print(curr_index)
    headers = {
        'x-rapidapi-key': "371bac7cffmsh31634f82fd36d9ap1a0645jsn6664e16822f2",
        'x-rapidapi-host': "api-football-beta.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    fixtureoutput = response.json()
    matchdetails = []
    print(fixtureoutput)
    matchresponse = fixtureoutput['response']

    for match in matchresponse:
        matchdetail = []
        matchdetail.append(match['fixture']['id'])  # 0
        matchdetail.append(match['fixture']['date'])  # 1
        date_time_obj = datetime.strptime(match['fixture']['date'], "%Y-%m-%dT%H:%M:%S%z")  # 2
        matchdetail.append(date_time_obj.day)
        matchdetail.append(date_time_obj.month)  # 3
        matchdetail.append(date_time_obj.year)  # 4
        matchdetail.append(match['fixture']['referee'])  # 5
        matchdetail.append(match['fixture']['venue']['id'])
        matchdetail.append(match['fixture']['venue']['name'])  # 7
        matchdetail.append(match['fixture']['venue']['city'])
        matchdetail.append(match['fixture']['status']['short'])  # 9
        matchdetail.append(match['league']['id'])  # 10
        matchdetail.append(match['league']['name'])  # 11
        matchdetail.append(match['league']['round'])
        matchdetail.append(nonetozero(match['league']['flag']))
        matchdetail.append(match['league']['country'])  # 14
        matchdetail.append(match['league']['logo'])
        matchdetail.append(match['league']['season'])
        matchdetail.append(match['teams']['home']['id'])  # 17
        matchdetail.append(match['teams']['home']['name'])
        matchdetail.append(match['teams']['home']['logo'])  # 19
        matchdetail.append(match['teams']['away']['id'])
        matchdetail.append(match['teams']['away']['name'])
        matchdetail.append(match['teams']['away']['logo'])
        matchdetail.append(match['goals']['home'])
        matchdetail.append(match['goals']['away'])  # 24
        matchdetails.append(matchdetail)

    return matchdetails


def mainfun():
    # playerstats()
    playerdataapi(592268)

    fixturedataapi(49, "2020-12-14", "2020-12-16")
