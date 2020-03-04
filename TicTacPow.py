from tkinter import *

#TKinter window
root = Tk()
root.title("TicTacPow!")
root.geometry("500x500")
root.resizable(0, 0)


#Center Frame
#btns_frame = tk.Frame(root, width = 300, height = 300, bg = "blue").place(relx=0.5, rely=0.5, anchor="center")
# frame = Frame(root, width = 300, height = 300, bg = "blue")
# frame.pack_propagate(False)
# frame.place(relx = 0.5, rely = 0.5, anchor="center")

#Buttons
#btn_pos_1 = tk.Button(btns_frame, width = 5, height = 5).place(relx=0.5, rely=0.5, anchor="center")
btn_pos_1 = Button(root, width = 100, height = 100, text = "Test")
btn_pos_1.grid(row = 0, column = 0)

root.mainloop()
