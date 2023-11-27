from tkinter import *
top = Tk()
'''
widgets are added here
'''
str='i am sting'
print(str.split(" ")[2])
top.title("indian driving school")
top.geometry("500x400")  
  
b = Button(top,text = "submit",bg="pink", fg="green" ,activebackground="green",activeforeground="pink")  
  
b.pack()  
  
#creating a simple canvas  
c = Canvas(top,bg = "pink")  
  
  
c.pack()  

top.mainloop()
