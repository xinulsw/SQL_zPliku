#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def pobierz_dane(plikcsv):
    """
    funkcja zwraca tuplę tupli zawierajacych dane
    z pliku csv do zapisania w tabeli"""

    dane = []  # deklarujemy pustą liste
    if os.path.isfile(plikcsv):  # sprawdzamy czy plik istnieje na dysku
        with open(plikcsv, "r") as zawartosc:  # otwieramy plik do odczytu
            zawartosc.readline()
            for linia in zawartosc:
                linia = linia.replace("\n", "")  # usuwamy znaki końca lini
                linia = linia.replace("\r", "")  # usuwamy znaki konca lini
                linia = linia[:-1]  # usuwamy znak ";" z końca linii
                # odczytujemy znaki jako utf-8
                linia = linia.replace("utf-8", "")
                # dodajemy elementy do tupli a tuplę do listy
                dane.append(tuple(linia.split(";")))
    else:
        print("Plik z danymi: ", plikcsv, " nie istnieje!")

    return tuple(dane)  # przeksztalcamy liste na tuple i zwracamy ja
