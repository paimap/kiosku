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

# TUGAS 3
# Fungsi Data Delivery
Data delivery diperlukan karena memungkinkan transfer dan pertukaran informasi yang efisien antara berbagai komponen sistem, pengguna, atau perangkat. Dalam konteks e-commerce, data delivery memastikan bahwa informasi penting seperti produk, transaksi, dan status pengiriman dapat diakses, diproses, dan dikelola dengan baik.

# Perbandingan JSON dan XML
Saya pribadi lebih memilih JSON karena lebih sederhana dan lebih mudah dibaca dibandingkan dengan XML. JSON menggunakan lebih sedikit karakter dan memiliki struktur yang lebih ringkas daripada XML yang menggunakan banyak tag. Menurut saya hal itu juga yang membuat JSON lebih populer dibanding XML.

# Fungsi Method is_valid() pada Form Django
Method is_valid() pada form Django memiliki peran penting dalam memverifikasi data yang dimasukkan ke dalam form. Kita membutuhkan method tersebut untuk memeriksa apakah data yang dikirim melalui form memenuhi semua aturan validasi yang telah ditentukan, baik itu validasi default dari Django maupun validasi kustom yang kita buat.

# CSRF Token
Kita membutuhkan csrf_token karena Django memberikan csrf_token untuk memastikan bahwa setiap permintaan POST berasal dari sumber yang sah, yaitu form yang dibuat oleh aplikasi sendiri dan bukan dari situs pihak ketiga yang berbahaya. Jika kita tidak menambahkan csrf_token pada form Django, aplikasi akan menjadi rentan terhadap serangan CSRF. Tanpa csrf_token, aplikasi tidak memiliki mekanisme untuk membedakan antara permintaan yang sah dari form di situs dengan permintaan yang berasal dari sumber berbahaya. Serangan CSRF memanfaatkan hubungan kepercayaan antara pengguna yang telah login dan server. Karena browser secara otomatis mengirimkan cookie sesi dalam setiap permintaan, penyerang dapat membuat permintaan berbahaya yang terlihat sah dari perspektif server.

# Implementasi Checklist

## Membuat input form untuk menambahkan objek model pada app sebelumnya.
1. Buat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data Stock Entry baru.
2. Buka berkas views.py yang ada pada direktori main dan tambahkan from django.shortcuts import render, redirect ; from main.forms import StockEntryForm ; from main.models import StockEntry pada bagian paling atas.
3. buat fungsi baru dengan nama create_stock_entry yang menerima parameter request.
4. Buka urls.py yang ada pada direktori main dan import fungsi create_stock_entry yang sudah dibuat tadi.
5. Tambahkan path URL ke dalam variabel urlpatterns pada urls.py di main untuk mengakses fungsi yang sudah di-import pada poin sebelumnya.
6. Buat berkas HTML baru dengan nama create_stock_entry.html pada direktori main/templates. Isi create_stock_entry.html dengan kode berikut.
7. Buka main.html dan tambahkan kode untuk menampilkan data stock dalam bentuk tabel serta tombol "Add New Stock Entry" yang akan redirect ke halaman form di dalam {% block content %}. 

## Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
1. Buka views.py yang ada pada direktori main dan tambahkan import HttpResponse dan Serializer pada bagian paling atas.
2. Buatlah sebuah fungsi baru yang menerima parameter request dengan nama show_xml dan show_json kemudian buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada StockEntry.
3. Tambahkan return function berupa HttpResponse di show_xml yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml".
7. Tambahkan return function berupa HttpResponse di show_json yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json".
10. Pada file yang sama buatlah dua fungsi baru yang menerima parameter request dan id dengan nama show_xml_by_id dan show_json_by_id.
11. Buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada StockEntry.
12. Tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON).

## Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
1. Buka urls.py yang ada pada direktori main dan import fungsi yang sudah dibuat tadi (from main.views import show_main, create_stock_entry, show_xml, show_json, show_xml_by_id, show_json_by_id).
2. Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi (path('', show_main, name='show_main'), path('create-stock-entry', create_stock_entry, name='create_stock_entry'), path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json'), path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'), path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),).

# Akses Menggunakan Postman

![Alt text](json.png)
![Alt text](xml.png)
![Alt text](json_with_id.png)
![Alt text](xml_with_id.png)


# Tugas 4
# Perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect adalah class bawaan Django yang secara eksplisit membuat HTTP response dengan kode status 302 (redirect) dan header "Location" yang mengarah ke URL baru. Sedangkan redirect adalah fungsi shortcut yang disediakan oleh Django untuk mempermudah pengalihan dan akan secara otomatis menggunakan HttpResponseRedirect() di belakang layar.
# Cara Kerja Penghubungan Model Product dengan User
Menghubungkan model Product dengan model User dalam Django biasanya melibatkan penggunaan relasi ForeignKey atau ManyToManyField, tergantung pada hubungan yang ingin dibentuk antara kedua model tersebut.
# Perbedaan antara Authentication dan Authorization
Authentication adalah proses verifikasi identitas pengguna seperti melalui username dan password. Sedangkan authorization adalah proses menentukan hak akses pengguna setelah mereka terautentikasi seperti izin untuk mengakses halaman admin atau mengubah data. Django mengimplementasikan authentication melalui sistem User dan Session, sedangkan authorization melalui permissions dan groups.
# Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang login dengan menggunakan session cookies yang menyimpan session ID, menghubungkan pengguna dengan data sesi di server. Cookies digunakan untuk banyak hal, termasuk autentikasi, menyimpan preferensi pengguna, dan pelacakan aktivitas pengguna. Tidak semua cookies aman, sehingga cookies harus dilindungi dengan pengaturan seperti Secure, HttpOnly, dan CSRF protection untuk mencegah serangan dan kebocoran data.
# Implementasi Checklist
## Implementasi Fungsi Register
1. Tambahkan import UserCreationForm dan messages pada bagian paling atas views.py.
2. Tambahkan fungsi register yang berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form ke dalam views.py.
3. Buatlah berkas HTML baru dengan nama register.html pada direktori main/templates. Isi register.html dengan html yang menampilkan form register.
4. Impor fungsi yang sudah dibuat ke urls.py
5. Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

## Implementasi Fungsi Login
1. Tambahkan import authenticate, login, dan AuthenticationForm pada bagian paling atas pada views.py.
2. Tambahkan fungsi login_user yang berfungsi untuk mengautentikasi pengguna yang ingin login ke dalam views.py.
3. Buatlah berkas HTML baru dengan nama register.html pada direktori main/templates. Isi register.html dengan html yang menampilkan form login.
4. Impor fungsi yang sudah dibuat ke urls.py
5. Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

## Implementasi Fungsi Logout
1. Tambahkan import logout pada bagian paling atas pada views.py.
2. Tambahkan fungsi logout_user yang berfungsi untuk melakukan mekanisme logout ke dalam fungsi views.py.
3. Tambahkan button logout pada main.html
4. Impor fungsi yang sudah dibuat ke urls.py
5. Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

## Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
![Alt text](akun_dan_dummy_1.png)
![Alt text](akun_dan_dummy_2.png)

## Menghubungkan model Product dengan User.
1. Tambahkan import from django.contrib.auth.models import User pada bagian paling atas pada models.py.
2. Pada model StockEntry yang sudah dibuat, tambahkan potongan kode user = models.ForeignKey(User, on_delete=models.CASCADE).
3. Ubah value dari stock_entries menjadi StockEntry.objects.filter(user=request.user) dan context pada fungsi show_main menjadi 'name': request.user.username,.
4. Simpan semua perubahan, dan lakukan migrasi model dengan python manage.py makemigrations
5. Lakukan python manage.py migrate untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya.
6. Tambahkan sebuah import baru pada settings.py yang ada pada subdirektori mental_health_tracker yaitu import os.
7. Ganti variabel DEBUG dari berkas settings.py menjadi seperti ini. PRODUCTION = os.getenv("PRODUCTION", False) DEBUG = not PRODUCTION

# Tugas 5
# Urutan Prioritas Pengambilan CSS Selector
1. Inline Style
Style yang ditentukan langsung pada elemen HTML menggunakan attribute style.
2. ID Selector
Selector yang menggunakan ID elemen dan setiap elemen harus unik.
3. Class Selector 
Selector yang menggunakan kelas
4. Element Selector
Selector yang menggunakan nama elemen HTML
5. Universal Selector
Selector yang ditandai dengan *. Selector ini akan diterapkan pada seluruh elemen

# Responsive Design
desain responsif akan memudahkan pengguna untuk melakukan aktivitas pada aplikasi web kita di berbagai perangkat seperti desktop, tablet, dan smartphone. Desain responsif memungkinkan aplikasi web untuk menyesuaikan ukuran dan resolusi sehingga dapat dilihat tanpa melakukan zoom.

# Margin, Border, dan padding
## Margin 
Margin adalah ruang di luar kotak untuk membuat jarak antara kotak dan elemen lainnya.
## Border
Border adalah garis yang mengelilingi kotak.
## Padding
Padding adalah ruang di dalam kotak, berada di antara konten dan border.

# Flex Box dan Grid Layout
## Flex Box
Flexbox adalah layout CSS yang dirancang untuk menyusun elemen dalam satu dimensi secara horizontal atau vertikal. Dengan menggunakan flexbox, kita dapat mengatur bagaimana elemen di dalam kontainer berubah terhadap ukuran ruang yang tersedia.
## Grid Layout
Grid Layout adalah layout CSS yang berguna untuk menyusun elemen dalam dua dimensi (baris dan kolom). Grid layout dapat membuat desain kompleks yang terstruktur, dan mengatur penempatan elemen dalam grid.

# Implementasi Checklist
## Fungsi Mengedit
1. buat fungsi baru bernama edit_stock yang menerima parameter request dan id di views.py
2. Buatlah berkas HTML baru dengan nama edit_stock.html pada subdirektori main/templates dan isi berkas tersebut.
3. Buka urls.py yang berada pada direktori main dan import fungsi edit_stock yang sudah dibuat.
4. Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
5. Tambahkan button yang memanggil edit_stock.

## Fungsi Menghapus
1. buat fungsi baru bernama delete_stock yang menerima parameter request dan id di views.py
2. Buatlah berkas HTML baru dengan nama delete_stock.html pada subdirektori main/templates dan isi berkas tersebut.
3. Buka urls.py yang berada pada direktori main dan import fungsi delete_stock yang sudah dibuat.
4. Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
5. Tambahkan button yang memanggil delete_stock.

## Kostumisasi Desain pada HTML yang Telah dibuat
1. Buatlah berkas HTML baru dengan nama navbar.html pada folder templates/ di root directory. Isi berkas navbar.html sesuai dengan desain yang diinginkan.
2. tautkan navbar tersebut ke dalam main.html, create_stock_entry.html, dan edit_stock.html yang berada di subdirektori main/templates/ dengan menggunakan tags include.
3. Buatlah file global.css di /static/css pada root directory dan tambahkan kelas custom atau style css yang sudah didefinisikan.
4. Hubungkan global.css dan script Tailwind ke base.html.
5. Ubah login.html sesuai dengan desain yang ingin dibentuk.
6. Ubah halaman register.html sesuai dengan desain yang ingin dibentuk.
7. Styling main.html dengan menambah card_info.html dan card_stock.html dan tambahkan button edit dan hapus lalu buat kondisi jika stock kosong.
8. Ubah edit_stock.html sesuai dengan desain yang ingin dibentuk.
9. Ubah create_stock.html sesuai dengan desain yang ingin dibentuk.

# Tugas 5
# Manfaat JavaScript dalam Pengembangan Aplikasi Web
JavaScript bermanfaat untuk membangun aplikasi web yang responsif, interaktif, dan kaya fitur. 
# Fungsi Await ketika Menggunakan Fetch
Await berfungsi untuk menunggu hingga promise selesai sebelum melanjutkan ke baris kode berikutnya. Jika await tidak digunakan, hasil fetch() akan berupa promise yang belum diselesaikan, sehingga data yang diharapkan belum siap digunakan.
# Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Kita menggunakan @csrf_exempt pada view yang akan digunakan untuk AJAX POST agar Django tidak memeriksa token CSRF, sehingga mencegah terjadinya kesalahan 403 Forbidden.
# pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan harus selalu dilakukan di backend karena server memiliki kendali penuh atas proses tersebut dan tidak bisa dimanipulasi oleh pengguna sehingga memberikan perlindungan tambahan, menjaga integritas data, dan memastikan bahwa sistem aman dari serangan atau manipulasi data.

# Implementasi Checklist
## Membuat Fungsi untuk Menambah Stock dengan AJAX
1. Tambahkan impor csrf_exempt dan require_POST ke views.py
2. Buat fungsi add_stock_entry_ajax yang menerima parameter request 
3. import fungsi yang telah dibuat ke views.py
4. tambahkan path url ke urlpatterns

## Menampilkan Data Stock Entry dengan fetch() API
1. pada views.py ubah data menjadi data = StockEntry.objects.filter(user=request.user)
2. Ubah block conditional pada stock entry menjadi < div id="stock_entry_cards"></ div>
3. buatlah fungsi baru pada block < script > tersebut dengan nama getStockEntries
4. Buat fungsi baru pada block < script >  dengan nama refreshStockEntries yang digunakan untuk me-refresh data stock secara asinkronus.

##  Membuat Modal Sebagai Form untuk Menambahkan Stock
1. Ubah bagian tombol Add New Stock Entry menjadi < a href="{% url 'main:create_stock_entry' %}" class="bg-indigo-400 hover:bg-indigo-400 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mx-4 "> Add New Stock Entry < /a >. 
2. Tambahkan tombol baru untuk melakukan penambahan data dengan < button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();"> Add New Stock Entry by AJAX </ button>

## Menambahkan Data Stock dengan AJAX
1. Buatlah fungsi baru pada block < script > dengan nama addStockEntry.
2. Tambahkan sebuah event listener pada form yang ada di modal untuk menjalankan fungsi addStockEntry().








