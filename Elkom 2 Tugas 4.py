# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:01:37 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

P = []

Pstr = list(input('Masukkan angka2: ').split(' '))
for i in range (len(Pstr)):
    x = int(Pstr[i])
    P.append(x)

result = 'idk'

for i in range(len(P)):
    hitung = P[i] % 2
    if hitung == 0:
        result = 'Memiliki angka genap di dalam list'
        break
    else:
        result = 'Tidak memiliki angka genap di dalam list'
        
print (result)
