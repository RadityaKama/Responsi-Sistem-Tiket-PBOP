# Sistem Pemesanan Tiket Berbasis OOP (Python)
Program ini merupakan simulasi sederhana dari sistem pemesanan tiket dengan pendekatan Object-Oriented Programming (OOP) menggunakan bahasa Python.
Terdapat tiga jenis tiket yang dikelola dalam sistem ini, yaitu Tiket Konser, Tiket Bioskop, dan Tiket Wisata, di mana masing-masing memiliki atribut serta logika perhitungan harga yang berbeda.

# Konsep Utama
Program ini menerapkan empat pilar utama dalam OOP:
1. Inheritance (Pewarisan) → Kelas TiketKonser, TiketBioskop, dan TiketWisata merupakan turunan dari kelas induk Tiket.
2. Encapsulation (Enkapsulasi) → Atribut dan metode tertentu dikelola dalam setiap kelas agar fungsi tetap terstruktur.
3. Polymorphism (Polimorfisme) → Metode tampilkan_info() dan hitung_total() dioverride pada setiap kelas turunan untuk menyesuaikan perilaku sesuai jenis tiketnya.
4. Abstraction (Abstraksi) → Logika umum seperti perhitungan total harga dan pengecekan stok dibuat sederhana agar mudah digunakan oleh kelas turunan.

# Struktur Kelas
Kelas Tiket bertindak sebagai kelas dasar yang berisi atribut utama:
1. nama_event : Nama acara atau destinasi
2. harga : Harga tiket satuan
3. stok : Jumlah tiket yang tersedia
Kelas ini juga menyediakan dua metode dasar:
1. tampilkan_info() → Menampilkan informasi umum tiket
2. hitung_total(jumlah) → Menghitung total harga berdasarkan jumlah tiket yang dibeli

Selanjutnya, terdapat tiga kelas turunan yang memperluas fungsi dari Tiket:
### Kelas TiketKonser
Mewakili tiket konser dengan atribut tambahan kategori (misalnya: VIP, Reguler).
Metode hitung_total() menerapkan sistem diskon otomatis:
1. VIP: Diskon 15% jika total harga melebihi Rp2.000.000
2. Reguler: Diskon 10% jika total harga melebihi Rp1.000.000

### Kelas TiketBioskop
Menambahkan atribut studio untuk menandakan lokasi pemutaran film.
Jika pembelian melebihi 3 tiket, pembeli mendapat diskon 5% dari total harga.

### Kelas TiketWisata
Menambahkan atribut lokasi untuk menunjukkan tempat wisata.
Jika total pembelian melebihi Rp500.000, pembeli mendapat diskon 8%.

# Cara Kerja Program
Ketika program dijalankan, beberapa objek tiket dibuat secara otomatis:
1. tiketkonservip → Konser TripleS kategori VIP
2. tiketkonserreguler → Konser Jondre kategori Reguler
3. tiketbioskop → Film Malam: Suami Kamu dari Zaman Megalitikum
4. tiketwisata → Wisata Tanah Lot di Bali
Program akan menampilkan daftar tiket yang tersedia lengkap dengan detailnya.
Kemudian dilakukan simulasi pembelian tiket oleh beberapa pelanggan, misalnya:
- Raditya membeli 4 tiket konser VIP
- Noordin membeli 8 tiket konser reguler
- Rusdiana membeli 10 tiket bioskop
- PT CenatzCenutz Tbk membeli 350 tiket wisata
Setiap pembelian akan menampilkan total harga beserta keterangan diskon (jika berlaku).
