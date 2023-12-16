from tkinter import Tk, Canvas
class MyCanvas(Tk):
    def __init__(self):
        super().__init__()
        myCanvas=Canvas(self,width=500,height=500,background='blue')
        myCanvas.create_line(10,10,50,10,fill='black',width=4)
        myCanvas.create_arc(20,20,100,100,fill='yellow')
        myCanvas.create_rectangle(150,150,400,400,fill='red')
        myCanvas.create_text(125,125,text='Python')
        myCanvas.pack()
        self.mainloop()
m=MyCanvas()

