from tkinter import Tk,Label,Entry,Button,Frame,Canvas

class GraphPlotter(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(500,500)
        self.title('My Line Graph Plotter')
        c=LineGraph(self)
        self.mainloop()

class LineGraph(Frame):
    def __init__(self,r):
        super().__init__(r)
        l1=Label(self,text='Equation of line is y=mx+c')
        l1.pack()
        l2=Label(self,text='Enter value for m: ')
        l2.pack()
        self.e1=Entry(self)
        self.e1.pack()
        l3=Label(self,text='Enter value for c: ')
        l3.pack()
        self.e2=Entry(self)
        self.e2.pack()
        b1=Button(self,text='Draw Line',command=self.drawLine)
        b1.pack()
        self.pack()
    def drawLine(self):
        y=[]
        m=int(self.e1.get())
        c=int(self.e2.get())
        for x in range (400):
            y.append(m*x+c)
        c1=Canvas(self, width=400,height=400,background='red')
        for x in range (399):
            c1.create_line(x,400-y[x],x+1,400-y[x+1],fill='black',width=4)
        c1.pack()

g=GraphPlotter()

