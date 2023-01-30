# tk-inter

# starter code
import tkinter as tk #compulsory
from tkinter import Entry, Widget, ttk # use ttk as labels looks more good
from csv import DictWriter
import os
win = tk.Tk() #compulsory
win.title("GUI")



# widgets----->label,buttons,radio button -tk,ttk

# create label
# use loop to create labels

labels = ["what is your name  : ","what is your Enail","What is your age : ","what is your gender : ","Country : ","state : ","City : "]
for i in range(len(labels)):
    cur_label = "label" +str(i)
    cur_label=ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W,padx=5,pady=5)
# name_label=ttk.Label(win,text="Enter Your Name : ")

# Entry Box
user_info ={
    "name":tk.StringVar(),
    "email":tk.StringVar(),
    "age":tk.StringVar(),
    "gender":tk.StringVar(),
    "country":tk.StringVar(),
    "state":tk.StringVar(),
    "city":tk.StringVar()
}
Counter=0
for i in user_info:
    cur_entry = "Entry" + i
    cur_entrybox = ttk.Entry(win,width=16,textvariable=user_info[i])
    cur_entrybox.grid(row=Counter,column=1)
    cur_entrybox.focus()
    Counter +=1
# name_var = tk.StringVar()# string type variable
# name_entrybox = ttk.Entry(win,width=16,textvariable=name_var)
# name_entrybox.grid(row=0,column=1)

# to set labels 
# pack method default = centre 
# centre layout manager  needs row and collown value

# name_label.grid(row=0,column=0)

###   Email label

# Email_label = ttk.Label(win,text="Enter Your Email : ")
# Email_label.grid(row=1,column=0,sticky=tk.W)  # W = west

# #########   age label 
# age_label = ttk.Label(win,text="Enter Your Age : ")
# age_label.grid(row=2,column=0,sticky=tk.W)  # W = west

# #  Entry Box to take Input
# name_var = tk.StringVar()# string type variable
# name_entrybox = ttk.Entry(win,width=16,textvariable=name_var)
# name_entrybox.grid(row=0,column=1)
# name_entrybox.focus()# to have the cursor

# email_var = tk.StringVar()
# Email_entrybox = ttk.Entry(win,width=16,textvariable=email_var)
# Email_entrybox.grid(row=1,column=1)

# age_var = tk.IntVar()
# age_entrybox = ttk.Entry(win,width=16,textvariable=age_var)
# age_entrybox.grid(row=2,column=1)

#Combo box
# gender_var = tk.StringVar()
# gender_combobox = ttk.Combobox(win,width=14,textvariable=gender_var,state="readonly")
# gender_combobox["values"] =("Male","Female","Others")
# gender_combobox.current(0)
# gender_combobox.grid(row=3,column=1)

# gender_label = ttk.Label(win,text="Select Your Gender : ")
# gender_label.grid(row=3,column=0,sticky=tk.W) 


# Radio Button
buttons = ["Student","Teacher","Businessman","Entreprenur","Fresher"]
usertype = tk.StringVar()
for i in range(len(buttons)):  
    radio_btr= ttk.Radiobutton(win,text=buttons[i],value=buttons[i],variable=usertype)
    radio_btr.grid(row=7,column=i)
# usertype = tk.StringVar()
# radio_btr1 = ttk.Radiobutton(win,text="Student",value="student",variable=usertype)
# radio_btr2 = ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=usertype)
# radio_btr3 = ttk.Radiobutton(win,text="Businessman",value="Businessman",variable=usertype)
# radio_btr4 = ttk.Radiobutton(win,text="Entreprenur",value="Entreprenur",variable=usertype)
# radio_btr5 = ttk.Radiobutton(win,text="Fresher",value="Fresher",variable=usertype)

# radio_btr1.grid(row=7,column=0)
# radio_btr2.grid(row=7,column=1)
# radio_btr3.grid(row=7,column=2)
# radio_btr4.grid(row=7,column=3)
# radio_btr5.grid(row=7,column=4)



# check button
checkbtn_var = tk.IntVar();
check_btn=ttk.Checkbutton(win,text="My First Check Button ",variable=checkbtn_var)
check_btn.grid(row=8,columnspan=3)


# Create Button
# def action():
#     username = name_var.get()
#     userage =  age_var.get()
#     user_email = email_var.get()
#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if checkbtn_var.get()==0:
#         subscribed = "NO"
#     else:
#         subscribed = "YES"
#         with open("output.csv","a")as op:
#             op.write(f"{username}, {userage}, {user_email}, {user_gender}, {user_type}, {subscribed} \n")
#             name_entrybox.delete(0,tk.END)
#             age_entrybox.delete(0,tk.END)
#             Email_entrybox.delete(0,tk.END)
#             name_label.configure(foreground="#7d0019")
#             submit_button.configure(foreground="Blue")
def action():
    username  =user_info["name"].get()
    userage   = user_info["age"].get()
    user_email = user_info["email"].get()
    user_gender = user_info["gender"].get()
    user_state = user_info["state"].get()
    user_country = user_info["country"].get()
    user_city =  user_info["city"].get()
    user_type =usertype.get()
    if checkbtn_var.get()==0:
        subscribed = "NO"
    else:
        subscribed = "YES"
        # write in csv  :
    with open("file2.csv","a",newline="") as ap:
        dict_writer = DictWriter(ap,fieldnames=["User Name","User Age","User Email Address","User Gender","user_country","user_state","user_city","Subscribed","user_type"])
        if os.stat("file2.csv").st_size==0:
            dict_writer.writeheader()
        else:
            pass
        dict_writer.writerow({
            "User Name" : username,
            "User Age" : userage,
            "User Email Address" : user_email,
            "User Gender" : user_gender,
            "user_country":user_country,
            "user_state":user_state,
            "user_city" :user_city,
            "Subscribed"  : subscribed,
            "user_type":user_type
        })

        # age_entrybox.delete(0,tk.END)
        # Email_entrybox.delete(0,tk.END)
        # name_label.configure(foreground="#7d0019")
        # submit_button.configure(foreground="Blue")

   
   
   

# def action():
#     username    = name_var.get()
#     userage     =  age_var.get()
#     user_email  = email_var.get()
#     user_gender = gender_var.get()
#     user_type   = usertype.get()
#     if checkbtn_var.get()==0:
#         subscribed = "NO"
#     else:
#         subscribed = "YES"
#         # write in csv  :
#     with open("file.csv","a",newline="") as ap:
#         dict_writer = DictWriter(ap,fieldnames=["User Name","User Age","User Gender","User Email Address","User Type","Subscribed"])
#         if os.stat("file.csv").st_size==0:
#             dict_writer.writeheader()
#         else:
#             pass
#         dict_writer.writerow({
#             "User Name" : username,
#             "User Age" : userage,
#             "User Gender" : user_gender,
#             "User Email Address" : user_email,
#             "User Type"  : user_type,
#             "Subscribed"  : subscribed,
#         })
#         name_entrybox.delete(0,tk.END)
#         age_entrybox.delete(0,tk.END)
#         Email_entrybox.delete(0,tk.END)
#         name_label.configure(foreground="#7d0019")
#         submit_button.configure(foreground="Blue")

    # print(f"username : {username},userage:  {userage} user Email  : {user_email}")
    # print(user_gender,subscribed,user_type)
submit_button = tk.Button(win,text="submit",command=action)
submit_button.grid(row=6,column=5)


win.mainloop() # to let the application running # compulsory



