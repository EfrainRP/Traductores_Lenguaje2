from tkinter import *
import re

class aplication():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x500')
        self.root.resizable(width=True,height=True)
        self.root.title('Expresiones Regulares')
        label = Label(self.root,text='Validacion de expresiones regulares', font=("Arial Black",12))
        label.pack(side=TOP)

        self.text = Frame(self.root)
        self.text.pack(side=TOP)

        self.frameDown = Frame(self.root)
        self.frameDown.pack(side=BOTTOM)

        self.text1 = Label(self.text,text='IPv4', font=("Arial",10))
        self.text1.grid(row=0,column=0,padx=10,pady=10)
        self.text2 = Label(self.text,text='Hora 24h', font=("Arial",10))
        self.text2.grid(row=1,column=0,padx=10,pady=10)
        self.text3 = Label(self.text,text='URLs', font=("Arial",10))
        self.text3.grid(row=2,column=0,padx=10,pady=10)
        self.text4 = Label(self.text,text='Mastercard', font=("Arial",10))
        self.text4.grid(row=3,column=0,padx=10,pady=10)

        self.t1 = Entry(self.text,width=40)
        self.t1.grid(row=0,column=1,padx=10,pady=10)
        self.t2 = Entry(self.text,width=40)
        self.t2.grid(row=1,column=1,padx=10,pady=10)
        self.t3 = Entry(self.text,width=40)
        self.t3.grid(row=2,column=1,padx=10,pady=10)
        self.t4 = Entry(self.text,width=40)
        self.t4.grid(row=3,column=1,padx=10,pady=10)

        self.b1 = Button(self.text,text='Validar',command=lambda:self.validar(1))
        self.b1.grid(row=0,column=2,padx=10,pady=10)
        self.b2 = Button(self.text,text='Validar',command=lambda:self.validar(2))
        self.b2.grid(row=1,column=2,padx=10,pady=10)
        self.b3 = Button(self.text,text='Validar',command=lambda:self.validar(3))
        self.b3.grid(row=2,column=2,padx=10,pady=10)
        self.b4 = Button(self.text,text='Validar',command=lambda:self.validar(4))
        self.b4.grid(row=3,column=2,padx=10,pady=10)

        self.l1 = Label(self.text,text='...')
        self.l1.grid(row=0,column=3)
        self.l2 = Label(self.text,text='...')
        self.l2.grid(row=1,column=3)
        self.l3 = Label(self.text,text='...')
        self.l3.grid(row=2,column=3)
        self.l4 = Label(self.text,text='...')
        self.l4.grid(row=3,column=3)

        self.bsalir = Button(self.frameDown,text='Salir',command=self.root.destroy)
        self.bsalir.pack(side=LEFT)
        self.blimpiar = Button(self.frameDown,text='Limpiar',command=self.limpiar)
        self.blimpiar.pack(side=LEFT)
        
        self.root.mainloop()
        
    def validar(self,num):
        if num == 1:        #Verificador de IPv4
            textvalidar = self.t1.get()
            x = re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$",textvalidar)
            if (x):
                self.l1.config(fg="green",text='IPv4 valida')
            else:
                self.l1.config(fg="red",text='IPv4 invalida') 
        elif num == 2:      #Verificador de Sistema Horario de 24h
            textvalidar = self.t2.get()
            x = re.search("^(([01]?\d)|(2[0-3])):([0-5]\d)$",textvalidar)
            if (x):
                self.l2.config(fg="green",text='Hora valida')
            else:
                self.l2.config(fg="red",text='Hora invalida') 
        elif num == 3:      #Verificador de URLs
            textvalidar = self.t3.get()
            x = re.search("^https?:\/\/[\w\-]+(\.[\w\-]+)+[#/?]?.*$",textvalidar)
            if (x):
                self.l3.config(fg="green",text='URL valida')
            else:
                self.l3.config(fg="red",text='URL invalida') 
        elif num == 4:      #Verificador de Mastercard
            textvalidar = self.t4.get()
            x = re.search("^5[1-5]\d{14}$",textvalidar)
            if (x):
                self.l4.config(fg="green",text='MasterCard valida')
            else:
                self.l4.config(fg="red",text='MasterCard invalida') 

    def limpiar(self):
        self.t1.delete(first=0,last='end')
        self.l1.config(fg='black',text='...')
        self.t2.delete(first=0,last='end')
        self.l2.config(fg='black',text='...')
        self.t3.delete(first=0,last='end')
        self.l3.config(fg='black',text='...')
        self.t4.delete(first=0,last='end')
        self.l4.config(fg='black',text='...')

app=aplication()
