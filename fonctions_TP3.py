import random

def mots():
    fichier=open('motspendu.txt','r')
    mots=fichier.readlines()
    numero_mot=random.randint(0,len(mots)-1)
    mot_pendu=mots[numero_mot]
    mot_chercher=[mot_pendu[0]]
    motpe=[mot_pendu[0]]
    for n in range(len(mot_pendu)-2):
        mot_chercher.append('_')
        motpe.append(mot_pendu[n])
    return mot_chercher, motpe



def affichage(mot_chercher,lettre,motpe):
    for i in range(len(mot_chercher)):
        if motpe[i]==lettre:
            mot_chercher[i]=lettre
    return mot_chercher



def verification_lettre(motpe,lettre):
    Let=[]
    for j in range(len(motpe)):
        if lettre==motpe[j]:
            Let.append(j)
            return True, Let
        else:
            return False




def jeu():
    nbre_erreurs=0
    motpe,mot_chercher=mots()
    while mot_chercher!=motpe and nbre_erreurs<=8:
        M=''
        for j in range(len(motpe)):
            M=M+mot_chercher[j]
            print(M)
            print('choisissez une lettre:')
            lettre=input()
            verif=verification_lettre(motpe,lettre)
            if verif==False:
                nbre_erreurs = nbre_erreurs+1
            else:
                M=''
                for i in range(len(motpe)):
                    if motpe[i]==lettre:
                        mot_chercher[i]=lettre
                    M=M+mot_chercher[i]
                print(M)
    M=''
    for i in range(len(motpe)):
        M=M+motpe[i]
                


jeu()


