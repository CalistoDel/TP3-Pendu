import random
import tkinter as tk


def mots():
    fichier=open('motspendu.txt','r')
    mots=fichier.readlines()
    numero_mot=random.randint(0,len(mots)-1)
    mot_pendu=mots[numero_mot]
    mot_chercher=[mot_pendu[0]]
    for n in range(len(mot_pendu)-2):
        mot_chercher.append('_')
    return mot_chercher, mot_pendu



def affichage(mot_chercher,lettre,mot_pendu):
    for i in range(len(mot_chercher)):
        if mot_pendu[i]==lettre:
            mot_chercher[i]=lettre
    return mot_chercher



def verification_lettre(mot_pendu,lettre):
    Let=[]
    for j in range(len(mot_pendu)):
        if lettre==mot_pendu[j]:
            Let.append(j)
            return True, Let
        else:
            return False




def jeu():
    nbre_erreurs=0
    mot_pendu,mot_chercher=mots()
    while mot_chercher!=mot_pendu and nbre_erreurs<=8:
        M=''
        for j in range(len(mot_pendu)):
            M=M+mot_chercher[j]
            print('choisissez une lettre:')
            lettre=input()
            verif=verification_lettre(mot_pendu,lettre)
            if verif==False:
                nbre_erreurs = nbre_erreurs+1
            else:
                M=''
                for i in range(len(mot_pendu)):
                    if mot_pendu[i]==lettre:
                        mot_chercher[i]=lettre
                    M=M+mot_chercher[i]
                print(M)
    M=''
    for i in range(len(mot_pendu)):
        M=M+mot_pendu[i]       

root=tk.Tk()         
width=750
height=750


class Fenetre():
    def __init__(self,root,width,height):
        tk.Canvas(root,width=750,height=750)
        Img=tk.PhotoImage("bonhomme1.gif")
        tk.Label(root,text=affichage(mot_chercher,lettre,mot_pendu))
        tk.Entry()
    root.mainloop()