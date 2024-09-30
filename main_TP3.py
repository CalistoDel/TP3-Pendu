import tkinter as tk
from fonctions_TP3 import jeu
from fonctions_TP3 import affichage
from fonctions_TP3 import verification_lettre

class jeu():
    def __init__(self):
        self.dico ={"bonjour"}
        self.chances = 8
    def verificationlettre(l):

    print('Ok')



class Fenetre():
    def __init__(self,root):
        self.nom='Fenetre du pendu'
        root.title(self.nom)
        self.images=[tk.PhotoImage(file=f"bonhomme{i}.gif") for i in range(1,9)]
        self.canvas=tk.Canvas(root,width=self.images[0].width(),height=self.images[0].height())
        self.canvas.pack()
        self.canvas.create_image(0,0,anchor="nw",image=self.images[0])
        self.input = tk.Entry()
        self.input.pack()

root=tk.Tk() 
app = Fenetre(root)
root.mainloop()