#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
import math
import random

def mass_ellipsoide(a = 1, b = 2, c = 3, masse_volumique = 10):
    volume = None
    masse = None
    volume = (4/3) * math.pi * a * b * c
    masse = masse_volumique / volume

    return volume, masse


def ADN_validity(chaine_ADN = None):
    chaine_ADN = input("saisir un brain d'ADN :")
    if "a" not in chaine_ADN:
        print("not valid")
    elif "t" not in chaine_ADN:
        print("not valid")
    elif "c" not in chaine_ADN:
        print("not valid")
    elif "g" not in chaine_ADN:
        print("not valid")
    else:
        print("valid")

    return chaine_ADN

def saisie(length):
    sample_letters = 'atcg'
    result_str = ''.join((random.choice(sample_letters) for i in range(length)))
    print("chaîne:", result_str)

    return result_str

def proportion():
    c = input("input 2 ADN carachter:")
    ratio = (c.count(c)) / len(saisie())

    return c

if __name__ == '__main__':
    # masse ellipsoide
    print("le volume et la masse sont respectivement de ", round(mass_ellipsoide()[0], 2), "L et", round(mass_ellipsoide()[1], 2), "Kg")
    print("le volume et la masse sont respectivement de ", round(mass_ellipsoide(5, 4, 10, 20)[0], 2), "L et", round(mass_ellipsoide(5, 4, 10, 20)[1], 2), "Kg")
    
    # Vérification ADN
    print("\n   Verifying ADN...")
    ADN_validity()

    saisie(20)

    proportion()