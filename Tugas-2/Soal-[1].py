nama =["rian", ]
nomor=["08989565463",]


def tambahkontak():
    tambahnama =input("nama : ")
    tambahnomor =int(input("no telefon : "))
    nama.append(tambahnama)
    nomor.append(tambahnomor)
    print("Kontak Berhasil Ditambah")

def daftarkontak():
    print("Daftar Kontak:")
    for i,c in zip(nama, nomor): 
        print("daftar nama: ", i +"\n No telefon : ", c)
    
    #for i in range(len(nama)):
        #print("Daftar nama : ",nama[i] )
         #print("No telefon : ", nomor[i])

def selesaikontak():
    print("Program Selesai")

while True:
    print("Selamat datang!")
    print("--Menu-- \n1. Daftar kontak \n2. Tambah kontak \n3. Keluar")

    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
     daftarkontak()
     print()
    elif pilihan == 2:
     tambahkontak()
     print()
    elif pilihan ==3 :
        selesaikontak()
        print()
        break
    else:
        print("Menu Tidak Tersedia")
        print()
        

