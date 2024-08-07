from tkinter import *
from datetime import *
import requests


# get api from api.open-meteo.com
URL = 'https://api.open-meteo.com/v1/forecast?latitude=35.8327&longitude=50.9915&hourly=temperature_2m&forecast_days=1'
location = 'delhi technologicaluniversity'
PARAM = {'address':location}
info = requests.get(url=URL, params=PARAM)
data = info.json()
temps = data["hourly"]["temperature_2m"]

#Get Time
nowTimes = datetime.now()
now_hour = nowTimes.hour


root = Tk()
root.title('Live Weather')
root.geometry('360x320')
root.resizable(False, False)
root.config(bg='#66FFB2')

#Frame
frame1 = Frame(root, height=40,width=300, bg='#66FFB2')
frame1.pack(side=TOP)
frame2 = Frame(root, height=40,width=300, bg='#66FFB2')
frame2.pack(side=TOP)
frame3 = Frame(root, height=40,width=300, bg='#66FFB2')
frame3.pack(side=TOP)
frame4 = Frame(root, height=40,width=300, bg='#66FFB2')
frame4.pack(side=TOP)
frame5 = Frame(root, height=40,width=300, bg='#66FFB2')
frame5.pack(side=TOP)
frame6 = Frame(root, height=40,width=300, bg='#66FFB2')
frame6.pack(side=TOP)
frame7 = Frame(root, height=40,width=300, bg='#66FFB2')
frame7.pack(side=TOP)
frame8 = Frame(root, height=40,width=300, bg='#66FFB2')
frame8.pack(side=TOP)

#Label
label1 = Label(frame6, text='Temp Is ?? C', bg='#66FFB2', fg='#202020')
label1.pack(padx=5, pady=5)

label2 = Label(frame5, text='For Get Temp Of Any Hour, Click On Hour', bg='#66FFB2', fg='#202020')
label2.pack(padx=5, pady=5)

label3 = Label(frame7, text='Click To See Live Weather',bg='#66FFB2', fg='#202020')
label3.pack(padx=5, pady=5)

#Variable 
tempp = None
#Definition
def getLiveTime():
    tempp = temps[now_hour]
    label3.config(text=f'Live Weather Of {now_hour}, Is {tempp} C')

def h00():
    tempp = temps[0]
    label1.config(text=f'Temp Is {tempp} C')

def h01():
    tempp = temps[1]
    label1.config(text=f'Temp Is {tempp} C')

def h02():
    tempp = temps[2]
    label1.config(text=f'Temp Is {tempp} C')

def h03():
    tempp = temps[3]
    label1.config(text=f'Temp Is {tempp} C')

def h04():
    tempp = temps[4]
    label1.config(text=f'Temp Is {tempp} C')

def h05():
    tempp = temps[5]
    label1.config(text=f'Temp Is {tempp} C')

def h06():
    tempp = temps[6]
    label1.config(text=f'Temp Is {tempp} C')

def h07():
    tempp = temps[7]
    label1.config(text=f'Temp Is {tempp} C')

def h08():
    tempp = temps[8]
    label1.config(text=f'Temp Is {tempp} C')

def h09():
    tempp = temps[9]
    label1.config(text=f'Temp Is {tempp} C')

def h10():
    tempp = temps[10]
    label1.config(text=f'Temp Is {tempp} C')

def h11():
    tempp = temps[11]
    label1.config(text=f'Temp Is {tempp} C')

def h12():
    tempp = temps[12]
    label1.config(text=f'Temp Is {tempp} C')

def h13():
    tempp = temps[13]
    label1.config(text=f'Temp Is {tempp} C')

def h14():
    tempp = temps[14]
    label1.config(text=f'Temp Is {tempp} C')

def h15():
    tempp = temps[15]
    label1.config(text=f'Temp Is {tempp} C')

def h16():
    tempp = temps[16]
    label1.config(text=f'Temp Is {tempp} C')

def h17():
    tempp = temps[17]
    label1.config(text=f'Temp Is {tempp} C')

def h18():
    tempp = temps[18]
    label1.config(text=f'Temp Is {tempp} C')

def h19():
    tempp = temps[19]
    label1.config(text=f'Temp Is {tempp} C')

def h20():
    tempp = temps[20]
    label1.config(text=f'Temp Is {tempp} C')

def h21():
    tempp = temps[21]
    label1.config(text=f'Temp Is {tempp} C')

def h22():
    tempp = temps[22]
    label1.config(text=f'Temp Is {tempp} C')

def h23():
    tempp = temps[23]
    label1.config(text=f'Temp Is {tempp} C')



#Button
btn0 = Button(frame8, text='Live Weather', command=getLiveTime)
btn0.pack(padx=10)

btn1 = Button(frame1, text='00', command=h00)
btn1.pack(padx=10, side=LEFT, pady=10)
btn2 = Button(frame1, text='01', command=h01)
btn2.pack(padx=10, side=LEFT)
btn3 = Button(frame1, text='02', command=h02)
btn3.pack(padx=10, side=LEFT)
btn4 = Button(frame1, text='03', command=h03)
btn4.pack(padx=10, side=LEFT)
btn5 = Button(frame1, text='04', command=h04)
btn5.pack(padx=10, side=LEFT)
btn6 = Button(frame1, text='05', command=h05)
btn6.pack(padx=10, side=LEFT)

# ******************************************

btn7 = Button(frame2, text='06', command=h06)
btn7.pack(padx=10, side=LEFT, pady=10)
btn8 = Button(frame2, text='07', command=h07)
btn8.pack(padx=10, side=LEFT)
btn9 = Button(frame2, text='08', command=h08)
btn9.pack(padx=10, side=LEFT)
btn10 = Button(frame2, text='09', command=h09)
btn10.pack(padx=10, side=LEFT)
btn11 = Button(frame2, text='10', command=h10)
btn11.pack(padx=10, side=LEFT)
btn12 = Button(frame2, text='11', command=h11)
btn12.pack(padx=10, side=LEFT)

# *******************************************

btn13 = Button(frame3, text='12', command=h12)
btn13.pack(padx=10, side=LEFT, pady=10)
btn14 = Button(frame3, text='13', command=h13)
btn14.pack(padx=10, side=LEFT)
btn15 = Button(frame3, text='14', command=h14)
btn15.pack(padx=10, side=LEFT)
btn16 = Button(frame3, text='15', command=h15)
btn16.pack(padx=10, side=LEFT)
btn17 = Button(frame3, text='16', command=h16)
btn17.pack(padx=10, side=LEFT)
btn18 = Button(frame3, text='17', command=h17)
btn18.pack(padx=10, side=LEFT)

# ******************************************

btn19 = Button(frame4, text='18', command=h18)
btn19.pack(padx=10, side=LEFT, pady=10)
btn20 = Button(frame4, text='19', command=h19)
btn20.pack(padx=10, side=LEFT)
btn21 = Button(frame4, text='20', command=h20)
btn21.pack(padx=10, side=LEFT)
btn22 = Button(frame4, text='21', command=h21)
btn22.pack(padx=10, side=LEFT)
btn23 = Button(frame4, text='22', command=h22)
btn23.pack(padx=10, side=LEFT)
btn24 = Button(frame4, text='23', command=h23)
btn24.pack(padx=10, side=LEFT)


root.mainloop()