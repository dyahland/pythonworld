#----------CAPSTONE PROJECT DATA RUMAH SAKIT--------------------

dataPasien=[
['No JKN','Nama','Umur','Jenis Kelamin','Diagnosa','Poli','No Kamar','Status'],
['20150120034','Bambang',56,'Pria','Diabetes','Umum','A001','BPJS'],
['20160120021','Ramlan',29,'Pria','Malaria','Umum','A002','Pribadi'],
['20130120091','Cahaya',45,'Perempuan','Kanker Kulit','Penyakit Dalam','B001','BPJS']]

empty=[]

#menampilkan daftar pasien
def tampil(dataPasien):
    from tabulate import tabulate
    tabel=(tabulate(dataPasien, headers='firstrow',tablefmt='fancy_grid'))
    print (tabel)#tablefmt=menampilkan format table yang akan di print
    return tabel

#mencari pasien berdasarkan nama
def cariNamaPasien(dataBaru):
    for i in range (len(dataPasien)):
        if dataPasien[i][1]==dataBaru:
            return i
    return -1 #berfungsi seperti if not

#mencari pasien berdasarkan noJKN
def cariKodePasien(new_data):
    for i in range (len(dataPasien)):
        if dataPasien[i][0]==new_data:
            return i
    return -1

#verifikasi data apakah jadi/tidak dimasukan, 
def validasi(data,iya,masukan):
    validation=input(f"Apakah mau dilanjutkan {masukan}? Silahkan pilih (Ya/No)").upper()
    if (validation=='NO'):
        print(f"--- Data tidak jadi di{masukan} ---")
        return 0
    elif (iya=='input' and validation=='YA'):
        print("--- Data telah tersimpan ---")
        dataPasien.append(data)
        print((data))
        return 1
    
        
    
def menampilkanData():
    while True:
        print('\t1. Melihat data pasien\n\t2. Kembali ke Menu Utama')
        
        a=input("Masukan pilihan sub menu: ")
        if a=='1':
            tampil(dataPasien)
        elif a=='2':
            break

def mencariData():
    from tabulate import tabulate
    while True:
        print('\t1. Mencari data berdasarkan nama pasien\n\t2. Mencari data berdasarkan no JKN pasien\n\t3. Kembali ke Menu Utama')
        b=input("Masukan pilihan sub menu: ")
        if b =='1':
            cariNama=input("Masukan nama pasien: ").capitalize()
            nama=cariNamaPasien(cariNama)
            if nama==-1:
                print("=============Data yang dicari tidak ditemukan==============\n\t\tMASUKAN KODE YANG BENAR")
            else:
                data=dataPasien[nama]
                print("=======================Data ditemukan=========================")
                headers = ["No JKN", "Nama", "Umur", "Jenis Kelamin", "Penyakit", "Departemen", "No Kamar", "Status"]
                dataBaru = (tabulate([data], headers=headers, tablefmt='fancy_grid'))
                print(dataBaru)
        if b =='2':
            cariKode=input("Masukan kode pasien: ")
            kode=cariKodePasien(cariKode)
            if kode==-1:
                print("=============Data yang dicari tidak ditemukan==============\n\t\tMASUKAN KODE YANG BENAR")
            else:
                data=dataPasien[kode]
                print("=======================Data ditemukan=========================")
                headers = ["No JKN", "Nama", "Umur", "Jenis Kelamin", "Penyakit", "Departemen", "No Kamar", "Status"]
                dataBaru = (tabulate([data], headers=headers, tablefmt='fancy_grid'))
                print(dataBaru)

        if b=='3':
            break
def regisPasien():
    while True:
        print('\t1. Registrasi pasien baru\n\t2. Kembali ke menu utama')
        c=input("Masukan sub menu yang dipilih: ")
        if c == '1':
            newCode=input("Masukan no JKN pasien: ")
            kode=cariKodePasien(newCode)
            if kode !=-1:
                print("===============Data yang akan ditambahkan telah ada=================")
            if kode == -1:
                newName=input("Masukan nama pasien: ").capitalize()
                newAge=int(input("Masukan umur pasien: "))
                newGender=input("Masukan jenis kelamin pasien: ").capitalize()
                newDiagnosa=input("Masukan diagnosa pasien: ").capitalize()
                newDepartemen=input("Masukan poli: ")
                newDepartemen=' '.join ([i.capitalize() for i in newDepartemen.split()])
                newRoomNumber=input("Masukan no kamar pasien: ").upper()
                newStatus=input("Masukan status pasien: ").upper()
                listBaru=[newCode,newName,newAge,newGender,newDiagnosa,newDepartemen,newRoomNumber,newStatus]
                x=validasi(listBaru,'input','update')
                break
        if c == '2':
            break

def upgradePasien():
    # tampilkan data pasien
    tampil(dataPasien)
    while True:
        # minta input nomor JKN yang akan diperbarui
        print('\t1. Edit data pasien\n\t2. Kembali ke menu utama')
        pilih = input('Masukan sub menu yang dipilih: ')
        
        # jika pengguna memasukkan "2", keluar dari loop
        if pilih == "2":
            break
        elif pilih == '1':
            noJKN = input('Masukan nomor JKN yang akan diupdate: ')
        # cari nomor JKN yang cocok pada data pasien
        #found = 0
        for i in range(1, len(dataPasien)):
            if dataPasien[i][0] == noJKN:
                found = True
                index = i
                break
        
        # jika nomor JKN tidak ditemukan, beri pesan kesalahan dan ulangi loop
        if not found:
            print('Nomor JKN tidak ditemukan!')
            continue
        
        # tampilkan opsi yang tersedia
        print('Pilih opsi yang tersedia:')
        print('1. Edit nomor JKN')
        print('2. Edit nama')
        print('3. Edit umur')
        print('4. Edit jenis kelamin')
        print('5. Edit diagnosa')
        print('6. Edit departemen')
        print('7. Edit nomor kamar')
        print('8. Edit status')
        print('9. Kembali ke sub menu' )

        # minta input pilihan
        pilihan = input('Pilihan: ')

        # validasi input pilihan
        if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > 9:
            print('Input tidak valid!')
            continue

        # konversi input pilihan ke integer
        pilihan = int(pilihan)

        # proses pengubahan data sesuai opsi yang dipilih
        if pilihan == 1:
            # minta input nomor JKN baru
            new_noJKN = input('Masukan nomor JKN baru: ')

            # validasi input nomor JKN baru
            if not new_noJKN.isdigit(): 
                print('Input tidak valid!')
                continue
            elif new_noJKN in [dataPasien[i][0] for i in range(1, len(dataPasien))]:
                print('no JKN yang baru diinput sama seperti data sebelumnya')
                continue
            else:
                # konfirmasi pengubahan data
                konfirmasi = input(f'Apakah yakin akan mengubah nomor JKN dari {noJKN} menjadi {new_noJKN}? (y/n) ')
                # proses pengubahan data jika dikonfirmasi
                if konfirmasi.lower() == 'y':
                    dataPasien[index][0] = new_noJKN
                    print('Data berhasil diperbarui!')
                else:
                    print('Anda gagal memperbaharui data')
                break
        elif pilihan == 2:
            # minta input nama baru
            new_nama = input('Masukan nama baru: ').capitalize()
            # validasi input nama baru
            if not new_nama.isalpha():
                print('Input tidak valid!')
                continue
            else:
                for i in range (1,len(dataPasien)):
                    if dataPasien[i][0]==noJKN and dataPasien[i][1]==new_nama:
                        print('Nama yang baru diinput sama seperti data sebelumnya')
                        continue
            # konfirmasi pengubahan data
            konfirmasi = input(f'Apakah yakin akan mengubah nama pasien {dataPasien[index][1]} menjadi {new_nama}? (y/n) ')
            # proses pengubahan data jika dikonfirmasi
            if konfirmasi.lower() == 'y':
                dataPasien[index][1] = new_nama
                print('Data berhasil diperbarui!')
            else:
                print('Anda gagal memperbaharui data')
        

        elif pilihan == 3:
            new_umur = input('Masukan umur baru: ')
            if not new_umur.isdigit():
                print('Input tidak valid!')
                continue
            else:
                for i in range(1,len(dataPasien)):
                    if dataPasien[i][0]==noJKN and dataPasien[i][2]==new_umur:
                        print('Umur yang baru diinput sama seperti data sebelumnya')
                        continue
            konfirmasi = input(f'Apakah yakin akan mengubah umur pasien {dataPasien[index][1]} dari {dataPasien[index][2]} menjadi {new_umur}? (y/n) ')
            if konfirmasi.lower() == 'y':
                dataPasien[index][2] = new_umur
                print('Data berhasil diperbarui!')
            else:
                print('Anda gagal memperbaharui data')

        elif pilihan == 4:
            new_gender=input('Masukan jenis kelamin baru: ').capitalize()
            if not new_gender.isalpha():
                print('Input tidak valid!')
                continue
            else:
                for i in range(1,len(dataPasien)):
                    if dataPasien[i][0]==noJKN and dataPasien[i][3]==new_gender:
                        print('Jenis kelamin yang baru diinput sama dengan data sebelumnya')
                        continue
            konfirmasi=input(f'Apakah yakin akan mengubah jenis kelamin pasien {dataPasien[index][1]} dari {dataPasien[index][3]} menjadi {new_gender}? (y/n) ')
            if konfirmasi.lower() == 'y':
                dataPasien[index][3] = new_gender
                print('Data berhasil diperbarui!')
            else:
                print('Anda gagal memperbaharui data')
    
        elif pilihan == 5:
            new_diagnosa=input('Masukan diagnoasa baru: ').capitalize()
            if new_diagnosa.isdigit():
                print ('Input tidak valid!')
                continue
            else:
                for i in range(1,len(dataPasien)):
                    if dataPasien[i][0]==noJKN and dataPasien[i][4]==new_diagnosa:
                        print('Diagnosa yang baru diinput sama dengan data sebelumnya')
                        continue
            konfirmasi=input(f'Apakah yakin akan mengubah diagnosa pasien {dataPasien[index][1]} dari {dataPasien[index][4]} menjadi {new_diagnosa}? (y/n) ')
            if konfirmasi.lower() == 'y':
                dataPasien[index][4] = new_diagnosa
                print('Data berhasil diperbarui!')
            else:
                print('Anda gagal memperbaharui data')
        elif pilihan == 6:
            new_departemen=input("Masukan poli baru: ").capitalize()
            if new_departemen.isdigit():
                print ('Input tidak valid!')
                continue
            else:
                for i in range(1,len(dataPasien)):
                    if dataPasien[i][0] == noJKN and dataPasien[i][5]==new_departemen:
                        print('Departemen yang baru diinput sama dengan data sebelumnya')
                        continue
            konfirmasi=input(f'Apakah yakin akan mengubah departemen pasien {dataPasien[index][1]} dari {dataPasien[index][5]} menjadi {new_departemen}? (y/n) ')
            if konfirmasi.lower() == 'y':
                dataPasien[index][5] = new_departemen
                print('Data berhasil diperbarui!')
            else:
                print('Anda gagal memperbaharui data')
        elif pilihan == 7:
            new_noKamar=input('Masukan no kamar baru: ').capitalize()
            if not new_noKamar.isalnum():
                print ('Input tidak valid!')
                continue
            else:
                for i in range(1,len(dataPasien)):
                    if dataPasien[i][0] == noJKN and dataPasien[i][6]==new_noKamar:
                        print('No kamar yang baru diinput sama dengan data sebelumnyfa')
                        continue
                konfirmasi=input(f'Apakah yakin akan mengubah no kamar pasien {dataPasien[index][1]} dari {dataPasien[index][6]} menjadi {new_noKamar}? (y/n) ')
                if konfirmasi.lower() == 'y':
                    dataPasien[index][6] = new_noKamar
                    print('Data berhasil diperbarui!')
                else:
                    print('Anda gagal memperbaharui data')  
        elif pilihan == 8:      
            new_status=input('Masukan status baru: ').upper()
            if not new_status.isalpha():
                print ('Input tidak valid!')
                continue
            else:
                for i in range(1, len(dataPasien)):
                    if dataPasien[i][0] == noJKN and dataPasien[i][7]==new_status:
                        print('Status yang baru diinput sama dengan data sebelumnya')
                        continue
                konfirmasi=input(f'Apakah yakin akan mengubah status pasien {dataPasien[index][1]} dari {dataPasien[index][7]} menjadi {new_status}? (y/n) ')
                if konfirmasi.lower() == 'y':
                    dataPasien[index][7] = new_status
                    print('Data berhasil diperbarui!')
                else:
                    print('Anda gagal memperbaharui data')    
        elif pilihan == 9:
            break
def deletePasien():
    while True:
        deletePasien=input('1. Menghapus pasien\n2. Kembali ke menu utama\n Silahkan pilih sub menu dibawah ini:  ')
        if deletePasien == '1':
            tambah_kode = input('Masukan no JKN pasien: ')
            kode=cariKodePasien(tambah_kode)
            if kode == -1:
                print('--- Data pasien yang akan dihapus tidak tersedia ---')
            elif kode != -1:
                while True:
                    check=str(input('Apakah data tersebut yakin dihapus(Ya/No): ')).upper()
                    if check == 'YA':
                        print('Data pasien telah terhapus')
                        empty.append(dataPasien.pop(kode))
                        break
                    if check == 'NO':
                        print('Data pasien tidak jadi dihapus')
                        break
        elif deletePasien== '2':
            break
while True:
    pilihMenu=input('''
        SELAMAT DATANG DI RS PASTI SEMBUH

    List menu data pasien rawat jalan
    \t1. Menampilkan data pasien\n\t2. Mencari data pasien\n\t3. Registrasi Pasien\n\t4. Mengubah data pasien\n\t5. Menghapus data pasien\n\t6. Keluar

    Untuk melanjutkan, silahkan pilih menu dibawah ini: ''')
    if (pilihMenu == '1'):
        menampilkanData()
    elif (pilihMenu == '2'):
        mencariData()
    elif (pilihMenu == '3'):
        regisPasien()
    elif (pilihMenu == '4'):
        upgradePasien()
    elif (pilihMenu == '5'):
        deletePasien()
    else:
        break

    
