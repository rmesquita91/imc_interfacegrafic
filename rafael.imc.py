# *********************************************
#
# *** Calculadora do IMC **********************
#
# *** RAFAEL MESQUITA *************************
#
# *********************************************

from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte1 = ("Arial"), ("10")

        self.espaço1 = Frame(master)
        self.espaço1["pady"] = 10
        self.espaço1.pack()

        self.espaço2 = Frame(master)
        self.espaço2["padx"] = 20
        self.espaço2.pack()

        self.espaço3 = Frame(master)
        self.espaço3["padx"] = 20
        self.espaço3.pack()

        self.espaço4 = Frame(master)
        self.espaço4["padx"] = 20
        self.espaço4.pack()

        self.espaço5 = Frame(master)
        self.espaço5["padx"] = 20
        self.espaço5.pack()

        self.espaço6 = Frame(master)
        self.espaço6["padx"] = 20
        self.espaço6.pack()

        self.nome = Label(self.espaço1, text="IMC - INDICE DE MASSA CORPORAL")
        self.nome["font"] = ("Arial", "15", "bold")
        self.nome.pack()

        self.digitoLabel = Label(self.espaço2, text="QUAL O VALOR DO SEU PESO EM KG:", font=self.fonte1)
        self.digitoLabel.pack(side=LEFT)

        self.digito = Entry(self.espaço2)
        self.digito["width"] = 30
        self.digito["font"] = self.fonte1
        self.digito.pack(side=LEFT)

        self.digito2Label = Label(self.espaço3, text="QUAL O VALOR DA SUA ALTURA:", font=self.fonte1)
        self.digito2Label.pack(side=LEFT)

        self.digito2 = Entry(self.espaço3)
        self.digito2["width"] = 30
        self.digito2["font"] = self.fonte1
        self.digito2.pack(side=LEFT)

        #caixa de texto "IMC"
        self.imcLabel = Label(self.espaço4, text="SEU INDICE DE MASSA CORPORAL:", font=self.fonte1)
        self.imcLabel.pack(side=LEFT)

        self.imcValor = Label(self.espaço5, text="", font=self.fonte1)
        self.imcValor.pack(side=RIGHT)

        #botão
        self.calcular = Button(self.espaço6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Calibri", "10")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcula
        self.calcular.pack()


    #Calculando IMC 
    def calcula(self):
        peso = self.digito.get()
        altura = self.digito2.get()

        resp = (float(peso))/(float(altura)*float(altura))

        if peso:
            self.imcValor["text"] = resp

            

        

root = Tk()
Application(root)
root.mainloop()

        
