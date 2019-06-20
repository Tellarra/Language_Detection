# -*- coding: utf-8 -*-
#!usr/bin/env python3.6
import re
import os
from vect import *
from token import *
from ReadFiles import *
from tkinter import *
from tkinter import ttk
#from gui import *
from tkinter import filedialog
from tkinter import messagebox

#Variables globales
windowMenu = Tk()
progressBar = ttk.Progressbar(windowMenu, mode="determinate", length="300")
chemin = ""
phrase = StringVar()
global window
global i
i = 0

#Cette fonction va créer tous nos dictionnaires automatiquement en arrière plan
def startProg() :

    langues = ["Eng","Fra","Esp","Dut","Ger","Ita"]
    for myFile in langues :
        myFile = myFile + "Dico.txt"
        if os.path.isfile(myFile) :
            os.remove(myFile)
            print("file ", myFile, "removed")

    count = 0


    for j in range(len(langues)):
        effacerOcc()
        inputUser = langues[j]
        listTexts, inputUser = ReadFiles.getTexts(inputUser)
        for name in listTexts :
            progressBar.step(count)
            count += 1
            windowMenu.update()
            path = "DataSet/Train/" + inputUser + "/" + name
            contenu = lireF(path)
            #occ_uni(contenu)
            occ_bi(contenu)
            ecrireDico("Dico.txt", inputUser)

    completeDico("FraDico.txt","EngDico.txt")
    completeDico("FraDico.txt","EspDico.txt")
    completeDico("EspDico.txt","EngDico.txt")
    completeDico("EspDico.txt","FraDico.txt")
    completeDico("EngDico.txt","FraDico.txt")
    completeDico("EngDico.txt","EspDico.txt")
    completeDico("EngDico.txt","DutDico.txt")
    completeDico("EngDico.txt","GerDico.txt")
    completeDico("FraDico.txt","DutDico.txt")
    completeDico("FraDico.txt","GerDico.txt")
    completeDico("EspDico.txt","DutDico.txt")
    completeDico("EspDico.txt","GerDico.txt")
    completeDico("EngDico.txt","ItaDico.txt")
    completeDico("FraDico.txt","ItaDico.txt")
    completeDico("EspDico.txt","ItaDico.txt")
    completeDico("DutDico.txt","ItaDico.txt")
    completeDico("GerDico.txt","ItaDico.txt")
    print()
    print("Eng-Eng")
    print(simCosinus("EngDico.txt","EngDico.txt"))
    print("Eng-Fra")
    print(simCosinus("EngDico.txt","FraDico.txt"))
    print("Eng-Esp")
    print(simCosinus("EngDico.txt","EspDico.txt"))
    print("Fra-Esp")
    print(simCosinus("FraDico.txt","EspDico.txt"))
    print("Eng-Dut")
    print(simCosinus("EngDico.txt","DutDico.txt"))
    print("Eng-Ger")
    print(simCosinus("EngDico.txt","GerDico.txt"))
    print("Fra-Dut")
    print(simCosinus("FraDico.txt","DutDico.txt"))
    print("Fra-Ger")
    print(simCosinus("FraDico.txt","GerDico.txt"))
    print("Esp-Dut")
    print(simCosinus("EspDico.txt","DutDico.txt"))
    print("Esp-Ger")
    print(simCosinus("EspDico.txt","GerDico.txt"))
    print("Ger-Dut")
    print(simCosinus("DutDico.txt","GerDico.txt"))
    print("Eng-Ita")
    print(simCosinus("EngDico.txt","ItaDico.txt"))
    print("Fra-Ita")
    print(simCosinus("FraDico.txt","ItaDico.txt"))
    print("Ita-Ger")
    print(simCosinus("ItaDico.txt","GerDico.txt"))
    print("Ita-Dut")
    print(simCosinus("ItaDico.txt","DutDico.txt"))
    print("Ita-Esp")
    print(simCosinus("EspDico.txt","ItaDico.txt"))
    print()

#Cette fonction prend le chemin du fichier choisis dans la boite de dialogue une fois qu'on a cliqué sur le bouton "fichier"
def openFile() :
    filename = filedialog.askopenfilename(initialdir = "/",title = "Choisissez un fichier texte", filetypes = (("txt files","*.txt"),("all files","*.*")))
    global chemin
    chemin = filename

""" Cette fonction vérifie si les conditions de recherches sont bien remplies par l'utilisateur.
    Si l'utilisateur a choisis un texte il ne doit pas entrer de phrases et inversement.
"""
def checkString() :
    print("Chemin2: ", chemin)
    print(phrase.get().isdigit())
    if chemin != "" and phrase.get() == "" :
        print("Chemin: ", chemin)
        choiceText(chemin)
    elif phrase.get() != "" and chemin == "" and not phrase.get().isdigit() :
        print("phrase")
        choicePh(phrase.get())
    elif chemin != "" and phrase.get() != "" :
        messagebox.showinfo(message="Vous ne devez choisir qu'un mode de détection")
    elif phrase.get().isdigit() :
        messagebox.showinfo(message="Vous ne devez entrer que des lettres")


""" Cette fonction prend le chemin du fichier choisis et extrait seulement le nom du fichier puis appelle la fonction result()
    Elle est appelée si l'utilisateur a choisit un texte et qu'il a cliqué sur le boutton "Détecter la langue"
"""
def choiceText(fileTxt) :
    effacerOcc()
    global chemin
    contenu = lireF(chemin)
    chemin = chemin.split("/")
    chemin = chemin[len(chemin)-1].split(".")
    result(chemin[0], contenu)

""" Cette fonction prend la phrase entrée par l'utilisateur et appelle la fonction result()
    Elle est appelée si l'utilisateur a choisit d'écrire une phrase et qu'il a cliqué sur le boutton "Détecter la langue"
"""
def choicePh(words) :
    effacerOcc()
    global i
    i += 1
    print("word ",words)
    contenu = lireP(words)
    print(contenu)
    fichierTest = "phrase"+str(i)
    result(fichierTest, contenu)

#Cette fonction execute d'abord la fonction startProg() puis ouvre une nouvelle fenêtre
def openWindow() :

    startProg()
    #Création de la fenêtre principale
    global window
    window = Toplevel(windowMenu)
    window.title("Detecteur de langue")
    window.geometry("2000x400")

    lF = LabelFrame(window, text="Choisissez un fichier texte", padx=20, pady=20)
    exitBtn = Button(window, text="Quitter", command=window.quit)
    findFile = Button(lF, text="Fichier", command=openFile)
    choiceTxt = Button(lF, text="Détecter la langue", command=checkString)

    #Ajout des widgets à la fenêtre
    expliLabel = Label(window, text="""\nPrécisions sur la similarité cosinus : \nComme la valeur cos θ est comprise dans "
        "l'intervalle [-1,1], la valeur -1 indiquera des vecteurs résolument opposés, 0 des vecteurs indépendants (orthogonaux) "
        "et 1 des vecteurs similaires.\nLes valeurs intermédiaires permettent d'évaluer le degré de similarité.\n""").pack()
    lF.pack(fill="both", expand="yes")
    findFile.pack()
    phraseBox = Entry(lF,textvariable=phrase).pack()
    choiceTxt.pack()

    exitBtn.pack()


#Cette fonction créée une nouvelle fenêtre avec le readme écrit dedans.
def openReadMe() :
    readme = Toplevel(windowMenu)
    readme.title("README")

    textRM = lireF("README.md")

    infoLabel = Label(readme,text=textRM)
    exitBtn = Button(readme, text="Quitter", command=readme.withdraw)
    infoLabel.pack()
    exitBtn.pack()


""" Cette fonction nous donne le résultat obtenus après le calcule des similaritées
    cosinus entre les dictionnaires créées précedemment et celui du texte ou de la phrase
"""
def result(fichierTest, contenu) :

    #occ_uni(contenu)
    occ_bi(contenu)
    print(fichierTest)
    ecrireDico("Dico.txt",fichierTest)
    file = fichierTest + "Dico.txt"
    dicoTest = recupVect(file)
    completeDico("EspDico.txt",file)
    completeDico("EngDico.txt",file)
    completeDico("FraDico.txt",file)
    #print(dicoTest)
    print()
    #coordTest = creaVect(dicoTest)
    #print(coordTest)
    print()
    normeTest = normeVect(file)
    simCosEng = simCosinus("EngDico.txt",file)
    simCosFra = simCosinus("FraDico.txt",file)
    simCosEsp = simCosinus("EspDico.txt",file)
    #simCosDut = simCosinus("DutDico.txt",file)
    simCosGer = simCosinus("GerDico.txt",file)

    if(simCosEng < 0) and (simCosEsp < 0) and (simCosFra < 0) and (simCosGer < 0):
        labelRes = Label(window, text="""Puisque tous les résultats des similarités cosinus sont inférieures à 0, alors le texte Test est un texte d'une langue ne faisant pas partie des langues de notre base de données.\nNous obtenons les résultats suivants pour les calculs de similarité avec l'anglais, le français, l'espagnol et l'allemend respectivement : \n"""+str(simCosEng)+", "+str(simCosFra)+", "+str(simCosEsp)+", "+str(simCosGer)+" .\n")
        labelRes.pack()
        #print("""Puisque tous les résultats des similarités cosinus sont inférieures à 0, alors le texte Test est un texte d'une langue ne faisant pas partie des langues de notre base de données.\nNous obtenons les résultats suivants pour les calculs de similarité avec l'anglais, le français et l'espagnol respectivement : \n"""+str(simCosEng)+", "+str(simCosFra)+", "+str(simCosEsp)+" .\n")
    elif(simCosEng == 1.0) or ((simCosEng > simCosFra >= simCosEsp >= simCosGer) or (simCosEng > simCosEsp >= simCosFra >= simCosGer) or (simCosEng > simCosFra >= simCosGer >= simCosEsp) or (simCosEng > simCosEsp >= simCosGer >= simCosFra) or (simCosEng > simCosGer >= simCosFra >= simCosEsp) or (simCosEng > simCosGer >= simCosEsp>= simCosFra)):
        labelRes = Label(window, text="Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'anglais, donc ce texte est un texte en anglais. Taux de similarité : "+str(simCosEng)+" .\n")
        labelRes.pack()
        #print("Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'anglais, donc ce texte est un texte en anglais. Taux de similarité : "+str(simCosEng)+" .\n")
    elif(simCosFra == 1.0) or ((simCosFra > simCosEng >= simCosEsp >= simCosGer) or (simCosFra > simCosEsp >= simCosEng >= simCosGer) or (simCosFra > simCosEng >= simCosGer >= simCosEsp) or (simCosFra > simCosEsp >= simCosGer >= simCosEng) or (simCosFra > simCosGer >= simCosEng >= simCosEsp) or (simCosFra > simCosGer >= simCosEsp>= simCosEng)):
        labelRes = Label(window, text="Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour le français, donc ce texte est un texte en français. Taux de similarité : "+str(simCosFra)+" .\n")
        labelRes.pack()
        #print("Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour le français, donc ce texte est un texte en français. Taux de similarité : "+str(simCosFra)+" .\n")
    elif(simCosEsp == 1.0) or ((simCosEsp > simCosEng >= simCosFra >= simCosGer) or (simCosEsp > simCosFra >= simCosEng >= simCosGer) or (simCosEsp > simCosEng >= simCosGer >= simCosFra) or (simCosEsp > simCosFra >= simCosGer >= simCosEng) or (simCosEsp > simCosGer >= simCosEng >= simCosFra) or (simCosEsp > simCosGer >= simCosFra >= simCosEng)):
        labelRes = Label(window, text="Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'espagnol, donc ce texte est un texte en espagnol. Taux de similarité : "+str(simCosEsp)+" .\n")
        labelRes.pack()
        #print("Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'espagnol, donc ce texte est un texte en espagnol. Taux de similarité : "+str(simCosEsp)+" .\n")
    elif(simCosGer == 1.0) or ((simCosGer > simCosEng >= simCosFra >= simCosEsp) or (simCosGer > simCosFra >= simCosEng >= simCosEsp) or (simCosGer > simCosEng >= simCosEsp >= simCosFra) or (simCosGer > simCosFra >= simCosEsp >= simCosEng) or (simCosGer > simCosEsp >= simCosEng >= simCosFra) or (simCosGer > simCosEsp >= simCosFra >= simCosEng)):
        labelRes = Label(window, text="Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'allemand, donc ce texte est un texte en allemand. Taux de similarité : "+str(simCosGer)+" .\n")
        labelRes.pack()
        #print("Nous avons obtenu que le texte Test était presque identique (ou identique) à nos données pour l'allemand, donc ce texte est un texte en allemand. Taux de similarité : "+str(simCosGer)+" .\n")

    #print()
    #i = i + 1
    #string = input("Voulez-vous tester si le programme peut détecter la langue d'un nouveau texte ? [o,n] ")



#Création de la fenêtre principale

windowMenu.title("Detecteur de langage")
windowMenu.geometry("2000x400")
#Création des widgets
introLabel = Label(windowMenu, text="Bienvenu sur notre programme de détection de la langue"
    "\nSi vous voulez detecter la langue d'un texte ou d'une phrase, cliquez sur le bouton Acceder au programme."
    "\nSi vous souhaitez en savoir plus sur l'utilisation du programme, cliquez sur ReadMe.")
exitBtn = Button(windowMenu, text="Quitter", command=windowMenu.quit)
detectBtn = Button(windowMenu, text="Acceder au programme", command=openWindow)
readmeBtn = Button(windowMenu, text="ReadMe", command=openReadMe)




#Ajout des widgets à la fenêtre
introLabel.pack()
detectBtn.pack()
readmeBtn.pack()
progressBar.pack()
exitBtn.pack()

#Affichage de la fenêtre

windowMenu.mainloop()
