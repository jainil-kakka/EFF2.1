from tkinter import *
from PIL import ImageTk, Image
import GifOpeningWindow
import MainWindow
import stathub
import EFFBL
import sqlite3
from datetime import datetime

root = Tk()
root.title('EFF 2.1')

system_width = root.winfo_screenwidth()
system_height = root.winfo_screenheight() - 60

logo_button_size = int(system_width * 0.078125)

# _____________________________________________________________________________________________
# Widget definitions
gobuttonimage = ImageTk.PhotoImage(Image.open("Resources\\BG\\DPGB.png"))

intro_page_img = Image.open('Resources\\BG\\MK1C.png')
intro_page_img = intro_page_img.resize((system_width, system_height), Image.ANTIALIAS)
intro_page_img = ImageTk.PhotoImage(intro_page_img)
intro_page_label = Label(root, image=intro_page_img)

main_page_img = Image.open('Resources\\BG\\MPMK1.png')
main_page_img = main_page_img.resize((system_width, system_height), Image.ANTIALIAS)
main_page_img = ImageTk.PhotoImage(main_page_img)
main_page_label = Label(root, image=main_page_img)

match_data_page_img = Image.open('Resources\\BG\\MDPBI.png')
match_data_page_img = match_data_page_img.resize((system_width, system_height), Image.ANTIALIAS)
match_data_page_img = ImageTk.PhotoImage(match_data_page_img)
match_data_page_label = Label(root, image=match_data_page_img)

stats_hub_button_img = Image.open('Resources\\BG\\MDBTMK2.png')
stats_hub_button_img_width = system_width * 0.19
stats_hub_button_img_height = system_height * 0.08
stats_hub_button_img = stats_hub_button_img.resize((int(stats_hub_button_img_width), int(stats_hub_button_img_height)),
                                                   Image.ANTIALIAS)
stats_hub_button_img = ImageTk.PhotoImage(stats_hub_button_img)
stats_hub_button_label = Button(root, image=stats_hub_button_img, command=lambda: stathub.stathubmain(system_width,system_height))

team_button_frame = Frame(root)

back_button = ImageTk.PhotoImage(Image.open('Resources\\BG\\MDBB.png'))

back_button_label = Button(root, image=back_button, borderwidth=0,
                           command=lambda: MainWindow.backfuntion(back_button_label,
                                                                  match_data_page_label,
                                                                  root, main_page_label, match_data_button_label,
                                                                  stats_hub_button_label, team_button_frame))

team_button_array = []
arsenal_image = Image.open('Resources\\TMS\\161.png')
arsenal_image = arsenal_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
arsenal_image = ImageTk.PhotoImage(arsenal_image)
arsenal = Button(team_button_frame, bg='#ffb81d', image=arsenal_image, padx=10, pady=10,
                 command=lambda: MainWindow.daterangewindow(161, gobuttonimage, root))
team_button_array.append(arsenal)

atletico_madrid_image = Image.open('Resources\\TMS\\530.png')
atletico_madrid_image = atletico_madrid_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
atletico_madrid_image = ImageTk.PhotoImage(atletico_madrid_image)
atletico_madrid = Button(team_button_frame, bg='#ffb81d', image=atletico_madrid_image, padx=10, pady=10
                         , command=lambda: MainWindow.daterangewindow(530, gobuttonimage, root))
team_button_array.append(atletico_madrid)

ac_milan_image = Image.open('Resources\\TMS\\489.png')
ac_milan_image = ac_milan_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
ac_milan_image = ImageTk.PhotoImage(ac_milan_image)
ac_milan = Button(team_button_frame, bg='#ffb81d', image=ac_milan_image, padx=10, pady=10
                  , command=lambda: MainWindow.daterangewindow(489, gobuttonimage, root))
team_button_array.append(ac_milan)

atalanta_image = Image.open('Resources\\TMS\\499.png')
atalanta_image = atalanta_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
atalanta_image = ImageTk.PhotoImage(atalanta_image)
atalanta = Button(team_button_frame, bg='#ffb81d', image=atalanta_image, padx=10, pady=10,
                  command=lambda: MainWindow.daterangewindow(499, gobuttonimage, root))
team_button_array.append(atalanta)

barcelona_image = Image.open('Resources\\TMS\\529.png')
barcelona_image = barcelona_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
barcelona_image = ImageTk.PhotoImage(barcelona_image)
barcelona = Button(team_button_frame, bg='#ffb81d', image=barcelona_image, padx=10, pady=10,
                   command=lambda: MainWindow.daterangewindow(529, gobuttonimage, root))
team_button_array.append(barcelona)

bayern_munich_image = Image.open('Resources\\TMS\\157.png')
bayern_munich_image = bayern_munich_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
bayern_munich_image = ImageTk.PhotoImage(bayern_munich_image)
bayern_munich = Button(team_button_frame, bg='#ffb81d', image=bayern_munich_image, padx=10, pady=10,
                       command=lambda: MainWindow.daterangewindow(157, gobuttonimage, root))
team_button_array.append(bayern_munich)

borussia_dortmund_image = Image.open('Resources\\TMS\\165.png')
borussia_dortmund_image = borussia_dortmund_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
borussia_dortmund_image = ImageTk.PhotoImage(borussia_dortmund_image)
borussia_dortmund = Button(team_button_frame, bg='#ffb81d', image=borussia_dortmund_image, padx=10, pady=10,
                           command=lambda: MainWindow.daterangewindow(165, gobuttonimage, root))
team_button_array.append(borussia_dortmund)

chelsea_image = Image.open('Resources\\TMS\\49.png')
chelsea_image = chelsea_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
chelsea_image = ImageTk.PhotoImage(chelsea_image)
chelsea = Button(team_button_frame, bg='#ffb81d', image=chelsea_image, padx=10, pady=10,
                 command=lambda: MainWindow.daterangewindow(49, gobuttonimage, root))
team_button_array.append(chelsea)

everton_image = Image.open('Resources\\TMS\\45.png')
everton_image = everton_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
everton_image = ImageTk.PhotoImage(everton_image)
everton = Button(team_button_frame, bg='#ffb81d', image=everton_image, padx=10, pady=10,
                 command=lambda: MainWindow.daterangewindow(79, gobuttonimage, root))
team_button_array.append(everton)

inter_milan_image = Image.open('Resources\\TMS\\505.png')
inter_milan_image = inter_milan_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
inter_milan_image = ImageTk.PhotoImage(inter_milan_image)
inter_milan = Button(team_button_frame, bg='#ffb81d', image=inter_milan_image, padx=10, pady=10,
                     command=lambda: MainWindow.daterangewindow(505, gobuttonimage, root))
team_button_array.append(inter_milan)

juventus_image = Image.open('Resources\\TMS\\496.png')
juventus_image = juventus_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
juventus_image = ImageTk.PhotoImage(juventus_image)
juventus = Button(team_button_frame, bg='#ffb81d', image=juventus_image, padx=10, pady=10,
                  command=lambda: MainWindow.daterangewindow(496, gobuttonimage, root))
team_button_array.append(juventus)

liverpool_image = Image.open('Resources\\TMS\\40.png')
liverpool_image = liverpool_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
liverpool_image = ImageTk.PhotoImage(liverpool_image)
liverpool = Button(team_button_frame, bg='#ffb81d', image=liverpool_image, padx=10, pady=10,
                   command=lambda: MainWindow.daterangewindow(40, gobuttonimage, root))
team_button_array.append(liverpool)

liecester_image = Image.open('Resources\\TMS\\46.png')
liecester_image = liecester_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
liecester_image = ImageTk.PhotoImage(liecester_image)
liecester = Button(team_button_frame, bg='#ffb81d', image=liecester_image, padx=10, pady=10,
                   command=lambda: MainWindow.daterangewindow(46, gobuttonimage, root))
team_button_array.append(liecester)

o_lyonnais_image = Image.open('Resources\\TMS\\80.png')
o_lyonnais_image = o_lyonnais_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
o_lyonnais_image = ImageTk.PhotoImage(o_lyonnais_image)
o_lyonnais = Button(team_button_frame, bg='#ffb81d', image=o_lyonnais_image, padx=10, pady=10,
                    command=lambda: MainWindow.daterangewindow(80, gobuttonimage, root))
team_button_array.append(o_lyonnais)

leipzig_image = Image.open('Resources\\TMS\\173.png')
leipzig_image = leipzig_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
leipzig_image = ImageTk.PhotoImage(leipzig_image)
leipzig = Button(team_button_frame, bg='#ffb81d', image=leipzig_image, padx=10, pady=20,
                 command=lambda: MainWindow.daterangewindow(173, gobuttonimage, root))
team_button_array.append(leipzig)

lazio_image = Image.open('Resources\\TMS\\487.png')
lazio_image = lazio_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
lazio_image = ImageTk.PhotoImage(lazio_image)
lazio = Button(team_button_frame, bg='#ffb81d', image=lazio_image, padx=10, pady=10,
               command=lambda: MainWindow.daterangewindow(487, gobuttonimage, root))
team_button_array.append(lazio)

bayer_leverkusen_image = Image.open('Resources\\TMS\\168.png')
bayer_leverkusen_image = bayer_leverkusen_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
bayer_leverkusen_image = ImageTk.PhotoImage(bayer_leverkusen_image)
bayer_leverkusen = Button(team_button_frame, bg='#ffb81d', image=bayer_leverkusen_image, padx=10, pady=10,
                          command=lambda: MainWindow.daterangewindow(533, gobuttonimage, root))
team_button_array.append(bayer_leverkusen)

manchester_city_image = Image.open('Resources\\TMS\\50.png')
manchester_city_image = manchester_city_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
manchester_city_image = ImageTk.PhotoImage(manchester_city_image)
manchester_city = Button(team_button_frame, bg='#ffb81d', image=manchester_city_image, padx=10, pady=10,
                         command=lambda: MainWindow.daterangewindow(50, gobuttonimage, root))
team_button_array.append(manchester_city)

manchester_utd_image = Image.open('Resources\\TMS\\33.png')
manchester_utd_image = manchester_utd_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
manchester_utd_image = ImageTk.PhotoImage(manchester_utd_image)
manchester_utd = Button(team_button_frame, bg='#ffb81d', image=manchester_utd_image, padx=10, pady=10,
                        command=lambda: MainWindow.daterangewindow(33, gobuttonimage, root))
team_button_array.append(manchester_utd)

marsielle_image = Image.open('Resources\\TMS\\81.png')
marsielle_image = marsielle_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
marsielle_image = ImageTk.PhotoImage(marsielle_image)
marsielle = Button(team_button_frame, bg='#ffb81d', image=marsielle_image, padx=10, pady=10,
                   command=lambda: MainWindow.daterangewindow(81, gobuttonimage, root))
team_button_array.append(marsielle)

monaco_image = Image.open('Resources\\TMS\\91.png')
monaco_image = monaco_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
monaco_image = ImageTk.PhotoImage(monaco_image)
monaco = Button(team_button_frame, bg='#ffb81d', image=monaco_image, padx=10, pady=10,
                command=lambda: MainWindow.daterangewindow(91, gobuttonimage, root))
team_button_array.append(monaco)

napoli_image = Image.open('Resources\\TMS\\492.png')
napoli_image = napoli_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
napoli_image = ImageTk.PhotoImage(napoli_image)
napoli = Button(team_button_frame, bg='#ffb81d', image=napoli_image, padx=10, pady=10,
                command=lambda: MainWindow.daterangewindow(492, gobuttonimage, root))
team_button_array.append(napoli)

psg_image = Image.open('Resources\\TMS\\85.png')
psg_image = psg_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
psg_image = ImageTk.PhotoImage(psg_image)
psg = Button(team_button_frame, bg='#ffb81d', image=psg_image, padx=10, pady=10,
             command=lambda: MainWindow.daterangewindow(85, gobuttonimage, root))
team_button_array.append(psg)

real_madrid_image = Image.open('Resources\\TMS\\541.png')
real_madrid_image = real_madrid_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
real_madrid_image = ImageTk.PhotoImage(real_madrid_image)
real_madrid = Button(team_button_frame, bg='#ffb81d', image=real_madrid_image, padx=10, pady=10,
                     command=lambda: MainWindow.daterangewindow(541, gobuttonimage, root))
team_button_array.append(real_madrid)

roma_image = Image.open('Resources\\TMS\\497.png')
roma_image = roma_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
roma_image = ImageTk.PhotoImage(roma_image)
roma = Button(team_button_frame, bg='#ffb81d', image=roma_image, padx=10, pady=10,
              command=lambda: MainWindow.daterangewindow(497, gobuttonimage, root))
team_button_array.append(roma)

sevilla_image = Image.open('Resources\\TMS\\536.png')
sevilla_image = sevilla_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
sevilla_image = ImageTk.PhotoImage(sevilla_image)
sevilla = Button(team_button_frame, bg='#ffb81d', image=sevilla_image, padx=10, pady=10,
                 command=lambda: MainWindow.daterangewindow(536, gobuttonimage, root))
team_button_array.append(sevilla)

shit_image = Image.open('Resources\\TMS\\47.png')
shit_image = shit_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
shit_image = ImageTk.PhotoImage(shit_image)
shit = Button(team_button_frame, bg='#ffb81d', image=shit_image, padx=10, pady=10,
              command=lambda: MainWindow.daterangewindow(47, gobuttonimage, root))
team_button_array.append(shit)

wolverhampton_image = Image.open('Resources\\TMS\\22222.png')
wolverhampton_image = wolverhampton_image.resize((logo_button_size, logo_button_size), Image.ANTIALIAS)
wolverhampton_image = ImageTk.PhotoImage(wolverhampton_image)
wolverhampton = Button(team_button_frame, bg='#ffb81d', image=wolverhampton_image, padx=10, pady=10,
                       command=lambda: MainWindow.daterangewindow(48, gobuttonimage, root))
team_button_array.append(wolverhampton)

match_data_button_img = Image.open('Resources\\BG\\MDBTMK!.png')
match_data_button_img_width = int(system_width * 0.19)
match_data_button_img_height = int(system_height * 0.08)
match_data_button_img = match_data_button_img.resize(
    (int(match_data_button_img_width), int(match_data_button_img_height)), Image.ANTIALIAS)
match_data_button_img = ImageTk.PhotoImage(match_data_button_img)
match_data_button_label = Button(root, image=match_data_button_img,
                                 command=lambda: MainWindow.matchdatamain(root, main_page_label,
                                                                          match_data_button_label,
                                                                          stats_hub_button_label, match_data_page_label,
                                                                          back_button_label, team_button_array,
                                                                          team_button_frame))




# ______________________________________________________________________________________________
# mainflow
GifOpeningWindow.OpeningWindow(root)
root.after(2500, GifOpeningWindow.intropage, root, intro_page_label)
root.after(5800, MainWindow.mainwindow, root, main_page_label, match_data_button_label, stats_hub_button_label)

root.mainloop()
