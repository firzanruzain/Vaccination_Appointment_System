# *******************************************************************************************************************
# Program : Group28.py
# Course : PSP0101 PROBLEM SOLVING AND PRGRAM DESIGN
# Class : TT2V
# Trimester : 2021/22 Trimester 1
# Member_1 : 1201100697 | Tunku Ahmad Fahmi Bin Tunku Ahmad Mustaffa | 1201100697@student.mmu.edu.my | 0167025232
# Member_2 : 1211103220 | Muhammad Firzan Ruzain Bin Firdus          | 1211103220@student.mmu.edu.my | 01127282086
# Member_3 : 1181102751 | Abdullah Bin Ahmad                         | 1181102751@student.mmu.edu.my | 01123883873
# Member_4 : 1211103237 | Nurul Ain Binti Kamarudin                  | 1211103237@student.mmu.edu.my | 0172003878
# *******************************************************************************************************************
# Task Distribution 
# Member_1 : Account Sign Up and Login Authentication
# Member_2 : Menu and Result Display
# Member_3 : Public User Update Information and View Appointment
# Member_4 : Administrator Assign Appointment, Create Vaccination Center and Generate List
# *******************************************************************************************************************

#------------------------------------------Import-----------------------------------------------------------------------

from tkinter import *
import os
from datetime import *
from tkinter import font
from tkinter.font import BOLD

#-----------------------------------------Funtions---------------------------------------------------------------

def db(): #function for update data from txt file
    global UserDetails
    global AdminDetails
    global MedicalInfo
    global Appointment
    global VaccCenter
    global Address

    UserDetails = []
    AdminDetails = []
    MedicalInfo = []
    Appointment = []
    VaccCenter = []
    Address = []

    file = open("UserDetails.txt", "r")
    for i in file:
        i = i.strip()
        lst = i.split(",")
        UserDetails.append(lst)
    file.close()

    file = open("AdminDetails.txt", "r")
    for i in file:
        i = i.strip()
        lst = i.split(",")
        AdminDetails.append(lst)
    file.close()

    file = open("MedicalInfo.txt", "r")
    for i in file:
        i = i.strip()
        lst = i.split(",")
        MedicalInfo.append(lst)
    file.close()

    file = open("Appointment.txt", "r")
    for i in file:
        i = i.strip()
        lst = i.split(",")
        Appointment.append(lst)
    file.close()

    file = open("VaccinationCenter.txt", "r")
    for i in file:
        i = i.strip()
        lst = i.split(",")
        VaccCenter.append(lst)
    file.close()

    file = open("Address.txt", "r")
    for i in file:
        i = i.strip()
        lst = i.split("#")
        Address.append(lst)
    file.close()

def delete(screen): #funtion for destroy window
    screen.destroy()

def center(toplevel, width, height): #funtion for centerised window
    windowWidth = width
    windowHeight = height
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(toplevel.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(toplevel.winfo_screenheight()/2 - windowHeight/2)
    
    # Positions the window in the center of the page.
    toplevel.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")

#---------------------------------------------Main Interfaces-------------------------------------------------------------
def register():
    global screen_register 
    screen_register = Toplevel(screen) #size and title for registering screen
    center(screen_register, 300, 570)
    screen_register.title("Registration VaccineMY")

    global username
    global name
    global phone
    global age
    global id
    global password
    global username_entry
    global name_entry
    global phone_entry
    global id_entry
    global password_entry
    global lbl
    global healthcare

    global postcode
    global city
    global state
    global address
    username = StringVar()
    password = StringVar()
    age = StringVar()
    name = StringVar()
    phone = StringVar()
    id = StringVar()

    postcode = StringVar()
    city = StringVar()
    state = StringVar()
    address = StringVar()
    healthcare = StringVar()

    lbl = Label(screen_register, text = "Please fill in all details", font = ("calibri", 15) )
    lbl.pack()
    Label(screen_register, text = "").pack()
    #get username
    Label(screen_register, text = "Username").pack() 
    username_entry = Entry(screen_register, textvariable = username)
    username_entry.pack()
    #get password
    Label(screen_register, text = "Password").pack()
    password_entry = Entry(screen_register, textvariable = password)
    password_entry.pack()
    #get name
    Label(screen_register, text = "Full Name").pack()
    name_entry = Entry(screen_register, textvariable = name)
    name_entry.pack()
    #get age
    Label(screen_register, text = "Age").pack()
    age_entry = Entry(screen_register, textvariable = age)
    age_entry.pack()
    #get phone
    Label(screen_register, text = "Phone Number").pack()
    phone_entry = Entry(screen_register, textvariable = phone)
    phone_entry.pack()
    #get id
    Label(screen_register, text = "ID Number").pack()
    id_entry = Entry(screen_register, textvariable = id)
    id_entry.pack()

    #get address
    Label(screen_register, text = "Address").pack()
    Entry(screen_register, textvariable = address).pack()
    #get postcode
    Label(screen_register, text = "Postcode").pack()
    Entry(screen_register, textvariable = postcode).pack()
    #get city
    Label(screen_register, text = "City").pack()
    Entry(screen_register, textvariable = city).pack()
    #get state
    Label(screen_register, text = "State").pack()
    Entry(screen_register, textvariable = state).pack()
    answers = ["N", "Y"]
    healthcare.set("N")
    Label(screen_register, text = "Are you a healthcare worker?").pack()
    OptionMenu(screen_register, healthcare, *answers).pack()

    Label(screen_register, text = "").pack()
    Button(screen_register, text = "Register", height = "1", width = "10", command = register_user).pack()

def register_user(): #function for registering username and password


    global label
    label = Label(screen_register, text = "", fg = "red", font = ("calibri", 11)) #label
    label.pack()

    username_info = username.get()
    phone_info = phone.get()
    id_info = id.get()
    name_info = name.get()
    age_info = age.get()
    password_info = password.get()

    address_info = address.get()
    postcode_info = postcode.get()
    city_info = city.get()
    state_info = state.get()
    healthcare_info = healthcare.get()

    registered = False


    file = open("UserDetails.txt", "r") #check if username is already registered
    for i in file:
        i = i.strip()
        lst = i.split(",")
        a = lst[0]
        if(a==username_info):
            registered = True
            break
    file.close()

    if registered == True:
        lbl.config(font=("calibri", 15), fg="red" )
        lbl['text'] = "Username already existed"
        # label = Label(screen_register, text = "Username " +username_info+ " already existed", fg = "red", font = ("calibri", 11)) #label to signify success in registering
        username_entry.delete(0, END)
    elif username_info == "":
        lbl.config(font=("calibri", 15), fg="red" )
        lbl['text'] = "Please insert a username"

    elif password_info == "":
        lbl.config(font=("calibri", 15), fg="red" )
        lbl['text'] = "Please insert a password"

    elif name_info == "" or phone_info == "" or id_info == "" or age_info == "" or address_info == "" or postcode_info == "" or city_info == "" or state_info == "" or healthcare_info == "":
        lbl.config(font=("calibri", 15), fg="red" )
        lbl['text'] = "Please fill in all details"

    elif age_info.isnumeric() == False:
        lbl.config(font=("calibri", 15), fg="red" )
        lbl['text'] = "Age is not valid"

    elif int(age_info) <= 0:
        lbl.config(font=("calibri", 15), fg="red" )
        lbl['text'] = "Age is not valid"

    elif len(id_info) != 12 or id_info.isdecimal() == False:
        lbl.config(font=("calibri", 15), fg="red" )
        lbl['text'] = "ID is not valid"

    else:
        ranking = 1

        if healthcare_info == "Y":
            ranking = 5
        elif int(age_info) >= 65:
            ranking = 3
        elif int(age_info) >= 18:
            ranking = 2
        file = open("UserDetails.txt", "a") #start of function of storing username and password 
        file.write("\n"+username_info+","+password_info+","+name_info+","+age_info+","+id_info+","+phone_info+",null,"+healthcare_info+","+str(ranking))
        file.close() #end of function of storing username and password 

        file = open("Address.txt", 'a')
        file.write("\n"+username_info+"#"+address_info+"#"+postcode_info+"#"+city_info+"#"+state_info)
        file.close
        db()

        global register_successful
        register_successful = Toplevel(screen)
        register_successful.title("VaksinMY")
        center(register_successful, 250, 150)
        Label(register_successful, text = "Register Successful").pack()
        Label(register_successful,text = "").pack()
        Label(register_successful,text = "Please complete your first\nmedical information questions").pack()
        Label(register_successful,text = "").pack()
        def action(x = register_successful, y = username_info):
            delete(x)
            updateMed(y)

        def action1(x = screen_register):
            delete(x)
        Button(register_successful, text = "OK", command = lambda:[action(), action1()] ).pack()

def login(x): #login screen
    global account
    account = x
    global screen_login
    screen_login = Toplevel(screen) #size and title for login screen 
    center(screen_login, 300, 200)
    screen_login.title("Login VaccineMY")

    global username_verify
    global password_verify
    global username_entry
    global password_entry
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen_login, text = "Please enter your Username & Password").pack()
    Label(screen_login, text = "").pack()
    Label(screen_login, text = "Username").pack()
    username_entry = Entry(screen_login, textvariable = username_verify)
    username_entry.pack()
    Label(screen_login, text = "Password").pack()
    password_entry = Entry(screen_login, textvariable = password_verify)
    password_entry.pack()
    Label(screen_login, text = "").pack()
    
    def action(x = account):
        verify(x)
    Button(screen_login, text = "Login", height = "1", width = "10", command =action).pack()

def verify(x): # verify login details
    global username
    username = username_verify.get()
    password = password_verify.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    success = False

    if x == "user":
        file = open("UserDetails.txt", "r")
        for i in file:
            i = i.strip()
            lst = i.split(",")
            a = lst[0]
            b = lst[1]
            if(a==username and b==password):
                success = True
                break
        file.close()
        user_menu(success)
    elif x == "admin":
        file = open("AdminDetails.txt", "r")
        for i in file:
            i = i.strip()
            lst = i.split(",")
            a = lst[0]
            b = lst[1]
            if(a==username and b==password):
                success = True
                break
        file.close()
        admin_menu(success)

def user_menu(success): # whole funtion for user menu
    for i in range(len(UserDetails)):
        if username == UserDetails[i][0]:
            userIndex = i
    
    if success == True:
        delete(screen_login)
        global main_menu
        main_menu = Toplevel(screen)
        main_menu.title("VaksinMY")
        center(main_menu, 300, 350)
        Label(main_menu, text = "User Menu", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
        Label(main_menu, text = "Welcome, "+UserDetails[userIndex][2]+" !", width = "300", height = "1", font = ("Calibri", 11)).pack()
        Label(main_menu, text = "").pack()

        def action(x = username):
            updateMed(x)
        Button(main_menu, text = "Update Medical History", height = "2", width = "30", command=action).pack()
        Label(main_menu, text = "").pack()

        def action(x = username):
            userInfo(x)
        Button(main_menu, text = "View User Info", height = "2", width = "30", command=action).pack()
        Label(main_menu, text = "").pack()
        def action(x = username):
            vacc(x)
        Button(main_menu, text = "Vaccination Appointment", height = "2", width = "30", command=action).pack()
        Label(main_menu, text = "").pack()
        def action(x = main_menu):
            delete(x)
        Button(main_menu, text = "Logout", height = "2", width = "30", command= action).pack()
    elif success == False:
        global screen_login_unsuccessful
        screen_login_unsuccessful = Toplevel(screen)
        screen_login_unsuccessful.title("VaksinMY")
        center(screen_login_unsuccessful, 250, 100)

        Label(screen_login_unsuccessful,text = "").pack()
        Label(screen_login_unsuccessful, text = "Username or Password Incorrect", font= ("Calibri", 12)).pack()
        Label(screen_login_unsuccessful,text = "").pack()
        def action(x = screen_login_unsuccessful):
            delete(x)
        Button(screen_login_unsuccessful, text = "OK", command = action).pack(fill= BOTH,)
        
def admin_menu(success): # whole funtion for admin menu
    if success == True:
        delete(screen_login)
        global main_menu
        main_menu = Toplevel(screen)
        main_menu.title("VaksinMY")
        center(main_menu, 300, 350)
        Label(main_menu, text = "Admin Menu", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
        Label(main_menu,text = "").pack()
        Button(main_menu, text = "View All User", height = "2", width = "30", command=viewUser).pack()
        Label(main_menu, text = "").pack()
        Button(main_menu, text = "Add New Vaccination Center", height = "2", width = "30", command=add_center).pack()
        Label(main_menu, text = "").pack()
        Button(main_menu, text = "Vaccination Appointment", height = "2", width = "30", command=vac_menu).pack()
        Label(main_menu, text = "").pack()
        def action(x = main_menu):
                delete(x)
        Button(main_menu, text = "Logout", height = "2", width = "30", command= action).pack()
    elif success == False:
        global screen_login_unsuccessful
        screen_login_unsuccessful = Toplevel(screen)
        screen_login_unsuccessful.title("VaksinMY")
        center(screen_login_unsuccessful, 250, 100)

        Label(screen_login_unsuccessful,text = "").pack()
        Label(screen_login_unsuccessful, text = "Username or Password Incorrect", font= ("Calibri", 12)).pack()
        Label(screen_login_unsuccessful,text = "").pack()
        def action(x = screen_login_unsuccessful):
            delete(x)
        Button(screen_login_unsuccessful, text = "OK", command = action).pack(fill= BOTH,)

def vac_menu():
    global menu
    menu = Toplevel(screen)
    menu.title("VaksinMY")
    center(menu, 300, 350)
    Button(menu, text = "View All", height = "2", width = "30", command=appointment).pack(pady=(70, 0))
    Label(menu, text = "").pack()
    Button(menu, text = "Update Status", height = "2", width = "30", command=updateStat).pack()
    Label(menu, text = "").pack()
    Button(menu, text = "Assign Appointment", height = "2", width = "30", command=appointment2).pack()
    Label(menu, text = "").pack()

def main_screen(): #function for the main screen
    global screen 
    screen = Tk() #size and title for main screen / root 
    center(screen, 300, 300)
    screen.title("VaccineMY")
    Label(text = "Vaccination Malaysia", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()

    def admin(x = "admin"): #identifier user/admin
        login(x)
    Button(text = "Admin Login", height = "2", width = "30", command = admin).pack()
    Label(text = "").pack()

    def user(x = "user"):
        login(x)
    Button(text = "Login", height = "2", width = "30", command = user).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    Label(text = "").pack()
    screen.mainloop()
#---------------------------------------------Admin Part-------------------------------------------------------------
def viewUser():
    global srt
    srt = False
    def sort(index):

        global srt
        if srt == False:
            def takeSecond(x):
                return x[index]
            userlist.sort(key=takeSecond, reverse=False)
            table()
            srt = True
        else:
            def takeSecond(x):
                return x[index]
            userlist.sort(key=takeSecond, reverse=True)
            table()
            srt = False

    def risksort():
        global srt
        for i in range(len(userlist)):
            if userlist[i][4] == "low":
                userlist[i][4] = 1
            elif userlist[i][4] == "medium":
                userlist[i][4] = 2
            elif userlist[i][4] == "high":
                userlist[i][4] = 3
        if srt == False:
            def takeSecond(x):
                    return x[4]
            userlist.sort(key=takeSecond, reverse=True)
            srt = True
        else:
            def takeSecond(x):
                    return x[4]
            userlist.sort(key=takeSecond, reverse=False)
            srt = False

        for i in range(len(userlist)):
            if userlist[i][4] == 1:
                userlist[i][4] = "low"
            elif userlist[i][4] == 2:
                userlist[i][4] = "medium"
            elif userlist[i][4] == 3:
                userlist[i][4] = "high"
        table()


    global view_screen
    view_screen = Toplevel(screen)
    center(view_screen, 1300, 500)
    view_screen.title("VaccineMY")
    view_screen.grid_columnconfigure(0, weight=1)
    Label(view_screen, text="All Users", fg="black", bg="grey", height="2", font=("Calibri", 15)).grid(row=0, sticky='we', columnspan=8)

    def action(x = 0):
        sort(x)
    Button(view_screen, text="Name",borderwidth=1, relief="ridge", command=action).grid(row=1, column=0, sticky='nsew')
    def action(x = 1):
        sort(x)
    Button(view_screen, text="Age", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=1, sticky='nsew')
    def action(x = 2):
        sort(x)
    Button(view_screen, text="ID", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=2, sticky='nsew')
    def action(x = 3):
        sort(x)
    Button(view_screen, text="Phone Number", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=3, sticky='nsew')
    Button(view_screen, text="Risk", borderwidth=1, relief="ridge", width=15, command=risksort).grid(row=1, column=4, sticky='nsew')
    def action(x = 5):
        sort(x)
    Button(view_screen, text="Vaccinated", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=5, sticky='nsew')
    def action(x = 6):
        sort(x)
    Button(view_screen, text="Postcode", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=6, sticky='nsew')
    def action(x = 7):
        sort(x)
    Button(view_screen, text="Priotity Ranking", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=7, sticky='nsew')

    userlist = []
    
    for i in range(len(UserDetails)):
        vaccinated = "no"
        username1 = UserDetails[i][0]
        name1 = UserDetails[i][2]
        age = UserDetails[i][3]
        id = UserDetails[i][4] 
        phone = UserDetails[i][5]
        risk = UserDetails[i][6]
        ranking = UserDetails[i][-1]
        for j in range(len(Appointment)):
            
            if Appointment[j][0] == username1:
                vaccinated = Appointment[j][-1]
        for l in range(len(Address)):
            if Address[l][0] == username1:
                postcode = Address[l][2]
        

        lst = [name1, age, id, phone, risk, vaccinated, postcode, ranking]
        userlist.append(lst)
        
    total_rows = len(userlist)
    total_columns = len(userlist[0])
    
    def table():
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(view_screen)
                e.insert(0, "")
                e.grid(row=i+2, column=j, sticky='nsew')

        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(view_screen)
                e.insert(0, userlist[i][j])
                e.grid(row=i+2, column=j, sticky='nsew')
    
    table()


def appointment():
    global srt
    srt = False
    def sort(index):

        global srt
        if srt == False:
            def takeSecond(x):
                return x[index]
            vacclist.sort(key=takeSecond, reverse=False)
            table()
            srt = True
        else:
            def takeSecond(x):
                return x[index]
            vacclist.sort(key=takeSecond, reverse=True)
            table()
            srt = False
    
    global appointment_screen
    appointment_screen = Toplevel(screen)
    center(appointment_screen, 800, 500)
    appointment_screen.title("VaccineMY")
    appointment_screen.grid_columnconfigure(0, weight=1)
    Label(appointment_screen, text="Vaccination Appointment", fg="black", bg="grey", height="2", font=("Calibri", 15)).grid(row=0, sticky='we', columnspan=6)

    def action(x = 0):
        sort(x)
    Button(appointment_screen, text="Name",borderwidth=1, relief="ridge", command=action).grid(row=1, column=0, sticky='nsew')
    def action(x = 1):
        sort(x)
    Button(appointment_screen, text="Center", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=1, sticky='nsew')
    def action(x = 2):
        sort(x)
    Button(appointment_screen, text="Date", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=2, sticky='nsew')
    def action(x = 3):
        sort(x)
    Button(appointment_screen, text="Time", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=3, sticky='nsew')
    def action(x = 4):
        sort(x)
    Button(appointment_screen, text="Confirmed", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=4, sticky='nsew')
    def action(x = 5):
        sort(x)
    Button(appointment_screen, text="Status", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=5, sticky='nsew')

    vacclist = []

    for i in range(len(Appointment)):
        username1 = Appointment[i][0]
        vcenter1 = Appointment[i][1]
        vconfirm = Appointment[i][2]
        vdate1 = Appointment[i][3]
        vtime1 = Appointment[i][4]
        vstatus = Appointment[i][5]
        for i in range(len(UserDetails)):
            if username1 == UserDetails[i][0]:
                name1 = UserDetails[i][2]
        

        lst = [name1, vcenter1, vdate1, vtime1, vconfirm, vstatus]
        vacclist.append(lst)

    total_rows = len(vacclist)
    total_columns = len(vacclist[0])
    
    def table():
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(appointment_screen)
                e.insert(0, "")
                e.grid(row=i+2, column=j, sticky='nsew')

        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(appointment_screen)
                e.insert(0, vacclist[i][j])
                e.grid(row=i+2, column=j, sticky='nsew')
    
    table()

def appointment2():
    def save(x):

        def next():

            vdate = f"{day.get()}/{month.get()}/{year.get()}"
            vtime = f"{hour.get()}:{minute.get()}"

            file = open("Appointment.txt","a")
            file.write("\n")
            file.write(username+",")
            file.write(vcenter.get()+",")
            file.write("N,")
            file.write(vdate+",")
            file.write(vtime+",pending")
            file.close()
            db()
            save_screen.destroy()
            appointment_screen.destroy()
            appointment2()
            


        username = x
        assigned = "No"

        for i in range(len(UserDetails)):
            if username == UserDetails[i][0]:
                name = UserDetails[i][2]
                risk = UserDetails[i][6]

        for i in range(len(Address)):
            if username == Address[i][0]:
                postcode = Address[i][2]

        for i in range(len(Appointment)):
            if username == Appointment[i][0]:
                assigned = "Yes"

        save_screen = Toplevel(screen)
        center(save_screen, 300, 485)
        save_screen.title("VaccineMY")

        info_frame = LabelFrame(save_screen)
        info_frame.pack(fill=BOTH, padx=10, pady=10)
        info_frame.grid_columnconfigure(0, weight=1)

        Label(info_frame, text="NAME", font=("Calibri", 13)).grid(row=0, column=0, sticky="nsw")
        Label(info_frame, text="RISK", font=("Calibri", 13)).grid(row=1, column=0, sticky="nsw")
        Label(info_frame, text="POSTCODE", font=("Calibri", 13)).grid(row=2, column=0, sticky="nsw")

        Label(info_frame, text=name.upper(), font=("Calibri", 13, BOLD)).grid(row=0, column=1, sticky="nsw")
        Label(info_frame, text=risk.upper(), font=("Calibri", 13, BOLD)).grid(row=1, column=1, sticky="nsw")
        Label(info_frame, text=postcode, font=("Calibri", 13, BOLD)).grid(row=2, column=1, sticky="nsw")

        if assigned == "Yes":
            frame = LabelFrame(save_screen)
            frame.pack(fill=BOTH, padx=10)
            Label(frame, text="Appointment already assigned", font=("Calibri", 13, BOLD)).pack()
        else:
            #-------------------date-------------------
            date_frame = LabelFrame(save_screen)
            date_frame.pack(fill=BOTH, pady=10, padx=10)
            date_frame.grid_columnconfigure(0, weight=2)
            date_frame.grid_columnconfigure(1, weight=2)
            date_frame.grid_columnconfigure(2, weight=4)

            Label(date_frame, text="Day").grid(row=0, column=0, sticky='nsew', pady=(10, 0))
            Label(date_frame, text="Month").grid(row=0, column=1, sticky='nsew', pady=(10, 0))
            Label(date_frame, text="Year").grid(row=0, column=2, sticky='nsew', pady=(10, 0))

            currentDay = f"{datetime.now().day:02d}"
            day = StringVar()
            day.set(currentDay)
            days = [f"{x:02d}" for x in range(1,32)]

            currentMonth = f"{datetime.now().month:02d}"
            month = StringVar()
            month.set(currentMonth)
            months = [f"{x:02d}" for x in range(1,13)]
            
            currentYear = f"{datetime.now().year:04d}"
            year = StringVar()
            year.set(currentYear)
            years = [f"{x}" for x in range(int(currentYear)-1, int(currentYear)+2)]

            OptionMenu(date_frame, day, *days).grid(row=1, column=0, sticky='nsew', pady=10, padx=10)
            OptionMenu(date_frame, month, *months).grid(row=1, column=1, sticky='nsew', pady=10, padx=10)
            OptionMenu(date_frame, year, *years).grid(row=1, column=2, sticky='nsew', pady=10, padx=10)

            #-------------------Time-------------------
            time_frame = LabelFrame(save_screen)
            time_frame.pack(fill=BOTH, pady=10, padx=10)
            time_frame.grid_columnconfigure(0, weight=2)
            time_frame.grid_columnconfigure(1, weight=2)

            Label(time_frame, text="Time").grid(row=0, columnspan=2, sticky='nsew', pady=(10, 0))

            currentHour = f"{datetime.now().hour:02d}"
            hour = StringVar()
            hour.set(currentHour)
            hours = [f"{x:02d}" for x in range(0,25)]

            currentMinute = f"{datetime.now().minute:02d}"
            minute = StringVar()
            minute.set(currentMinute)
            minutes = [f"{x:02d}" for x in range(0,60)]

            OptionMenu(time_frame, hour, *hours).grid(row=1, column=0, sticky='nse', pady=10)
            OptionMenu(time_frame, minute, *minutes).grid(row=1, column=1, sticky='nsw', pady=10)

            #-------------------Vacc Center-------------------
            center_frame = LabelFrame(save_screen)
            center_frame.pack(fill=BOTH, padx=10)

            Label(center_frame, text="Vaccination Center").pack(pady=(10, 0))

            vcenters = [VaccCenter[x][0] for x in range(len(VaccCenter))]
            vcenter = StringVar()
            vcenter.set(vcenters[0])

            OptionMenu(center_frame, vcenter, *vcenters).pack(pady=10)

            #-------------------Vacc Center-------------------
            Button(save_screen, text="SET\nAPPOINTMENT", font=("Calibri", 13), command=next).pack(ipadx=15, pady=10)
        

    global srt
    srt = False
    def sort(index):

        global srt
        if srt == False:
            def takeSecond(x):
                return x[index]
            userlist.sort(key=takeSecond, reverse=False)
            table()
            srt = True
        else:
            def takeSecond(x):
                return x[index]
            userlist.sort(key=takeSecond, reverse=True)
            table()
            srt = False
    
    global appointment_screen
    appointment_screen = Toplevel(screen)
    center(appointment_screen, 800, 500)
    appointment_screen.title("VaccineMY")
    appointment_screen.grid_columnconfigure(0, weight=1)
    Label(appointment_screen, text="Assign Appointment", fg="black", bg="grey", height="2", font=("Calibri", 15)).grid(row=0, sticky='we', columnspan=6)

    def action(x = 0):
        sort(x)
    Button(appointment_screen, text="Name",borderwidth=1, relief="ridge", command=action).grid(row=1, column=0, sticky='nsew')
    def action(x = 1):
        sort(x)
    Button(appointment_screen, text="Assigned", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=1, sticky='nsew')
    def action(x = 2):
        sort(x)
    Button(appointment_screen, text="Postcode", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=2, sticky='nsew')
    def action(x = 3):
        sort(x)
    Button(appointment_screen, text="Priority", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=3, sticky='nsew')

    userlist = []

    for i in range(len(UserDetails)):
        username = UserDetails[i][0]
        name = UserDetails[i][2]
        priority = UserDetails[i][-1]
        assigned = "No"

        for j in range(len(Address)):
            if username == Address[j][0]:
                postcode = Address[j][2]

        for h in range(len(Appointment)):
            if username == Appointment[h][0]:
                assigned = "Yes"

        lst = [name, assigned, postcode, priority]
        userlist.append(lst)

    total_rows = len(userlist)
    total_columns = len(userlist[0])
    usernamesButton = {}
    
    def table():
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(appointment_screen)
                e.insert(0, "")
                e.grid(row=i+2, column=j, sticky='nsew')

        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(appointment_screen)
                e.insert(0, userlist[i][j])
                e.grid(row=i+2, column=j, sticky='nsew')
                if userlist[i][j] == "No":
                    e.configure(bg="red")
                elif userlist[i][j] == "Yes":
                    e.configure(bg="green")

        for i in range(len(userlist)):
                        nameq = userlist[i][0]
                        for j in range(len(UserDetails)):
                            if nameq == UserDetails[j][2]:
                                usernameq = UserDetails[j][0]
                        
                        def action(x = usernameq):
                            save(x)
                        
                        usernamesButton[usernameq] = Button(appointment_screen, text=nameq, command=action)
                        usernamesButton[usernameq].grid(row=i+2, column=0, sticky='nsew')
    table()

def updateStat():
    global vac_status
    vac_status = Toplevel(screen)
    vac_status.title("VaksinMY")
    center(vac_status, 800, 350)
    Label(vac_status, text = "Vaccination Status", width = "300", height = "2", font = ("Calibri", 13)).pack()

    frame = LabelFrame(vac_status, relief=FLAT)
    frame.pack(fill=BOTH, pady=0, padx=10)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=4)
    frame.grid_columnconfigure(2, weight=4)

    Label(frame, text="Date: ").grid(row=0, column=0, sticky='nsew')
    Label(frame, text="Center: ").grid(row=1, column=0, sticky='nsew')
    date_info = StringVar()

    date_entry = Entry(frame, textvariable=date_info)
    date_entry.grid(row=0,column=1, sticky='nsew')
    def today():
        current = date.today().strftime("%d/%m/%Y")
        date_entry.delete(0, END)
        date_entry.insert(0, str(current))
    Button(frame, text="TODAY", command=today).grid(row=0,column=2, sticky='nsew')

    centers = ["ALL"]
    for i in range(len(VaccCenter)):
        centers.append(VaccCenter[i][0])
    vcenter_info = StringVar(screen)
    vcenter_info.set(centers[1])

    OptionMenu(frame, vcenter_info, *centers).grid(row=1, column=1, sticky='nsew')

    def all():
        vcenter_info.set(centers[0])
    Button(frame, text="ALL", command=all).grid(row=1,column=2, sticky='nsew')

    def search():

        def update(x):

            def save():
                for i in range(len(Appointment)):
                    if username == Appointment[i][0]:
                        Appointment[i][-1] = vstatus.get()

                file = open("Appointment.txt", 'w+')
                for i in range(len(Appointment)):
                    for j in range(len(Appointment[0])):
                        if Appointment[i][j] == Appointment[i][-1]:
                            file.write(Appointment[i][j])
                        else:
                            file.write(Appointment[i][j]+",")

                    if Appointment[i] != Appointment[-1]:
                        file.write("\n")
                file.close()    

                db()
                delete(status_screen)
                search()
                

            username = x
            for i in range(len(UserDetails)):
                if username == UserDetails[i][0]:
                    name = UserDetails[i][2]
                    id = UserDetails[i][4]
            for i in range(len(Address)):
                if username == Address[i][0]:
                    state = Address[i][-1] 

            global status_screen
            status_screen = Toplevel(screen)
            status_screen.title("VaksinMY")
            center(status_screen, 300, 250)
            Label(status_screen, text = "Update Status", width = "300", height = "2", font = ("Calibri", 13)).pack()

            nameFrame = LabelFrame(status_screen, height=20)
            nameFrame.pack(fill=BOTH, padx=5, pady=(5, 10))

            Label(nameFrame, text=name.upper(), font=("Calibri", 13)).pack()

            infoFrame = LabelFrame(status_screen, height=20)
            infoFrame.pack(fill=BOTH, padx=5)
            
            frame = LabelFrame(infoFrame, borderwidth=0)
            frame.pack(fill=BOTH)
            Label(frame, text="USERNAME", font=("Calibri", 13)).pack(anchor='w', side="left", padx="8")
            Label(frame, text=username, font=("Calibri", 13, "bold")).pack(side="right", padx="8")
            frame = LabelFrame(infoFrame, borderwidth=0)
            frame.pack(fill=BOTH)
            Label(frame, text="ID", font=("Calibri", 13)).pack(anchor='w', side="left", padx="8")
            Label(frame, text=id, font=("Calibri", 13, "bold")).pack(side="right", padx="8")
            frame = LabelFrame(infoFrame, borderwidth=0)
            frame.pack(fill=BOTH)
            Label(frame, text="STATE", font=("Calibri", 13)).pack(anchor='w', side="left", padx="8")
            Label(frame, text=state, font=("Calibri", 13, "bold")).pack(side="right", padx="8")

            finalFrame = LabelFrame(status_screen, height=20, relief="flat")
            finalFrame.pack(fill=BOTH, padx=5, pady=10)
            finalFrame.grid_columnconfigure(0, weight=1)
            finalFrame.grid_columnconfigure(1, weight=1)

            answers = ["pending", "canceled", "done"]
            vstatus = StringVar()
            vstatus.set(answers[0])

            OptionMenu(finalFrame, vstatus, *answers).grid(row=0, column=0, sticky='nsew')
            Button(finalFrame, text="UPDATE", command=save).grid(row=0, column=1, sticky='nsew')
            

        for widget in listFrame.winfo_children():
            widget.destroy()
        vcenter = vcenter_info.get()
        vdate = date_info.get()


        def option():
            global srt #sort function
            srt = False
            def sort(index):

                global srt
                if srt == False:
                    def takeSecond(x):
                        return x[index]
                    vacclist.sort(key=takeSecond, reverse=False)
                    table()
                    srt = True
                else:
                    def takeSecond(x):
                        return x[index]
                    vacclist.sort(key=takeSecond, reverse=True)
                    table()
                    srt = False

            def action(x = 0):
                sort(x)
            Button(listFrame, text="Name",borderwidth=1, relief="ridge", command=action).grid(row=1, column=0, sticky='nsew')
            def action(x = 1):
                sort(x)
            Button(listFrame, text="Center", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=1, sticky='nsew')
            def action(x = 2):
                sort(x)
            Button(listFrame, text="Time", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=2, sticky='nsew')
            def action(x = 3):
                sort(x)
            Button(listFrame, text="Confirmed", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=3, sticky='nsew')
            def action(x = 4):
                sort(x)
            Button(listFrame, text="Status", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=4, sticky='nsew')

            vacclist = []

            for i in range(len(Appointment)):
                username1 = Appointment[i][0]
                vcenter1 = Appointment[i][1]
                vconfirm = Appointment[i][2]
                vdate1 = Appointment[i][3]
                vtime1 = Appointment[i][4]
                vstatus = Appointment[i][5]
                for j in range(len(UserDetails)):
                    if username1 == UserDetails[j][0]:
                        name1 = UserDetails[j][2]
                
                if vdate1 == vdate:
                    lst = [name1, vcenter1, vtime1, vconfirm, vstatus]
                    vacclist.append(lst)


            if vacclist != []:
                total_rows = len(vacclist)
                total_columns = len(vacclist[0])

                def table():
                    usernamesButton = {}
                    for i in range(total_rows):
                        for j in range(total_columns):
                            e = Entry(listFrame)
                            e.insert(0, "")
                            e.grid(row=i+2, column=j, sticky='nsew')

                    for i in range(total_rows):
                        for j in range(1, total_columns):
                            e = Entry(listFrame)
                            e.insert(0, vacclist[i][j])
                            e.grid(row=i+2, column=j, sticky='nsew')

                    for i in range(len(vacclist)):
                        nameq = vacclist[i][0]
                        for j in range(len(UserDetails)):
                            if nameq == UserDetails[j][2]:
                                usernameq = UserDetails[j][0]
                        
                        def action(x = usernameq):
                            update(x)
                        
                        usernamesButton[usernameq] = Button(listFrame, text=nameq, command=action)
                        usernamesButton[usernameq].grid(row=i+2, column=0, sticky='nsew')

                table()

        def option1():
            global srt #sort function
            srt = False
            def sort(index):

                global srt
                if srt == False:
                    def takeSecond(x):
                        return x[index]
                    vacclist.sort(key=takeSecond, reverse=False)
                    table()
                    srt = True
                else:
                    def takeSecond(x):
                        return x[index]
                    vacclist.sort(key=takeSecond, reverse=True)
                    table()
                    srt = False

            def action(x = 0):
                sort(x)
            Button(listFrame, text="Name",borderwidth=1, relief="ridge", command=action).grid(row=1, column=0, sticky='nsew')
            def action(x = 1):
                sort(x)
            Button(listFrame, text="Time", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=1, sticky='nsew')
            def action(x = 2):
                sort(x)
            Button(listFrame, text="Confirmed", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=2, sticky='nsew')
            def action(x = 3):
                sort(x)
            Button(listFrame, text="Status", borderwidth=1, relief="ridge", width=15, command=action).grid(row=1, column=3, sticky='nsew')

            vacclist = []

            for i in range(len(Appointment)):
                username1 = Appointment[i][0]
                vcenter1 = Appointment[i][1]
                vconfirm = Appointment[i][2]
                vdate1 = Appointment[i][3]
                vtime1 = Appointment[i][4]
                vstatus = Appointment[i][5]
                for j in range(len(UserDetails)):
                    if username1 == UserDetails[j][0]:
                        name1 = UserDetails[j][2]
                
                if vdate1 == vdate and vcenter1 == vcenter:
                    lst = [name1, vtime1, vconfirm, vstatus]
                    vacclist.append(lst)
                    
            if vacclist != []:
                total_rows = len(vacclist)
                total_columns = len(vacclist[0])

                def table():
                    usernamesButton = {}
                    for i in range(total_rows):
                        for j in range(total_columns):
                            e = Entry(listFrame)
                            e.insert(0, "")
                            e.grid(row=i+2, column=j, sticky='nsew')

                    for i in range(total_rows):
                        for j in range(total_columns):
                            e = Entry(listFrame)
                            e.insert(0, vacclist[i][j])
                            e.grid(row=i+2, column=j, sticky='nsew')

                    for i in range(len(vacclist)):
                        nameq = vacclist[i][0]
                        for j in range(len(UserDetails)):
                            if nameq == UserDetails[j][2]:
                                usernameq = UserDetails[j][0]
                        
                        def action(x = usernameq):
                            update(x)
                        
                        usernamesButton[usernameq] = Button(listFrame, text=nameq, command=action)
                        usernamesButton[usernameq].grid(row=i+2, column=0, sticky='nsew')
                
                table()

        if vcenter == "ALL":
            option()
        else:
            option1()

        


    Button(vac_status, text="SEARCH", command=search).pack(pady=10, padx=10, fill=BOTH)

    listFrame = LabelFrame(vac_status)
    listFrame.pack(fill=BOTH)
    listFrame.grid_columnconfigure(0, weight=1)

def add_center():
    global add_screen
    add_screen = Toplevel(screen)
    center(add_screen, 350, 500)
    add_screen.title("VaccineMY")

    center_info = StringVar()
    capacity_info = StringVar()
    total_rows = len(VaccCenter)
    total_columns = len(VaccCenter[0])

    add_screen.grid_columnconfigure(1, weight=1)
    add_screen.grid_columnconfigure(0, weight=1)
    Label(add_screen, text="Vaccionation Center").grid(row=0, column=0, sticky='nsew')
    Label(add_screen, text="Capacity/hour").grid(row=0, column=1, sticky='nsew')

    def refresh():
        db()
        add_screen.destroy()
        add_center()
    
    def add():
        vcenter = center_info.get()
        vcapacity = capacity_info.get()
        existed = False
        for i in range(len(VaccCenter)):
                if vcenter == VaccCenter[i][0]:
                    existed = True
        
        if vcenter == "" or vcapacity == "":
            lbl.config(text="Please fill in all details", fg="red")
        elif existed == True:
            lbl.config(text="Center is already added", fg="red")
        elif vcapacity.isnumeric() == False:
            lbl.config(text="Insert valid number", fg="red")
        else:
            file = open("VaccinationCenter.txt", "a")
            file.write("\n")
            file.write(vcenter+","+vcapacity)
            file.close()
            center_entry.delete(0, END)
            refresh()

    for i in range(total_rows):
        for j in range(total_columns):
            
            e = Entry(add_screen, width=20, font=('Arial',16,'bold'))          
            e.grid(row=i+1, column=j, sticky='nsew')
            e.insert(END, VaccCenter[i][j])
            e.config(state=DISABLED, disabledforeground="black")
    
    lbl = Label(add_screen, text="Insert new center")
    lbl.grid(pady=(10, 0), columnspan=2)
    center_entry = Entry(add_screen, width=20, bg="grey", fg='white',font=('Arial',16,'bold'), textvariable=center_info)
    center_entry.grid(sticky='nsew')
    capacity_entry = Entry(add_screen, width=20, bg="grey", fg='white',font=('Arial',16,'bold'), textvariable=capacity_info)
    capacity_entry.grid(sticky='nsew', column=1, row=center_entry.grid_info()['row'])
    b = Button(add_screen, text="Add", command=add, width=50)
    b.grid(columnspan=2, pady=15)

#---------------------------------------------User Part-------------------------------------------------------------

def updateMed(username):

    updated = "Never Updated"

    for i in range(len(MedicalInfo)):
        if username == MedicalInfo[i][0]:
            updated = "Last updated: "+MedicalInfo[i][-1]
            index = i


    def save():
        if updated != "Never Updated":
            del MedicalInfo[index]
            file = open("MedicalInfo.txt", "w+")
            for i in range(len(MedicalInfo)):
                for j in range(len(MedicalInfo[0])):

                    if MedicalInfo[i][j] == MedicalInfo[i][-1]:
                        file.write(MedicalInfo[i][j])
                    elif MedicalInfo[i][j] != MedicalInfo[i][-1]:
                        file.write(MedicalInfo[i][j]+",")

                if MedicalInfo[i] != MedicalInfo[-1]:
                    file.write("\n")
                elif MedicalInfo[0]:
                    file.write("\n")
            file.close()


        file = open("MedicalInfo.txt", "a")
        file.write(username+","+q1.get()+","+q2.get()+","+q3.get()+","+q4.get()+","+q5.get()+","+current)
        file.write("\n")
        file.close()

        lst = [q1.get(), q2.get(), q3.get(), q4.get(), q5.get()]
        count = 0

        for i in lst:
            if i == "Y":
                count += 1
        if count > 3:
            risk = "high"
        elif count > 1:
            risk = "medium"
        else:
            risk = "low"

        for i in range(len(UserDetails)):
            if username == UserDetails[i][0]:
                UserDetails[i][-3] = risk
                if risk == "high":
                    if UserDetails[i][-1] != "5":
                        UserDetails[i][-1] = "4"
                else:
                    if UserDetails[i][-1] != "5":
                        if int(UserDetails[i][3]) >= 65:
                            UserDetails[i][-1] = "3"
                        elif int(UserDetails[i][3]) >= 18:
                            UserDetails[i][-1] = "2"
                        else:
                            UserDetails[i][-1] = "1"

        file = open("UserDetails.txt", 'w+')
        for i in range(len(UserDetails)):
            for j in range(len(UserDetails[0])):
                if UserDetails[i][j] == UserDetails[i][-1]:
                    file.write(UserDetails[i][j])
                else:
                    file.write(UserDetails[i][j]+",")

            if UserDetails[i] != UserDetails[-1]:
                file.write("\n")
        file.close()
        
        

        db()

        global register_successful
        register_successful = Toplevel(screen)
        register_successful.title("VaksinMY")
        center(register_successful, 250, 150)
        Label(register_successful, text = "Successful").pack()
        Label(register_successful,text = "").pack()
        def action(x = register_successful):
            delete(x)

        def action1(x = update_screen):
            delete(x)
        Button(register_successful, text = "OK", command = lambda:[action(), action1()] ).pack()

    global update_screen
    update_screen = Toplevel(screen)
    update_screen.title("VaksinMY")
    center(update_screen, 300, 455)
    Label(update_screen, text = "Medical History", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()

    answers = ["N", "Y"]

    global current
    current = date.today().strftime("%d/%m/%Y")

    global q1
    global q2
    global q3
    global q4
    global q5
    q1 = StringVar(screen)
    q1.set("N")
    q2 = StringVar(screen)
    q2.set("N")
    q3 = StringVar(screen)
    q3.set("N")
    q4 = StringVar(screen)
    q4.set("N")
    q5 = StringVar(screen)
    q5.set("N")

    Label(update_screen, text = "Please answer all the questions", font = ("calibri", 15) ).pack()

    Label(update_screen, text=updated).pack()
    Label(update_screen, text = "Current date: "+current).pack()
    Label(update_screen, text="").pack()

    #get q1
    Label(update_screen, text = "Are you feeling sick today?").pack() 
    q1_entry = OptionMenu(update_screen, q1, *answers)
    q1_entry.pack()
    #get q2
    Label(update_screen, text = "Are you unvaccinated?").pack()
    q2_entry = OptionMenu(update_screen, q2, *answers)
    q2_entry.pack()
    #get q3
    Label(update_screen, text = "Have you ever have severe allergic reaction?").pack()
    q3_entry = OptionMenu(update_screen, q3, *answers)
    q3_entry.pack()
    #get q4
    Label(update_screen, text = "Do you have symptoms of COVID-19?").pack()
    q4_entry = OptionMenu(update_screen, q4, *answers)
    q4_entry.pack()
    #get q5
    Label(update_screen, text = "Do you have a bleeding disorder?").pack()
    q5_entry = OptionMenu(update_screen, q5, *answers)
    q5_entry.pack()

    Label(update_screen, text="").pack()
    Button(update_screen, text="Done", width=20, bg="green", command=save).pack()

def userInfo(username):
    status = "pending"
    for i in range(len(UserDetails)):
        if username == UserDetails[i][0]:
            name = UserDetails[i][2]
            age = UserDetails[i][3]
            id = UserDetails[i][4]
            phone = UserDetails[i][5]
            risk = UserDetails[i][6]

    for i in range(len(Address)):
        if username == Address[i][0]:
            state = Address[i][-1]

    for i in range(len(Appointment)):
        if username == Appointment[i][0]:
            vcenter = Appointment[i][1]
            vdate = Appointment[i][3]
            status = Appointment[i][-1]
            

    update = "null"
    for i in range(len(MedicalInfo)):
        if username == MedicalInfo[i][0]:
            update = MedicalInfo[i][-1]

    global info_screen
    info_screen = Toplevel(screen)
    info_screen.title("VaksinMY")
    center(info_screen, 300, 455)
    Label(info_screen, text = "User Info", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()

    nameFrame = LabelFrame(info_screen, height=20)
    nameFrame.pack(fill=BOTH, padx=5, pady=(5, 10))

    Label(nameFrame, text=name.upper(), font=("Calibri", 13)).pack()

    if risk != "null":
        Label(nameFrame, text=risk.capitalize()+" risk", font=("Calibri", 10)).pack()
        #Label(nameFrame, text="Please complete the medical info to get risk category", font=("Calibri", 10)).pack()
    #else:
        
    

    infoFrame = LabelFrame(info_screen, height=20)
    infoFrame.pack(fill=BOTH, padx=5)
    
    frame = LabelFrame(infoFrame, borderwidth=0)
    frame.pack(fill=BOTH)
    Label(frame, text="USERNAME", font=("Calibri", 13)).pack(anchor='w', side="left", padx="8")
    Label(frame, text=username, font=("Calibri", 13, "bold")).pack(side="right", padx="8")
    frame = LabelFrame(infoFrame, borderwidth=0)
    frame.pack(fill=BOTH)
    Label(frame, text="ID", font=("Calibri", 13)).pack(anchor='w', side="left", padx="8")
    Label(frame, text=id, font=("Calibri", 13, "bold")).pack(side="right", padx="8")
    frame = LabelFrame(infoFrame, borderwidth=0)
    frame.pack(fill=BOTH)
    Label(frame, text="STATE", font=("Calibri", 13)).pack(anchor='w', side="left", padx="8")
    Label(frame, text=state, font=("Calibri", 13, "bold")).pack(side="right", padx="8")
    
    riskFrame = LabelFrame(info_screen, height=20,  relief=RIDGE, bg="#249ec7")
    riskFrame.pack(fill='x', padx=5, pady=10)

    frame = LabelFrame(riskFrame, relief=FLAT, bg="white")
    frame.pack(fill=BOTH)

    if update != "null":
        Label(frame, bg='white', text="As of "+update, font=("Calibri",11,"italic")).pack(anchor="w")

    frame = LabelFrame(riskFrame, relief=FLAT)
    frame.pack(fill=BOTH)

    if risk == "low":
        riskFrame.config(bg="#249ec7")
        Label(frame, bg='#249ec7', text="LOW RISK", fg="white", font=("Calibri", 15, "bold")).pack(fill='x')
    elif risk == "medium":
        riskFrame.config(bg="#f0bc1f")
        Label(frame, bg='#f0bc1f', text="MEDIUM RISK", fg="white", font=("Calibri", 15, "bold")).pack(fill='x')
    elif risk == "high":
        riskFrame.config(bg="#ed2139")
        Label(frame, bg='#ed2139', text="HIGH RISK", fg="white", font=("Calibri", 15, "bold")).pack(fill='x')
    else:
        riskFrame.config(bg="grey")
        Label(frame, bg='grey', text="Please complete your medical info", fg="white", font=("Calibri", 12, "bold")).pack(fill='x')

    if status == "done":
        vaccFrame = LabelFrame(info_screen, height=20,  relief=RIDGE, bg="white")
        vaccFrame.pack(fill='x', padx=5)

        frame = LabelFrame(vaccFrame, relief=FLAT, bg="white")
        frame.pack(fill=BOTH)
        Label(frame, bg='#21ed8e', text="VACCINATED", font=("Calibri",20,"bold"), fg="white").pack(fill=X)

        frame = LabelFrame(vaccFrame, relief=FLAT, bg="white")
        frame.pack(fill=BOTH)
        Label(frame, text="Date: "+vdate, font=("Calibri",15), fg="black", bg='white').pack(anchor='w')
        Label(frame, text="Center: "+vcenter, font=("Calibri",15), fg="black", bg='white').pack(anchor='w')
    elif status == "pending" or status == "canceled":
        vaccFrame = LabelFrame(info_screen, height=20,  relief=RIDGE, bg="white")
        vaccFrame.pack(fill='x', padx=5)

        frame = LabelFrame(vaccFrame, relief=FLAT, bg="white")
        frame.pack(fill=BOTH)
        Label(frame, bg='#ed9121', text="NOT VACCINATED", font=("Calibri",20,"bold"), fg="white").pack(fill=X)
    
def vacc(username):
    def refresh():
        db()
        app_screen.destroy()
        vacc(username)

    def confirm():

        def no():
            for i in range(len(Appointment)):
                if username == Appointment[i][0]:
                    Appointment[i][2] = "N"

            file = open("Appointment.txt", 'w+')
            for i in range(len(Appointment)):
                for j in range(len(Appointment[0])):
                    if Appointment[i][j] == Appointment[i][-1]:
                        file.write(Appointment[i][j])
                    else:
                        file.write(Appointment[i][j]+",")

                if Appointment[i] != Appointment[-1]:
                    file.write("\n")
            file.close()
            
            db()
            delete(app1_screen)
            refresh()

        def yes():
            for i in range(len(Appointment)):
                if username == Appointment[i][0]:
                    Appointment[i][2] = "Y"

            file = open("Appointment.txt", 'w+')
            for i in range(len(Appointment)):
                for j in range(len(Appointment[0])):
                    if Appointment[i][j] == Appointment[i][-1]:
                        file.write(Appointment[i][j])
                    else:
                        file.write(Appointment[i][j]+",")

                if Appointment[i] != Appointment[-1]:
                    file.write("\n")
            file.close()
            
            db()
            delete(app1_screen)
            refresh()

        app1_screen = Toplevel(screen)
        app1_screen.title("VaksinMY")
        center(app1_screen, 300, 150)
        app1_screen.grid_columnconfigure(0, weight=1)
        app1_screen.grid_columnconfigure(1, weight=1)
        Label(app1_screen, text = "Confirm Appointment", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).grid(row=0, sticky='we', columnspan=2)
        Label(app1_screen, text="Please make sure you are \n available on the date and time given.", font = ("Calibri", 11)).grid(row=1, sticky='we', columnspan=2, pady=10)
        Button(app1_screen, text="YES", width=12, bg="#21ed8e", relief=FLAT, fg="white", font = ("Calibri", 14, BOLD), command=yes).grid(row=2, column=0, sticky='we')
        Button(app1_screen, text="NO", width=12, bg="#ed2139", relief=FLAT, fg="white", font = ("Calibri", 14, BOLD), command=no).grid(row=2, column=1, sticky='we')

    registered = False

    for i in range(len(Appointment)):
        if username == Appointment[i][0]:
            registered = True
            vcenter = Appointment[i][1]
            rvsp = Appointment[i][2]
            vdate = Appointment[i][3]
            time = Appointment[i][4]
            done = Appointment[i][-1]

    for i in range(len(UserDetails)):
        if username == UserDetails[i][0]:
            name = UserDetails[i][2]
            id = UserDetails[i][4]

    global app_screen
    app_screen = Toplevel(screen)
    app_screen.title("VaksinMY")
    center(app_screen, 300, 455)
    Label(app_screen, text = "Vaccination Appointment", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()

    main_frame = LabelFrame(app_screen, height=20, bg="white")
    main_frame.pack(fill=BOTH, padx=10, pady=10)

    Label(main_frame, text="Name", bg="white", fg="grey", font=("Calibri", 11)).pack(anchor='w')
    Label(main_frame, text=name.upper(), bg="white", fg="black", font=("Calibri", 13, BOLD)).pack(anchor='w')
    Label(main_frame, text="IC", bg="white", fg="grey", font=("Calibri", 11)).pack(anchor='w')
    Label(main_frame, text=id, bg="white", fg="black", font=("Calibri", 13, BOLD)).pack(anchor='w')

    if registered == False:
        app_frame = LabelFrame(main_frame, bg='white', height=20)
        app_frame.pack(fill=BOTH, padx=5, pady=10)

        Label(app_frame, text="NO APPOINTMENT", bg="white", fg="black", font=("Calibri", 13, BOLD)).pack()
    else:
        app_frame = LabelFrame(main_frame, bg='white', height=20)
        app_frame.pack(fill=BOTH, padx=5, pady=10)

        Label(app_frame, text="APPOINTMENT", bg="white", fg="black", font=("Calibri", 13, BOLD)).pack()
        Label(app_frame, text="Center: "+vcenter, bg="white", fg="grey", font=("Calibri", 11)).pack(anchor='w')
        Label(app_frame, text="Date: "+vdate, bg="white", fg="grey", font=("Calibri", 11)).pack(anchor='w')
        Label(app_frame, text="Time: "+time, bg="white", fg="grey", font=("Calibri", 11)).pack(anchor='w')
        if rvsp == "Y":
            Label(app_frame, text="Status: Confirmed", bg="white", fg="grey", font=("Calibri", 11)).pack(anchor='w')
        else:
            Label(app_frame, text="Status: Unavailable", bg="white", fg="grey", font=("Calibri", 11)).pack(anchor='w')

        if done == "pending":
            Button(app_frame, text="Confirm Appointment", font=("Calibri", 11, UNDERLINE), relief=FLAT, bg="white", command=confirm).pack()
            Label(app_frame, text="NOT COMPLETED", font=("Calibri", 13, BOLD), relief=FLAT, bg="#ed2139", fg="white").pack(fill=BOTH)
        elif done == "done":
            Label(app_frame, text="COMPLETED", font=("Calibri", 13, BOLD), relief=FLAT, bg="#249ec7", fg="white").pack(fill=BOTH)
        elif done == "canceled":
            Label(app_frame, text="APPOINTMENT CANCELED", font=("Calibri", 13, BOLD), relief=FLAT, bg="#ed9121", fg="white").pack(fill=BOTH)
#---------------------------------------------Executes-------------------------------------------------------------

db()
main_screen() #executes everything