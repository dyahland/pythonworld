# README PROJECT PYTHON FUNDAMENTAL
## by Dyah Witamara

Program ini adalah program CRUD data pasien di Rumah Sakit Pasti Sembuh dengan menggunakan format data list dalam list. Pemlihan  list dalam list dikarenakan format ini cocok dengan fitur table tabulate yang digunakan untuk menampilkan data pasien.

Sub data yang ada di program ini ada 8 yaitu: No JKN, nama pasien, umur, jenis kelamin, penyakit, departemen, no kamar dan status.
Seperti jenis program nya, program ini akan mengeksekusi fungsi Create, Read, Update, dan Delete.

1. Fungsi Create
. Pertama-tama, dalam program ini terdapat data 3 pasien yang telah ditambahkan sebelumnya dan dapat langsung di tampilkan dengan bantuan tabel tabulate serta fungsi format grid agar lebih rapi. Tapi selain itu, program ini dapat menambahkan data pasien baru yang akan di verifikasi terlebih dahulu apakah data tersebut sebelumnya telah ada atau tidak.
2. Fungsi Read
. Seluruh script dan function dibuat berkorelasi satu sama lain sehingga ketika fungsi 1 dipanggil akan mengikutsertakan fungsi lainnya.
3. Fungsi update
. Pada fungsi update awalnya data pasien yang akan di update dimasukan berdasarkan no JKN, selanjutnya no JKN tersebut akan di cross check terlebih dahulu apakah data pasien tersebut ada di sistem. Selain itu,pada script fungsi update ada banyak verifikasi yang harus dilewati, misalnya kolom NO JKN semua nya harus berisi angka jika tidak akan error demikian juga dengan 7 kolom yang lain, fungsi yang dipakai adalah isalpha, isalnum, dan isdigit.
4. Fungsi delete
. Pada fungsi ini dapat menghapuskan data pasien berdasarkan nomor pasien, pertama-tama nomor pasien yang akan dihapus akan dicari terlebih dahulu apakah ada di dalam sistem atau tidak, jika ada maka seluruh data dari pasien tersebut (no JKN-status) akan dihapus.
5. Fungsi search
. Selain fungsi CRUD, dalam program ini juga menggunakan fungsi search, yaitu pencarian data berupa inputan no JKN dan nama pasien sehingga ketika program dijalankan, hanya data pasien yang dicari tersebutlah yang akan muncul.
