import sqlite3
from datetime import datetime

today = datetime.now()
day = int(today.strftime("%d"))
month = int(today.strftime("%m"))
year = int(today.strftime("%Y"))
hour = int(today.strftime("%H"))
minute = int(today.strftime("%M"))


def createmanagertable():
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE Manager(
            Manager_id integer PRIMARY KEY,
            Manager_name text NOT NULL
    ) ''')
    con.commit()
    con.close()


def createteamtable():
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    cursor.execute('DROP TABLE Team')
    cursor.execute('''CREATE TABLE Team(
            Manager_id integer NOT NULL,
            Player_id integer NOT NULL
    ) ''')
    con.commit()
    con.close()

def insertmanagers():
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM InTeam')
    cursor.execute('DELETE FROM Team')
    managers = [[1,1144],[1,849],[1,329],[1,263482],[1,83],[1,269],[1,907],[1,276],[1,851],[1,617],[1,30410],[1,636],
                [1,283],[1,532],[1,46815],[1,1863],[1,257],[1,510],[2,399],[2,2006],[2,184226],[2,2918],[4,1460],[4,666],
                [4, 227],[6,184],[6,2286],[6,264],
                [1,39],[1,21090],[1,53],[1,644],[1,1707],[1,10135],[1,1153],[1,898],[1,2780],[1,1856],[1,18813],[1,2937],
                [2,1100],[2,629],[2,278],[2,904],[2,645],[2,1485],[2,853],[2,30558],[2,47296],[2,8],[2,129718],[2,19545],
                [2,2935],[2,45],[2,2054],[2,10316],[2,107],[3,874],[3,306],[3,127],[3,2296],[3,304],[3,882],[3,2290]
                ,[3,18819],[3,1640],[3,17],[3,2678],[3,752],[3,647],[3,318],[3,509],[3,891],[3,790],[3,1709]
                ,[3,501],[3,5],[4,2495],[4,730],[4,280],[4,667],[4,762],[4,1243],[4,2778],[4,181812],[4,511],[4,658],[4,226]
                ,[4,198],[4,567],[4,1166],[4,18778],[4,855],[4,1096],[4,1271],[4,785],[4,2063],[4,2933],[4,1257],[4,14382],
                [4,8489],[4,38735],[4,2472],[4,31009],[5,521],[5,497],[5,19187],[5,909],[5,643],[5,1646],[5,59],[5,135775]
                ,[5,262],[5,2285],[5,538],[5,30533],[5,505],[5,289],[5,30422],[5,18],[5,2701],[5,1323],[5,19194],[5,47300]
                ,[6,154],[6,522],[6,633],[6,631],[6,2986],[6,502],[6,19220],[6,188],[6,19461],[6,18788],[6,266],[6,1859],[6,2923],[6,322]
                ,[6,1557],[6,372],[6,757],[6,186],[6,18846],[6,887],[6,2280],[6,860],[6,22236],[6,2059],[7,759],[7,157]
                ,[7,217],[7,635],[7,29],[7,978],[7,754],[7,1622],[7,331],[7,56],[7,216],[7,875],[7,738],[7,583],[7,9]
                ,[7,1912],[7,1152],[7,194],[7,931],[7,290],[7,1149],[7,33]]
    InTeam = [[0,1144],[0,849],[1,329],[0,263482],[0,83],[1,269],[1,907],[0,276],[1,851],[1,617],[1,30410],[1,636],
                [1,283],[1,532],[1,46815],[1,1863],[1,257],[1,510],
                [0,39],[1,21090],[0,53],[1,644],[0,1707],[0,10135],[0,1153],[0,898],[1,2780],[1,1856],[0,18813],[1,2937],
                [1,1100],[1,629],[1,278],[0,904],[1,645],[1,1485],[1,853],[1,30558],[1,47296],[1,8],[1,129718],[1,19545],
                [1,2935],[1,45],[0,2054],[1,10316],[1,107],[1,874],[1,306],[1,127],[1,2296],[1,304],[1,882],[1,2290]
                ,[1,18819],[1,1640],[0,17],[1,2678],[1,752],[0,647],[1,318],[1,509],[1,891],[1,790],[1,1709]
                ,[1,501],[1,5],[1,2495],[1,730],[1,280],[1,667],[1,762],[1,1243],[0,2778],[0,181812],[1,511],[1,658],[0,226]
                ,[1,198],[1,567],[0,1166],[1,18778],[1,855],[1,1096],[0,1271],[0,785],[1,2063],[0,2933],[0,1257],[0,14382],
                [1,8489],[0,38735],[0,2472],[1,31009],[1,521],[1,497],[1,19187],[1,909],[1,643],[1,1646],[1,59],[1,135775]
                ,[1,262],[1,2285],[1,538],[1,30533],[1,505],[1,289],[0,30422],[1,18],[1,2701],[0,1323],[1,19194],[1,47300]
                ,[1,154],[1,522],[1,633],[1,631],[1,2986],[1,502],[0,19220],[1,188],[0,19461],[1,18788],[1,266],[1,1859]
                ,[0,1557],[1,372],[0,757],[1,186],[0,18846],[1,887],[0,2280],[0,860],[0,22236],[0,2059],[1,759],[1,157]
                ,[1,217],[1,635],[1,29],[1,978],[1,754],[1,1622],[1,331],[1,56],[0,216],[1,875],[0,738],[0,583],[1,9]
                ,[1,1912],[1,1152],[1,194],[0,931],[1,290],[1,1149],[1,33],[1,399],[1,2006],[1,184226],[0,2918],[1,1460],[0,666],[1, 227],[1,184],[1,2286],[1,264],[1,2923],[1,322]]


    #for man in mans:
    #    cursor.execute('INSERT INTO Manager VALUES(:Manager_id, :Manager_name)',
    #               {
    #                   "Manager_id": man[0],
    #                   "Manager_name": man[1]
    #              })

    for record in InTeam:

        cursor.execute('INSERT INTO InTeam VALUES(:PlayerId,:InTeam,:GMonth)',
                   {
                       "PlayerId": int(record[1]),
                       "InTeam": record[0],
                       "GMonth": 11
                   })
    for manager in managers:
        cursor.execute('INSERT INTO Team VALUES(:Manager_id,:Player_id)',
                       {
                           "Manager_id": manager[0],
                           "Player_id": manager[1]
                       })

    cursor.execute('SELECT Count(*) FROM InTeam WHERE InTeam =1')
    count = cursor.fetchall()
    print(count)
    con.commit()
    con.close()

def idtoname(p_id):
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    cursor.execute('SELECT p.Name FROM Player p WHERE p.Player_id ='+str(p_id))
    P_name = cursor.fetchone()
    con.commit()
    con.close()
    if(P_name is None):
        P_name = 'No Records'
    else:
        P_name = P_name[0]
    return P_name

def nametoid(p_name):
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    cursor.execute('SELECT p.Player_id FROM Player p WHERE p.Name ="'+str(p_name)+'"')
    id = cursor.fetchone()
    con.commit()
    con.close()
    if(id is None):
        id = 'No Records'
    else:
        id = id[0]
    return id
#idtoname(1)

def manageridtoplayersid(Manager_id):
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    cursor.execute('SELECT t.Player_id FROM Team t WHERE t.Manager_id = '+str(Manager_id))
    playerslist = cursor.fetchall()
    playerlist=[]
    for players in playerslist:
        playerlist.append([players[0],idtoname(players[0])])
    con.commit()
    con.close()
    return playerlist

#print(manageridtoplayersid(1))

def selection(teamlist):
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    for record in teamlist:

        cursor.execute('INSERT INTO InTeam VALUES(:PlayerId,:InTeam,:GMonth)',
                   {
                       "PlayerId": int(nametoid(record[0])),
                       "InTeam": record[1],
                       "GMonth": 3
                   })
    con.commit()
    con.close()
    print('successful')

def view():
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    cursor.execute('SELECT Count(*) FROM Team')
    count = cursor.fetchall()
    print(count)
    con.commit()
    con.close()


#createmanagertable()
#createteamtable()
#insertmanagers()
#view()


def totalapicalls():
    con = sqlite3.connect('JH_database.db')
    cursor_1 = con.cursor()
    cursor_1.execute('SELECT Count(day) FROM APICALLS WHERE Day=' + str(day))
    count = cursor_1.fetchone()
    con.commit()
    con.close()
    return count[0]


def api_call_limit_exceeded():
    con = sqlite3.connect('JH_database.db')
    cursor_1 = con.cursor()
    cursor_1.execute('SELECT Count(day) FROM APICALLS WHERE Day=' + str(day))
    count = cursor_1.fetchone()
    con.commit()
    con.close()
    if count[0] >= 550:
        return True
    else:
        return False


def clear_previous_api_call_data():
    try:
        con = sqlite3.connect('JH_database.db')
        cursor_1 = con.cursor()
        cursor_1.execute("DELETE FROM APICALLS WHERE Day <> " + str(day))
        cursor_1.execute("DELETE FROM APICALLS WHERE Month <> " + str(month))
        cursor_1.execute("DELETE FROM APICALLS WHERE Year <> " + str(year))
        con.commit()
        con.close()

    except Exception:
        print("Previous Values Not Cleared")


def get_curr_index(array_length):
    con = sqlite3.connect('JH_database.db')
    cursor_1 = con.cursor()
    for curr_index in range(0, array_length - 1):
        cursor_1.execute(
            'SELECT Count(day) FROM APICALLS WHERE Day=' + str(day) +' AND Month = '+str(month) +' AND Year = '+str(year)+' AND curr_index =' + str(curr_index))
        count = cursor_1.fetchone()
        if count[0] <= 89:
            con.commit()
            con.close()
            return curr_index
    return curr_index+1


def insert_api_call(num, curr_index):
    con = sqlite3.connect('JH_database.db')
    cursor_1 = con.cursor()
    cursor_1.execute("INSERT INTO APICALLS VALUES (:Day,:Month,:Year,:Hour,:Minute,:Api_call,:curr_index)",
                     {
                         "Day": day,
                         "Month": month,
                         "Year": year,
                         "Hour": hour,
                         "Minute": minute,
                         "Api_call": num,
                         "curr_index": curr_index
                     })
    con.commit()
    con.close()


def insertmatches(match_details):
    print("matches", match_details)
    con = sqlite3.connect('EFFDB.db')
    cursor_1 = con.cursor()
    cursor_1.execute('''INSERT INTO Matches VALUES (:Fixture_id, :Home_id, :Away_id, :Referee, :Date, :Month,
                        :Year, :Venue_id, :Match_status, :League_id, :League_round, :Season, :H_Goals, :A_Goals)''',
                     {
                         'Fixture_id': match_details[0],
                         'Home_id': match_details[17],
                         'Away_id': match_details[20],


                         'Referee': match_details[5],
                         'Date': match_details[2],
                         'Month': match_details[3],
                         'Year': match_details[4],
                         'Venue_id': match_details[6],
                         'Match_status': match_details[9],
                         'League_id': match_details[10],
                         'League_round': match_details[12],
                         'Season': match_details[16],
                         'H_Goals': match_details[23],
                         'A_Goals': match_details[24]
                     }
                     )
    con.commit()
    con.close()
def insert_teams(match_details):
    con = sqlite3.connect('EFFDB.db')
    cursor_1 = con.cursor()
    cursor_1.execute('''INSERT INTO Teams VALUES (:Team_id, :Name, :Logo)''',
                     {
                         'Team_id': match_details[0],
                         'Name': match_details[1],
                         'Logo': match_details[2]
                     })
    con.commit()
    con.close()


def insertvenue(match_details):
    con = sqlite3.connect('EFFDB.db')
    cursor_1 = con.cursor()
    cursor_1.execute('''INSERT INTO VENUE VALUES (:Venue_id, :Name, :City)''',
                     {
                         'Venue_id': match_details[0],
                         'Name': match_details[1],
                         'City': match_details[2]
                     })
    con.commit()
    con.close()

def createpp():
    playerpricelist=[[45,6,2,2.5],[853,5,2,3],[30558,5,2,4.2],[8,5,2,4.7],[129718,5,2,4.5],[399,8,2,1.5],[278,2,2,13.7],[2054,7,2,2],[1100,2,2,14.2],[2935,6,2,2.5]
                     ,[904,3,2,6],[1485,3,2,11.2],[645,3,2,6.2],[629,2,2,8.7],[22221,5,2,3],[184226,8,2,1.5],[2006,8,2,1.5],[10316,7,2,2.2]
                     ,[107,7,2,2],[2918,8,2,1.5],[742,5,2,3]
                     ,[1460,8,4,1.5],[14382,7,4,2],[169,6,4,2.5],[666,7,4,2],[2495,3,4,6],[198,5,4,3.5],[31009,7,4,2],[38735,7,4,2],[181812,5,4,5],[511,5,4,4]
                     ,[1257,6,4,2.5],[1166,5,4,3],[280,4,4,4.7],[293,6,4,2.5],[855,6,4,3],[567,5,4,4],[18778,5,4,3],[785,6,4,2.5],[2778,5,4,3],[227,10,4,0.5],[730,3,4,5.7],[762,4,4,5.5]
                     ,[658,5,4,3.5],[667,4,4,6.5],[2472,7,4,3.4],[1096,6,4,2.7],[2063,6,4,2.5],[226,5,4,4],[8489,7,4,3],[1243,5,4,3.2]

                     ,[22236,7,6,2],[188,4,6,3.7],[887,6,6,2.5],[154,1,6,10.5],[502,4,6,7.5],[522,2,6,8],[149,6,6,2.5],[264,9,6,1]
                     ,[2280,6,6,2.5],[19220,4,6,6.5],[2986,4,6,5],[2278,6,6,3],[176,6,6,2.5],[860,6,6,2.5],[897,4,6,6],[633,4,6,4]
                     ,[631,4,6,7],[18788,4,6,6],[757,6,6,2.5],[372,6,6,2.5],[266,5,6,3.5],[184,8,6,1.5],[248,5,6,3],[2286,9,6,1],[2059,7,6,3]

                     ,[31,7,1,2],[53,6,1,2.5],[39,6,1,2.9],[851,4,1,3.7],[532,5,1,4],[30410,4,1,6.7],[907,2,1,9.8],[644,6,1,2.9],[510,5,1,3],[257,5,1,4],[898,7,1,2]
                     ,[21090,6,1,2.6],[283,5,1,5],[617,4,1,4.7],[636,4,1,4.2],[1144,8,1,1.5],[1153,7,1,2],[269,6,1,4],[276,2,1,7.5],[10135,7,1,2],[1856,7,1,2.4]
                     ,[1863,5,1,4.5],[329,8,1,1.5],[2780,7,1,3.5],[849,9,1,1],[46815,5,1,3.5],[1707,6,1,2.5],[83,10,1,0.5],[263482,10,1,0.5],[2937,7,1,2]

                     ,[29,3,7,7],[157,2,7,7.5],[583,5,7,3],[1622,4,7,5.2],[875,4,7,4],[194,5,7,3],[9,5,7,5.2],[217,2,7,8.3],[56,4,7,4.7],[33,7,7,2.2],[216,4,7,3.5]
                     ,[978,4,7,4.8],[635,3,7,5],[931,5,7,3.5],[1149,6,7,2.5],[754,4,7,3.5],[759,2,7,8.5],[738,5,7,3.7],[331,4,7,4.2],[290,5,7,4.5],[1152,5,7,3],[1912,5,7,3]

                     ,[30533,5,5,4],[47300,6,5,6.2],[30422,5,5,4],[538,5,5,3.2],[497,3,5,5.5],[505,5,5,3.5],[521,1,5,12],[262,5,5,4.2],[2701,6,5,4]
                     ,[18,6,5,2.5],[2285,5,5,4.2],[19194,6,5,3.1],[59,4,5,4],[289,5,5,5],[909,4,5,6],[643,4,5,5.5],[1323,6,5,2.6]
                     ,[1646,4,5,5.7],[135775,4,5,5.3],[19187,3,5,8.8]

                     ,[1640,4,3,5.5],[874,1,3,13],[127,3,3,4.5],[509,5,3,4.7],[5,7,3,2],[501,6,3,2.5],[17,4,3,3.5],[2290,4,3,4],[306,2,3,10]
                     ,[304,3,3,7.5],[882,4,3,5],[891,5,3,3.7],[2678,4,3,6.7],[752,4,3,3.5],[2296,3,3,4],[647,5,3,3.7],[1709,6,3,2.5],[318,5,3,4.2],[790,6,3,3.1],[18819,4,3,5.7]
                     ]
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    # cursor.execute('''CREATE TABLE PlayerPrice(
    #             Player_id integer PRIMARY KEY,
    #             Pool Integer CHECK(Pool < 11),
    #             Status Integer NOT NULL,
    #             Bought_Price REAL check(Bought_Price>0.4)
    #     ) ''')
    cursor.execute('DELETE FROM PlayerPrice')
    for pp in playerpricelist:
        cursor.execute('INSERT INTO PlayerPrice VALUES(:Player_id,:Pool,:Status,:Bought_Price)',
                       {
                           'Player_id':pp[0],
                           'Pool':pp[1],
                           'Status':pp[2],
                           'Bought_Price':pp[3]
                       })

    cursor.execute('SELECT Status,sum(Bought_Price) FROM PlayerPrice GROUP BY Status')
    count=cursor.fetchall()
    print(count)
    con.commit()
    con.close()


def createpool():
    con = sqlite3.connect('EFFDB.db')
    cursor = con.cursor()
    # cursor.execute('''CREATE TABLE Pool(
    #             Pool integer PRIMARY KEY,
    #             Base_Price Real CHECK(Base_Price > 0.4)
    #     ) ''')
    adams = [[1,5],[2,4.5],[3,4],[4,3.5],[5,3],[6,2.5],[7,2],[8,1.5],[9,1],[10,0.5]]
    for adam in adams:
        cursor.execute('''INSERT INTO Pool VALUES(:Pool, :Base_Price)''',
        {
            'Pool': adam[0],
            'Base_Price':adam[1]
        }
        )
    cursor.execute('SELECT * FROM POOL')
    a=cursor.fetchall()
    print(a)
    con.commit()
    con.close()



def insertleague(match_details):
    con = sqlite3.connect('EFFDB.db')
    cursor_1 = con.cursor()
    cursor_1.execute('''INSERT INTO League VALUES (:League_id, :Name, :Country, :Flag, :Logo)''',
                     {
                         'League_id': match_details[0],
                         'Name': match_details[1],
                         'Country': match_details[4],
                         'Flag': match_details[3],
                         'Logo': match_details[5]
                     })
    con.commit()
    con.close()


def insertplayer(match_details):
    con = sqlite3.connect('EFFDB.db')
    cursor_1 = con.cursor()
    cursor_1.execute('''INSERT INTO Player VALUES(:Player_id, :Name, :Photo, :Number)''',
                     {
                         'Player_id': match_details[0],
                         'Name': match_details[1],
                         'Photo': match_details[2],
                         'Number': match_details[5]
                     })
    con.commit()
    con.close()


def insertplayer_stats(match_details, match_id):
    con = sqlite3.connect('EFFDB.db')
    cursor_1 = con.cursor()
    cursor_1.execute('''INSERT INTO Player_stats VALUES(:Match_id,:Player_id, :Mins, :Position, :Rating,
                        :Offside, :Shots_total, :Shots_on, :Goal, :Assist, :Goal_conceded, :Saves, :Key_Pass,
                        :Tackles, :Blocks, :Interceptions, :Dribbles, :Dribbles_past, :Fouls, :Fouls_drawn,
                        :Y_card, :R_card, :Penalty_won, :Penalty_saved, :Penalty_committed, :Penalty_missed,
                        :Total_points)''',
                     {
                         'Match_id': match_id,
                         'Player_id': match_details[0],
                         'Mins': match_details[3],
                         'Position': match_details[4],
                         'Rating': match_details[6],
                         'Offside': match_details[7],
                         'Shots_total': match_details[9],
                         'Shots_on': match_details[8],
                         'Goal': match_details[9],
                         'Assist': match_details[11],
                         'Goal_conceded': match_details[10],
                         'Saves': match_details[12],
                         'Key_Pass': match_details[13],
                         'Tackles': match_details[14],
                         'Blocks': match_details[15],
                         'Interceptions': match_details[16],
                         'Dribbles': match_details[17],
                         'Dribbles_past': match_details[18],
                         'Fouls': match_details[20],
                         'Fouls_drawn': match_details[19],
                         'Y_card': match_details[21],
                         'R_card': match_details[22],
                         'Penalty_won': match_details[23],
                         'Penalty_saved': match_details[27],
                         'Penalty_committed': match_details[24],
                         'Penalty_missed': match_details[26],
                         'Total_points': match_details[29]
                     })
    con.commit()
    con.close()


def insertplayerdata(playerdata, match_detail):
    try:
        insertmatches(match_detail)
    except sqlite3.Error as error:
        print("ERROR :", error)

    try:
        insertleague(match_detail[10:16])
    except sqlite3.Error as error:
        print("ERROR :", error)

    try:
        insertvenue(match_detail[6:9])
    except sqlite3.Error as error:
        print("ERROR :", error)

    try:
        insert_teams(match_detail[17:20])
        insert_teams(match_detail[20:23])
    except sqlite3.Error as error:
        print("ERROR :", error)

    for player in playerdata:
        try:
            insertplayer_stats(player, match_detail[0])
        except sqlite3.Error as error:
            print("ERROR :", error)

        try:
            insertplayer(player[0:6])
        except sqlite3.Error as error:
            print("ERROR :", error)

#createpp()