import sys

print ('\t\t\t=================')
print ('\t\t\tJUAL HEWAN QURBAN')
print ('\t\t\t=================')
print ()
hewan=4
jawaban= False
while jawaban == False :
    tebak = int(input('tebak ada berapa jenis hewan qurban? : '))
    if tebak>hewan :
        print('banyak banget')
    elif tebak<hewan :
        print('masa cuma segitu sih')
    elif tebak==hewan :
        break;
print ('Betul ayo lanjut belanja!')

print("TERSEDIA HEWAN QURBAN : ")
print("1. Sapi Large : Rp 16.000.000,- ")
print("2. Sapi Reguler : Rp 12.500.000,- ")
print("3. Kambing Large : Rp 4.500.000,- ")
print("4. Kambing Reguler : Rp 2.000.000,- ")
print ()

print(' Promo Diskon: ')
print('\t\t\t1. Diskon 50% untuk prmbrlian datas 24 juta')
print('\t\t\t2. Diskon 35% untuk prmbrlian datas 15 juta')
print('\t\t\t3. Diskon 20% untuk prmbrlian datas 8 juta')

print()
pilih = int(input('pilih jenis hewan (1/2/3/4) ? : '))

if pilih==1 :
    hargaHewan= 16000000
elif pilih==2 :
    hargaHewan= 12500000
elif pilih==3 :
    hargaHewan= 4500000
elif pilih==4 :
    hargaHewan = 2000000
else :
    print ()
    print ('Belum Tersedia')
    print ('Terimakasih')
    sys.exit()
    

jumlah = int(input('berapa banyak pembelian ? : '))
pembelian = hargaHewan*jumlah
if pembelian >= 24000000 :
    diskon = 50
elif pembelian >= 15000000 :
    diskon = 35
elif pembelian >= 8000000 :
    diskon = 20
else :
    diskon = 0
totalDiskon = pembelian * diskon/100
totalPembelian= pembelian - totalDiskon

print()
print('\t\t\t Hasil Pembelian Anda')
print('\t\t\t ====================')
print()
print('Pilihan Hewan : %d' %pilih)
print('Harga Hewan : Rp. %d' %hargaHewan)
print('Jumlah Pembelian : %d Kambing' %jumlah)
print('Pembelian : Rp. %d' %pembelian)
print('Diskon : %d%%' %diskon)
print('Total Diskon : %d' %totalDiskon)
print('------------------------------')
print('Total : Rp. %d' %totalPembelian)

print()
print('Terimakasih telah membeli semoga berkah')
