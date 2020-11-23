from tkinter import *
window=Tk()

#items to add
btn1=Button(window, text="Autonomas", fg='black', bg='red', activebackground='Green')
btn2=Button(window, text="Up", fg='black', bg='Green')
btn3=Button(window, text="Down", fg='black', bg='Green')
btn4=Button(window, text="Left", fg='black', bg='Green')
btn5=Button(window, text="Right", fg='black', bg='Green')
btn6=Button(window, text="On/Off", fg='white', bg='black')

lbl1=Label(window, text="Speed: ")
lbl2=Label(window, text="km/h")
lbl3=Label(window, text="Co-ordinates: ")

msg1=Message (window, bg='white')


#code to get menu
menu = Menu(window) 
window.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=window.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 
helpmenu.add_command(label='info')

#co-ordinates of items
btn1.place(x=20, y=20)
btn2.place(x=310, y=350)
btn3.place(x=300, y=400)
btn4.place(x=200, y=400)
btn5.place(x=400, y=400)
btn6.place(x=400, y=20)


lbl1.place(x=20, y=400)
lbl2.place(x=90, y=400)
lbl3.place(x=20, y=350)

msg1.place(x=70, y=400)


#window options
window.title('Rover Remote')
window.geometry("500x500")
window.mainloop()
