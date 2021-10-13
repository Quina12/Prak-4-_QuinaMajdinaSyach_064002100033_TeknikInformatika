# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 08:23:28 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

#Konversi bilangan desimal-biner dan biner-desimal 
def o1():
    #desimal ke biner
    bilangan = int(input('Masukkan bilangan: '))
    
    #khusus 1
    if bilangan == 1:
        hasil = 1
    else:
        #proses
        result = []
        first = bilangan % 2
        result.append(first)
        proses = True
        while proses == True:
            bilangan = bilangan // 2
            biner = bilangan % 2
            result.append(biner)
            if bilangan == 1:
                proses = False 
        result.reverse()
        hasil = ' '.join(map(str, result))
    print ('Nilai biner adalah: ',hasil)
    input('\nPRESS ENTER')

def o2():
    #biner ke desimal
    biner = str(input('Masukkan biner: '))
    biner2 = list(biner)
    binerl = []
    for i in range(len(biner2)):
        binerl.append(int(biner2[i]))
    binerl.reverse()
    hasil = int()
    kons = 1
    tambah = binerl[0] * kons
    hasil += tambah
    for i in range(1,len(binerl)):
        kons = kons*2
        tambah = binerl[i] * kons
        hasil += tambah
    print('Nilai bilangan desimal:',hasil)
    input('\nPRESS ENTER')

ulang = True
while ulang == True:    
    
    # User interface
    print("   ----Program Konversi Bilangan----")
    print('''
    Pilih fungsi yang akan digunakan:
        1. Desimal  =>  Biner
        2. Biner    =>  Desimal
        3. Keluar''')
    opsi = str(input('\nSilahkan pilih menu>> '))
    if opsi == '1':
        o1()
    elif opsi == '2':
        o2()
    elif int(opsi) == 3:
        print("Terimakasih telah menggunakan program ini")
        break
    else:
        ulang = False