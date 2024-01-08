from tkinter import *

window = Tk()
window.geometry("500x300")

def submit_value():
      with open("yourform.txt", "a") as  userfile:
            userfile.write("Personal info\n")
            userfile.write("Name: " + name_value.get()+"\n")
            userfile.write("Email: "+ email_value.get()+"\n")
            userfile.write("Contact no: "+ phone_num_value.get()+"\n")
            userfile.write("Gender: "+ gender_value.get()+"\n")
      print("your form is submitted sucessfully")


Label(window, text="Yusmu registration form",
      font=("times",15,"bold")).grid(row=0,column=3)
name_user = Label(window, text="Student name")
name_user.grid(row=1,column=2)
what_study = Label(window,text="your course")
what_study.grid(row=2,column=2)
phone_num = Label(window,text="Contact no")
phone_num.grid(row=3,column=2)
gender = Label(window,text="gender")
gender.grid(row=4,column=2)
address = Label(window,text="address")
address.grid(row=5,column=2)
email = Label(window,text="Email")
email.grid(row=6,column=2)

name_value = StringVar()
what_study_value = StringVar()
phone_num_value = StringVar()
gender_value = StringVar()
address_value = StringVar()
email_value = StringVar()
check_value = IntVar()

name_box = Entry(window,textvariable=name_value)
name_box.grid(row=1,column=3)
what_study_box = Entry(window,textvariable=what_study_value)
what_study_box.grid(row=2,column=3)
phone_num_box = Entry(window,textvariable=phone_num_value)
phone_num_box.grid(row=3,column=3)
gender_box = Entry(window,textvariable=gender_value)
gender_box.grid(row=4,column=3)
address_box = Entry(window,textvariable=address_value)
address_box.grid(row=5,column=3)
email_box = Entry(window,textvariable=email_value)
email_box.grid(row=6,column=3)

check_box = Checkbutton(window,text="Remember Me",variable=check_value)
check_box.grid(row=7,column=3)
submit_bttn = Button(text="Submit",command=submit_value)
submit_bttn.grid(row=8,column=3)


window.mainloop()