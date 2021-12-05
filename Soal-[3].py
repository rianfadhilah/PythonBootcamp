teori = int(input("Masukkan Nilai Ujian Teori: "))
praktek = int (input("Masukkan Nilai Ujian Praktek: "))
if teori >=70 and praktek >=70:
    print("Selamat, Anda lulus!")
elif teori >=70 and praktek < 70:
    print("Anda Harus Mengulang Ujian Praktek")
elif teori <70 and praktek >= 70:
    print("Anda Harus Mengulang Ujian Teori")
else:
    print("Anda Harus Mengulang Ujian Teori dan Praktek")