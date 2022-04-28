import sqlite3
from datetime import datetime

today = datetime.now()
day = int(today.strftime("%d"))
month = int(today.strftime("%m"))
year = int(today.strftime("%Y"))
hour = int(today.strftime("%H"))
minute = int(today.strftime("%M"))



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
