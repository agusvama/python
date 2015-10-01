#holaMundoGUI.py

from Tkinter import *

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.hola = Button(frame, text="Hola", command = self.decir_hola)
		self.hola.pack(side=LEFT)		
	
	def decir_hola(self):
		print "hola mundo desde GUI!"		
		print "button clicked D:"

root = Tk()	
app = App(root)	
root.mainloop()
