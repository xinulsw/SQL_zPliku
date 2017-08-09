#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from pob_dane import pobierz_dane

con = sqlite3.connect('test.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

# najpierw musimy utworzyć tabele i relacje między nimi
# tworzenie tabel
cur.execute("DROP TABLE IF EXISTS aktynom;")
# execute dla jednego polecenia
cur.execute("""
CREATE TABLE IF NOT EXISTS aktynom(
    data varchar(200),
    stacja integer,
    calkow float,
    rozpr float,
    bezposr float,
    kon varchar(20)
)""")


aktyn = pobierz_dane('GDY_201705.csv')
print(aktyn)

cur.executemany('INSERT INTO aktynom (data, stacja, calkow, rozpr, bezposr, kon) VALUES (?, ?, ?, ?, ?, ?)', aktyn)
cur.execute('SELECT * FROM aktynom')

wynik = cur.fetchall()
for w in wynik:
    print(w['data'], w['stacja'], w['calkow'], w['rozpr'], w['bezp'], w['kon'])
