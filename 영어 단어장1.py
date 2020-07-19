
import tkinter
import tkinter.messagebox
import random

def callback():
    data = lines[v.get()].split(',')
    if s[v.get()].get() == data[1][:-1] :
        tkinter.messagebox.showinfo("성공" ,"맞았습니다!")
        
    else:
        tkinter.messagebox.showwarning("실패" ,"틀렸습니다!")

root = tkinter.Tk()
root.title("word")

file = open("word.csv", "r")
lines = file.readlines()

v = tkinter.IntVar()
s = [tkinter.StringVar() for i in range(len(lines))]

random.shuffle(lines)
index = 0

a = int(input("열의 개수:"))

for i in range(0,3*(len(lines)//a)+1,3):
    for x in range(a):
        if index+x<len(lines):
            data = lines[index+x].split(',')
            '''
            a = input(data[0]+"?")
            if data[1][:-1] == a:
                print("맞췄습니다.")
            else:
                print("틀렸습니다.")
            '''
            lbl = tkinter.Label(root, text=data[0])
            lbl.grid(row=x, column=i,padx = 5, pady = 5)
            txt = tkinter.Entry(root,textvariable = s[x])
            txt.grid(row=x, column=i+1,padx = 5, pady = 5)
            btn = tkinter.Radiobutton(root, text="OK", width=15,variable = v, command = callback, value = x, indicatoron = 0)
            btn.grid(row=x, column=i+2, padx = 5, pady = 5)
        else:
            break
    index+=a
    
file.close() 
root.mainloop()
