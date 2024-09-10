# Implementasi Checklist:
## Membuat Proyek Django Baru:
1. Membuat direktori baru dengan nama kiosku
2. Mengaktifkan environment pada direktori 
3. Buat berkas requirements.txt yang berisikan dependencies
4. Install dependencies
5. Buat proyek django dengan nama kiosku
## Membuat aplikasi dengan nama main pada proyek tersebut:
1. Jalankan perintah python manage.py startapp main pada direktori kiosku
2. Daftarkan aplikasi main ke settings.py
3. Tambahkan main ke variabel installed apps
## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Membuka urls.py yang ada di direktori proyek 'lodon_mart' (bukan direktori main).
2. import path,include dari modul django.urls.
3. Menambahkan dalam list url_patterns ( yang awalnya hanya berisi path('admin/', admin.site.urls) ) dengan path('', include('main.urls')).
## Membuat model pada aplikasi main dengan nama Product
1. Membuka models.py dalam direktori aplikasi 'main'.
2. Membuat class baru bernama Product dengan parameter models.Model.
3. Menambahkan atribut name dengan tipe charField, price dengan tipe IntegerField, dan description dengan tipe TextField.
## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
1. Buka berkas views.py yang terletak di dalam berkas aplikasi main.
2. Apabila belum ada, tambahkan baris-baris import from django.shortcuts import render di bagian paling atas berkas.
3. Tambahkan fungsi show_main yang me-return render(request, "main.html", context)
4. Ubah variable dan isi sesuai dengan yang dibutuhkan.
## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Pada file urls.py di direktori main, import path dari modul django.urls.
2. Import fungsi show_main dari main.views.
3. Inisialisasi variabel untuk menyimpan nama aplikasi yaitu 'main'.
4. Membuat list dengan isi path('', show_main, name ='show_main').
## Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
1. Login ke akun PWS yang sudah dibuat
2. Create new project dan buat project name dengan nama kiosku
3. Simpan credential username dan password
4. Tambahkan URL deployment PWS ke settings.py
5. Menjalankan instruksi yang ada di bagian project command di PWS


# Bagan request client

![Alt text](bagan.png)

## Penjelasan
1. Klien mengirimkan request http ke server
2. urls.py menentukan rute URL yang menghubungkan URL tertentu ke view yang sesuai.
3. views.py menangani logika aplikasi dan memproses permintaan yang diterima.
4. models.py menyediakan model data yang dihubungkan dengan basis data.
5. Html template menyediakan struktur HTML untuk merender respons yang dikirim kembali ke klien.
6. Client response merupakan respons akhir yang dikirim kembali ke klien.

# Fungsi git dalam pengembangan perangkat lunak

## Version Control:
untuk melacak perubahan yang dilakukan pada kode sumber dari waktu ke waktu.

## Kolaborasi Tim:
Untuk membantu banyak pengembang mengerjakan proyek bersama
## Reversi dan Pemulihan:
memfasilitasi pemulihan dari kesalahan atau pengembalian ke versi sebelumnya:
## Manajemen Proyek: 
membantu dalam mengelola dan memantau perkembangan proyek

# Framework Django
Menurut saya Django memiliki dokumentasi yang lengkap sehingga memudahkan pemula untuk belajar. Selain itu, Django juga memiliki komunitas yang aktif sehingga memudahkan pembelajaran dan pemecahan masalah. Di Fasilkom sendiri python merupakan bahasa pemrograman di DDP 1 sehingga untuk mempelajari Django sebagai mahasiswa Fasilkom tidak butuh banyak penyesuaian.

# Django disebut ORM
Django disebut ORM karena Django memetakan langsung basis data ke object pada Python sehingga tidak diperlukan lagi menulis query SQL secara langsung.


