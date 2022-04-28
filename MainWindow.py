from tkinter import *
from tkcalendar import *
import datetime
from tkinter import messagebox
import EFFBL
import DBInterface


def mainwindow(root, label, label1, label2):
    label.place(x=0, y=0)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight() - 69))
    print(root.winfo_screenwidth(), root.winfo_screenheight())
    root.configure(bg='black')

    label1.place(x=int(root.winfo_screenwidth() * 0.772), y=int(root.winfo_screenheight() * 0.2305))

    label2.place(x=int(root.winfo_screenwidth() * 0.772), y=int(root.winfo_screenheight() * 0.4))


def forgetpage(label, label1, label2):
    label.place_forget()

    label1.place_forget()

    label2.place_forget()


def matchdatamain(root, label, label1, label2, label3, label4, team_button_array, team_button_frame):
    forgetpage(label, label1, label2)

    label3.place(x=0, y=0)

    label4.place(x=root.winfo_screenwidth() - 200, y=0)
    frame_width_place = int((root.winfo_screenwidth() / 2) - (root.winfo_screenwidth() * 3.5 * 0.078125))
    frame_height_place = int((root.winfo_screenheight() / 2) - (root.winfo_screenwidth() * 2 * 0.078125))
    team_button_frame.place(x=frame_width_place, y=frame_height_place)

    row_count = 0
    column_count = 0

    for team in team_button_array:
        team.grid(row=row_count, column=column_count)
        column_count += 1
        if column_count == 7:
            row_count += 1
            column_count = 0


# to travel back to main page
def backfuntion(label, label1, root, label2, label3, label4, frame):
    label.place_forget()
    label1.place_forget()
    frame.place_forget()
    mainwindow(root, label2, label3, label4)


def detailedwindow(match_detail, root):
    match_details = match_detail[0]
    detailedwin = Toplevel()
    detailedwin.title(" Detailed Window")
    detailedwin.geometry(
        "1240x660+{0}+{1}".format(int((root.winfo_screenwidth() / 2) - 620),
                                  int((root.winfo_screenheight() / 2) - 330)))
    detailedwin.configure(bg="#ffb81d")
    # print((match_detail))
    dvar = str(match_details[2]) + " - " + str(match_details[3]) + " - " + str(match_details[4])
    matchinfo = str(match_details[18]) + " ( " + str(match_details[23]) + " ) vs ( " + str(
        match_details[24]) + " ) " + str(
        match_details[21]) + "\n" + str(dvar) + "\n" + str(match_details[11]) + " - " + str(match_details[12]) + "\n" \
        + str(match_details[5]) + "    " + str(match_details[7])
    match_heading = Label(detailedwin, text=matchinfo, bg="#ffb81d", font=(33))
    match_heading.grid(row=1, column=0, columnspan=4)

    match_detail_frame1 = Frame(detailedwin, bg="#ffb81d")
    match_detail_frame1.grid(row=5, column=1)

    Sr_No = Label(match_detail_frame1, text="Sr.No.", bg="#ffb81d").grid(row=1, column=0)
    Name = Label(match_detail_frame1, text="Name", bg="#ffb81d").grid(row=1, column=1)
    Mins = Label(match_detail_frame1, text="Mins", bg='#ffb81d').grid(row=1, column=2)
    CS = Label(match_detail_frame1, text="CS", bg='#ffb81d').grid(row=1, column=3)
    SHOT = Label(match_detail_frame1, text="SHOT", bg='#ffb81d').grid(row=1, column=4)
    GLS = Label(match_detail_frame1, text="GLS", bg='#ffb81d').grid(row=1, column=5)
    KP = Label(match_detail_frame1, text="KP", bg='#ffb81d').grid(row=1, column=6)
    TKLS = Label(match_detail_frame1, text="TKLS", bg='#ffb81d').grid(row=1, column=7)
    BLK = Label(match_detail_frame1, text="BLK", bg='#ffb81d').grid(row=1, column=8)
    INT = Label(match_detail_frame1, text="INT", bg='#ffb81d').grid(row=1, column=9)
    DRB = Label(match_detail_frame1, text="DRB", bg='#ffb81d').grid(row=1, column=10)
    YC = Label(match_detail_frame1, text="YC", bg='#ffb81d').grid(row=1, column=11)
    RC = Label(match_detail_frame1, text="RC", bg='#ffb81d').grid(row=1, column=12)
    PMSD = Label(match_detail_frame1, text="PMSD", bg='#ffb81d').grid(row=1, column=13)
    PSVD = Label(match_detail_frame1, text="PSVD", bg='#ffb81d').grid(row=1, column=14)
    TGL = Label(match_detail_frame1, text="TGL", bg='#ffb81d').grid(row=1, column=15)
    GLA = Label(match_detail_frame1, text="GLA", bg='#ffb81d').grid(row=1, column=16)
    TOT = Label(match_detail_frame1, text="TOT", bg='#ffb81d').grid(row=1, column=17)

    Sr_No = Label(match_detail_frame1, text="Sr.No.", bg='#ffb81d').grid(row=1, column=18, padx=5)
    Name = Label(match_detail_frame1, text="Name", bg='#ffb81d').grid(row=1, column=19)
    Mins = Label(match_detail_frame1, text="Mins", bg='#ffb81d').grid(row=1, column=20)
    CS = Label(match_detail_frame1, text="CS", bg='#ffb81d').grid(row=1, column=21)
    SHOT = Label(match_detail_frame1, text="SHOT", bg='#ffb81d').grid(row=1, column=22)
    GLS = Label(match_detail_frame1, text="GLS", bg='#ffb81d').grid(row=1, column=23)
    KP = Label(match_detail_frame1, text="KP", bg='#ffb81d').grid(row=1, column=24)
    TKLS = Label(match_detail_frame1, text="TKLS", bg='#ffb81d').grid(row=1, column=25)
    BLK = Label(match_detail_frame1, text="BLK", bg='#ffb81d').grid(row=1, column=26)
    INT = Label(match_detail_frame1, text="INT", bg='#ffb81d').grid(row=1, column=27)
    DRB = Label(match_detail_frame1, text="DRB", bg='#ffb81d').grid(row=1, column=28)
    YC = Label(match_detail_frame1, text="YC", bg='#ffb81d').grid(row=1, column=29)
    RC = Label(match_detail_frame1, text="RC", bg='#ffb81d').grid(row=1, column=30)
    PMSD = Label(match_detail_frame1, text="PMSD", bg='#ffb81d').grid(row=1, column=31)
    PSVD = Label(match_detail_frame1, text="PSVD", bg='#ffb81d').grid(row=1, column=32)
    TGL = Label(match_detail_frame1, text="TGL", bg='#ffb81d').grid(row=1, column=33)
    GLA = Label(match_detail_frame1, text="GLA", bg='#ffb81d').grid(row=1, column=34)
    TOT = Label(match_detail_frame1, text="TOT", bg='#ffb81d').grid(row=1, column=35)

    indexs = int(len(match_detail))
    # print(match_detail)
    rown = 2

    for i in range(1, indexs):
        if (match_detail[i][1][17]) == "H":
            baa = 0
            if (match_detail[i][0][4]) == "G":
                sr_no_label = Label(match_detail_frame1, text=i, fg='#921010', bg='#ffb81d').grid(row=i + 1,
                                                                                                  column=0)
                name = Label(match_detail_frame1, text=match_detail[i][1][16], fg='#921010', bg='#ffb81d').grid(
                    row=i + 1, column=1)
                for j in range(0, 16):
                    points = Label(match_detail_frame1, text=match_detail[i][1][j], fg='#921010',
                                   bg='#ffb81d').grid(row=i + 1, column=j + 2)
            elif (match_detail[i][0][4]) == "D":

                sr_no_label = Label(match_detail_frame1, text=i, fg='#0F528A', bg='#ffb81d').grid(row=i + 1,
                                                                                                  column=0)
                name = Label(match_detail_frame1, text=match_detail[i][1][16], fg='#0F528A', bg='#ffb81d').grid(
                    row=i + 1,
                    column=1)
                for j in range(0, 16):
                    points = Label(match_detail_frame1, text=match_detail[i][1][j], fg='#0F528A',
                                   bg='#ffb81d').grid(row=i + 1, column=j + 2)
            elif (match_detail[i][0][4]) == "M":

                sr_no_label = Label(match_detail_frame1, text=i, fg='#16680E', bg='#ffb81d').grid(row=i + 1,
                                                                                                  column=0)
                name = Label(match_detail_frame1, text=match_detail[i][1][16], fg='#16680E', bg='#ffb81d').grid(
                    row=i + 1,
                    column=1)
                for j in range(0, 16):
                    points = Label(match_detail_frame1, text=match_detail[i][1][j], fg='#16680E',
                                   bg='#ffb81d').grid(row=i + 1, column=j + 2)
            else:

                sr_no_label = Label(match_detail_frame1, text=i, fg='#320E68', bg='#ffb81d').grid(row=i + 1,
                                                                                                  column=0)
                name = Label(match_detail_frame1, text=match_detail[i][1][16], fg='#320E68', bg='#ffb81d').grid(
                    row=i + 1,
                    column=1)
                for j in range(0, 16):
                    points = Label(match_detail_frame1, text=match_detail[i][1][j], fg='#320E68',
                                   bg='#ffb81d').grid(row=i + 1, column=j + 2)
        else:
            baa = 0
            if (match_detail[i][0][4]) == "G":
                sr_no_label = Label(match_detail_frame1, text=i, fg='#921010', bg='#ffb81d').grid(row=rown,
                                                                                                  column=18)

                name = Label(match_detail_frame1, text=match_detail[i][1][16], fg='#921010', bg='#ffb81d').grid(
                    row=rown, column=19)

                for j in range(0, 16):
                    points = Label(match_detail_frame1, text=match_detail[i][1][j], fg='#921010',
                                   bg='#ffb81d').grid(
                        row=rown, column=20 + j)

                rown += 1
            elif (match_detail[i][0][4]) == "D":
                sr_no_label = Label(match_detail_frame1, text=i, fg='#0F528A', bg='#ffb81d').grid(row=rown,
                                                                                                  column=18)

                name = Label(match_detail_frame1, text=match_detail[i][1][16], fg='#0F528A', bg='#ffb81d').grid(
                    row=rown, column=19)

                for j in range(0, 16):
                    points = Label(match_detail_frame1, text=match_detail[i][1][j], fg='#0F528A',
                                   bg='#ffb81d').grid(
                        row=rown, column=20 + j)

                rown += 1
            elif (match_detail[i][0][4]) == "M":
                sr_no_label = Label(match_detail_frame1, text=i, fg='#16680E', bg='#ffb81d').grid(row=rown,
                                                                                                  column=18)

                name = Label(match_detail_frame1, text=match_detail[i][1][16], fg='#16680E', bg='#ffb81d').grid(
                    row=rown, column=19)

                for j in range(0, 16):
                    points = Label(match_detail_frame1, text=match_detail[i][1][j], fg='#16680E',
                                   bg='#ffb81d').grid(
                        row=rown, column=20 + j)

                rown += 1
            else:
                sr_no_label = Label(match_detail_frame1, text=i, fg='#320E68', bg='#ffb81d').grid(row=rown,
                                                                                                  column=18)

                name = Label(match_detail_frame1, text=match_detail[i][1][16], fg='#320E68', bg='#ffb81d').grid(
                    row=rown, column=19)

                for j in range(0, 16):
                    points = Label(match_detail_frame1, text=match_detail[i][1][j], fg='#320E68',
                                   bg='#ffb81d').grid(
                        row=rown, column=20 + j)

                rown += 1


# harshad write in this


def matchdetailswindow(match_option, root):
    # print(match_option)
    matchdetails = Toplevel()
    matchdetails.title("Match DETAILS")
    matchdetails.geometry(
        "900x1000+{0}+{1}".format(int((root.winfo_screenwidth() / 2) - 450),
                                  int((root.winfo_screenheight() / 2) - 500)))
    matchdetails.configure(bg="#ffb81d")
    match_buttons_frame = LabelFrame(matchdetails, bg="#ffb81d", text="Matches")
    match_buttons_frame.grid(row=0, column=0)
    no_data_button = Label(matchdetails, text="NO DATA TO DISPLAY", font=(172),
                           bg="#ffb81d", padx=60, pady=10)

    no_data_button.grid(row=0, column=1)

    def matchdatashow(match_detail, match_index):
        match_detail = match_detail[match_index]
        match_id = match_detail[0]
        response = EFFBL.playerdataapi(match_id)
        if response == 0:
            messagebox.showerror("API Failure", "API calls Exceeded \n Try again Tomorrow")
            return 0
        playerstatsarray = EFFBL.playerstats(response)
        playerspointarray = EFFBL.playerpoints(playerstatsarray)
        no_data_button.grid_forget()
        match_details_frame1 = LabelFrame(matchdetails, bg="#ffb81d", text=str(match_index + 1))
        match_details_frame1.grid(row=0, column=match_index + 1, rowspan=100, sticky='n')
        clear_button = Button(match_details_frame1, text="CLEAR", bg="#ffb81d", font=(33), padx=50,
                              command=match_details_frame1.destroy)
        clear_button.grid(row=0, column=0, columnspan=4)
        row_count = 5
        column_count = 0
        var = str(match_detail[2]) + " - " + str(match_detail[3]) + " - " + str(match_detail[4])
        match_textd = str(match_detail[18]) + " ( " + str(match_detail[23]) + " ) vs ( " + str(
            match_detail[24]) + " ) " + str(
            match_detail[21]) + "\n" + str(var) + "\n" + str(match_detail[11])
        match_heading = Label(match_details_frame1, text=match_textd, bg="#ffb81d", font=(33))
        match_heading.grid(row=1, column=0, columnspan=4)
        player_name_label = Label(match_details_frame1, text="Player Name", bg="#ffb81d", font=(33), padx=5, pady=10)
        player_name_label1 = Label(match_details_frame1, text="Player Name", bg="#ffb81d", font=(33), padx=5, pady=10)
        player_name_label.grid(row=4, column=0)
        player_name_label1.grid(row=4, column=2)
        player_points_label1 = Label(match_details_frame1, text="Points", bg="#ffb81d", font=(33), padx=5, pady=10)
        player_points_label = Label(match_details_frame1, text="Points", bg="#ffb81d", font=(33), padx=5, pady=10)
        player_points_label.grid(row=4, column=1)
        player_points_label1.grid(row=4, column=3)
        index = 0
        home_details = []
        away_details = []
        for playerstats in playerstatsarray:
            if playerstats[28] == 'H':
                playerstats.append(playerspointarray[index][15])
                home_details.append(playerstats)
                index = index + 1
            else:
                playerstats.append(playerspointarray[index][15])
                away_details.append(playerstats)
                index = index + 1

        match_details = [match_detail]
        ind = 0
        for playerstats in playerstatsarray:
            playermatchdata = [playerstats, playerspointarray[ind]]
            match_details.append(playermatchdata)
            ind = ind + 1
        # print(match_details)
        home_button = Button(match_details_frame1, text='Enter Match Into DB \n (Home Team)', font=(25),
                             bg="#ffb81d", padx=5, pady=2,
                             command=lambda: DBInterface.insertplayerdata(home_details, match_detail))
        away_button = Button(match_details_frame1, text='Enter Match Into DB \n (Away Team)', font=(25),
                             bg="#ffb81d", padx=5, pady=2,
                             command=lambda: DBInterface.insertplayerdata(away_details, match_detail))
        home_button.grid(row=2, column=0, columnspan=2)
        away_button.grid(row=2, column=2, columnspan=2)
        detailed_matchdata = Button(match_details_frame1, text='Get Detailed Match Data', font=(25),
                                    bg="#ffb81d", padx=5, pady=2,
                                    command=lambda: detailedwindow(match_details, root))
        detailed_matchdata.grid(row=3, column=0, columnspan=4)
        hrow = 5
        arow = 5
        for playerpoints in playerspointarray:
            if playerpoints[17] == 'H':
                player_name = Label(match_details_frame1, text=playerpoints[16], font=(25), bg="#ffb81d", padx=5,
                                    pady=2)
                player_name.grid(row=hrow, column=0)
                player_points = Label(match_details_frame1, text=playerpoints[15], font=(33), bg="#ffb81d", padx=5,
                                      pady=2)
                player_points.grid(row=hrow, column=1)
                hrow += 1
            if playerpoints[17] == 'A':
                player_name = Label(match_details_frame1, text=playerpoints[16], font=(25), bg="#ffb81d", padx=5,
                                    pady=2)
                player_name.grid(row=arow, column=+2)
                player_points = Label(match_details_frame1, text=playerpoints[15], font=(33), bg="#ffb81d", padx=5,
                                      pady=2)
                player_points.grid(row=arow, column=+ 3)
                arow += 1

    match_index = IntVar()
    index = 0
    for matches in match_option:
        var = str(matches[2]) + " - " + str(matches[3]) + " - " + str(matches[4])
        match_text = str(matches[18]) + " ( " + str(matches[23]) + " ) vs ( " + str(matches[24]) + " ) " + str(
            matches[21]) + "\n" + str(var) + "\n" + str(matches[11])

        Radiobutton(match_buttons_frame, text=match_text, bg="#ffb81d", font=(33), padx=10,
                    variable=match_index,
                    value=index, command=lambda: matchdatashow(match_option, match_index.get())).pack(anchor='w')
        index += 1


def daterangewindow(team_id, gobuttonimage, root):
    id1 = team_id

    date_page = Toplevel()
    date_page.title("Enter DATE")
    date_page.geometry(
        "250x150+{0}+{1}".format(int((root.winfo_screenwidth() / 2) - 125), int((root.winfo_screenheight() / 2) - 75)))
    date_page.configure(bg="#ffb81d")

    current_date = datetime.datetime.now()
    cyear = current_date.year
    cmonth = current_date.month
    cday = current_date.day

    cal = Calendar(date_page, selectmode="day", year=cyear, month=cmonth, day=cday, date_pattern='y/mm/dd')

    label_of_to_date = Label(date_page, text="From Date :", bg="#ffb81d")
    label_of_to_date.grid(row=0, column=0, padx=20, pady=10)
    entry_from_date = DateEntry(date_page, date_pattern="yyyy-mm-dd")
    entry_from_date.grid(row=0, column=1, padx=20, pady=10)

    label_of_to_date = Label(date_page, text="To Date :", bg="#ffb81d")
    label_of_to_date.grid(row=1, column=0, padx=20, pady=10)
    entry_to_date = DateEntry(date_page, date_pattern="yyyy-mm-dd")
    entry_to_date.grid(row=1, column=1, padx=20, pady=10)

    def getdate():
        match_data_array = [id1]
        fromdate = (entry_from_date.get_date())
        from_date = fromdate.strftime("%Y-%m-%d")
        match_data_array.append(from_date)
        todate = (entry_to_date.get_date())
        to_date = todate.strftime("%Y-%m-%d")
        match_data_array.append(to_date)
        if todate == fromdate or fromdate > todate:

            messagebox.showerror("Date Range ERROR", "Please Select Different Dates")  # to get error msg
            date_page.destroy()
            daterangewindow(match_data_array[0], gobuttonimage, root)

        else:
            date_page.destroy()

            match_options = EFFBL.fixturedataapi(match_data_array[0], match_data_array[1], match_data_array[2])
            if match_options == 0 or DBInterface.api_call_limit_exceeded():
                if match_options == 0:
                    messagebox.showerror("No Matches", "No Matches for the given dates \n Please try with other dates")
                else:
                    messagebox.showerror("API Failure", "API calls Exceeded \n Try again Tomorrow")
            else:
                matchdetailswindow(match_options, root)

    click = Button(date_page, image=gobuttonimage, command=getdate, padx=10, pady=10, borderwidth=0)
    click.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
