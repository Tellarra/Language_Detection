# -*- coding: utf-8 -*-
#!usr/bin/env python3.6

from __future__ import unicode_literals
import re
import os
import sys
import io
import ReadFiles
import json


ponctuation = r"\t|\n|\s|\.|\,|\;|\?|\!|\'|\-|\:|\/\w+|.\/.|\s+"
chiffres = r'\d+\s'
occ = {}

def lireF(fichier):
    """La méthode lireF(f) permet de récupérer le nom d'un fichier et de l'ouvrir, en lecture uniquement
    et de renvoyer une chaine de caractères composée seulement des lettres non accentuées du texte."""

    with io.open(fichier,"r", encoding="utf8", errors="ignore") as f :
        l = re.sub("[^a-zA-Z]+", '', f.read())
        l = l.lower()
    return l

def lireP(phrase):
    l = re.sub("[^a-zA-Z]+", '', phrase)
    l = l.lower()
    return l

def ecrireDico(fichier, pays):
    """Cette méthode écrit le contenu du dictionnaire dans un fichier .txt
        et le met à jour en fonction des résultats obtenus """
    myFile = pays + "Dico.txt"
    occ2 = dict()
    print(os.path.isfile(myFile))
    if os.path.isfile(myFile) :
        occ2 = lireDico(myFile)
        for key, value in occ.items():
            if key in occ2 and occ2[key] is not None :
                occ2[key] += value
            else:
                occ2[key] = value
        with open(myFile, 'w', encoding="utf8") as f:
            f.write(json.dumps(occ2))
    else :
        with open(myFile, 'w', encoding="utf8") as f:
            f.write(json.dumps(occ))


def lireDico(fichier) :
    data = dict()
    with open(fichier, encoding="utf8") as raw_data:
        val = raw_data.read()
        data = json.loads(val)
    #print("data : ", data)
    return data

def lireDicoKey(fichier):
    t = list()
    data = dict()
    if re.match(r'\w+Dico\.txt',fichier):
        with open(fichier, encoding="utf8") as raw_data:
                val = raw_data.read()
                data = json.loads(val)
                for key, value in data.items() :
                    t.append(key)
    return t


def completeDico(fichier1,fichier2):
    if(re.match(r'\w+Dico.txt',fichier1) and re.match(r'\w+Dico.txt',fichier2)):
        dicoF1 = lireDico(fichier1)
        dicoF2 = lireDico(fichier2)
        keyF1 = lireDicoKey(fichier1)
        keyF2 = lireDicoKey(fichier2)
        for i in keyF1:
            if(i not in keyF2):
                 dicoF2[i]= 0
        with open(fichier2, 'w', encoding='utf-8') as fic:
            fic.write(json.dumps(dicoF2))

def supprZeroDico(fichier):
    l = list()
    dico = lireDico(fichier)
    for key, value in dico.items():
        if (value == 0):
            l.append(key)
    for i in l :
        del dico[i]
    with open(fichier, 'w', encoding="utf8") as fic:
            fic.write(json.dumps(dico))


def occ_uni(obj):
    """Cette méthode permet de récupérer les occurrences des lettres dans un texte et
    retourne le dictionnaire ayant pour clé la lettre et pour valeur le nombre d'occurrences."""
    #occ = {}
    for i in obj :
        if i in occ and (not re.match(ponctuation,i) and not re.match(chiffres,i)):
            occ[i] += 1
        elif i not in occ and (not re.match(ponctuation,i) and not re.match(chiffres,i)):
            occ[i] = 1
    return occ


def occ_bi(obj):
    """Cette méthode permet de récupérer les occurrences des bi-grammes de lettres dans un texte et
    retourne le dictionnaire ayant pour clé le bi-gramme et pour valeur le nombre d'occurrences."""
    global occ
    liste_Lettres = [i for i in obj]
    #print(liste_Lettres)
    for j in range(len(liste_Lettres)-1):
        a = liste_Lettres[j]+liste_Lettres[j+1]
        if a in occ and (not re.match(ponctuation,a) and not re.match(chiffres,a)):
            occ[a] += 1
        elif a not in occ and (not re.match(ponctuation,a) and not re.match(chiffres,a)):
            occ[a] = 1
    return occ

def effacerOcc():
    global occ
    occ = {}
