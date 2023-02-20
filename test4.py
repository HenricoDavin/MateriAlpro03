ubin1 = int(input('Masukkan jumlah ubin 1 meter: '))
ubin5 = int(input('Masukkan jumlah ubin 5 meter: '))
panjang = int(input('Masukkan panjang yang ingin ditutupi ubin: '))

if (1*ubin1 + 5*ubin5)>=panjang:
    if panjang%5==0 and panjang//5<=ubin5:
        print('Bisa')
    elif panjang%5<=ubin1:
        print('Bisa')
    else: print('Tidak Bisa')
else: print('Tidak Bisa')