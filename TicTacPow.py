from tkinter import *

#TKinter window
root = Tk()
root.title("TicTacPow!")
root.geometry("300x300")
root.resizable(0, 0)


#Frame Grid
btn1_frame = Frame(root, width = 100, height = 100, bg = "blue")
btn1_frame.pack_propagate(False)
btn1_frame.grid(row = 0, column = 0)
btn2_frame = Frame(root, width = 100, height = 100, bg = "red")
btn2_frame.pack_propagate(False)
btn2_frame.grid(row = 0, column = 1)
btn3_frame = Frame(root, width = 100, height = 100, bg = "green")
btn3_frame.pack_propagate(False)
btn3_frame.grid(row = 0, column = 2)

btn4_frame = Frame(root, width = 100, height = 100, bg = "yellow")
btn4_frame.pack_propagate(False)
btn4_frame.grid(row = 1, column = 0)
btn5_frame = Frame(root, width = 100, height = 100, bg = "purple")
btn5_frame.pack_propagate(False)
btn5_frame.grid(row = 1, column = 1)
btn6_frame = Frame(root, width = 100, height = 100, bg = "violet")
btn6_frame.pack_propagate(False)
btn6_frame.grid(row = 1, column = 2)

btn7_frame = Frame(root, width = 100, height = 100, bg = "tan")
btn7_frame.pack_propagate(False)
btn7_frame.grid(row = 2, column = 0)
btn8_frame = Frame(root, width = 100, height = 100, bg = "orange")
btn8_frame.pack_propagate(False)
btn8_frame.grid(row = 2, column = 1)
btn9_frame = Frame(root, width = 100, height = 100, bg = "white")
btn9_frame.pack_propagate(False)
btn9_frame.grid(row = 2, column = 2)

#Buttons
btn_pos_1 = Button(btn1_frame,  text="1")
btn_pos_1.pack(fill = BOTH, expand = 1)
btn_pos_2 = Button(btn2_frame,  text="2")
btn_pos_2.pack(fill = BOTH, expand = 1)
btn_pos_3 = Button(btn3_frame,  text="3")
btn_pos_3.pack(fill = BOTH, expand = 1)

btn_pos_4 = Button(btn4_frame,  text="4")
btn_pos_4.pack(fill = BOTH, expand = 1)
btn_pos_5 = Button(btn5_frame,  text="5")
btn_pos_5.pack(fill = BOTH, expand = 1)
btn_pos_6 = Button(btn6_frame,  text="6")
btn_pos_6.pack(fill = BOTH, expand = 1)

btn_pos_7 = Button(btn7_frame,  text="7")
btn_pos_7.pack(fill = BOTH, expand = 1)
btn_pos_8 = Button(btn8_frame,  text="8")
btn_pos_8.pack(fill = BOTH, expand = 1)
btn_pos_9 = Button(btn9_frame,  text="9")
btn_pos_9.pack(fill = BOTH, expand = 1)


root.mainloop()
