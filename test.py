#3.1
suhu = float(input('Masukkan suhu: '))

if suhu <34.0:
    print('Mati Kedinginan')
elif 34.0<=suhu<=37.0:
    print('Aman')
elif 37.1<=suhu<=39.0:
    print('Demam')
else: print('Mati Kepanasan')

#3.2
angka = int(input('Masukkan bilangan:'))

if angka >0:
    print('Positif')
elif angka <0:
    print('Negatif')
else: print('Nol')

#3.3
a = int(input('Masukkan angka'))
b = int(input('Masukkan angka'))
c = int(input('Masukkan angka'))

if a>b and a>c:
    print('A terbesar')
elif b>a and b>c:
    print('B terbesar')
elif c>a and c>b:
    print('C terbesar')