class Tiket():
    def __init__(self, nama_event, harga, stok):
        self.nama_event = nama_event
        self.harga = harga
        self.stok = stok
    
    def tampilkan_info(self):
        return f"Event: {self.nama_event}, Harga: {self.harga}, Stok: {self.stok}"
    
    def hitung_total(self, jumlah):
        if jumlah > self.stok:
            return "Stok tidak mencukupi."
        else:
            total_harga = self.harga * jumlah
            return f"Total harga untuk {jumlah} tiket adalah {total_harga}"

class TiketKonser(Tiket):
    def __init__(self, nama_event, harga, stok, kategori):
        super().__init__(nama_event, harga, stok)
        self.kategori = kategori
    
    def tampilkan_info(self):
        return super().tampilkan_info() + f", Kategori: {self.kategori}"
    
    def hitung_total(self, jumlah): 
        if jumlah > self.stok:
            return "Stok tidak mencukupi."
        
        total_harga = self.harga * jumlah
        diskon = 0
        keterangan_diskon = ""
        
        if self.kategori.lower() == "vip":
            if total_harga > 2000000:
                diskon = 0.15
                keterangan_diskon = " (Diskon 15%)"
        elif self.kategori.lower() == "reguler":
            if total_harga > 1000000:
                diskon = 0.10
                keterangan_diskon = " (Diskon 10%)"
        
        total_bayar = total_harga * (1 - diskon)
        return (f"Total harga untuk {jumlah} tiket {self.kategori} {keterangan_diskon} "
                f"adalah Rp {total_bayar:,.0f}")

class TiketBioskop(Tiket):
    def __init__(self, nama_event, harga, stok, studio):
        super().__init__(nama_event, harga, stok)
        self.studio = studio 
    
    def tampilkan_info(self):
        return super().tampilkan_info() + f", Studio: {self.studio}"
    
    def hitung_total(self, jumlah):
        if jumlah > self.stok:
            return "Stok tidak mencukupi."
        
        total_harga = self.harga * jumlah
        diskon = 0
        keterangan_diskon = ""

        if jumlah > 3:
            diskon = 0.05
            keterangan_diskon = " (Diskon 5%)"
            
        total_bayar = total_harga * (1 - diskon)
        return (f"Total harga untuk {jumlah} tiket Bioskop {keterangan_diskon} "
                f"adalah Rp {total_bayar:,.0f}")

class TiketWisata(Tiket):
    def __init__(self, nama_event, harga, stok, lokasi):
        super().__init__(nama_event, harga, stok)
        self.lokasi = lokasi
    
    def tampilkan_info(self):
        return super().tampilkan_info() + f", Lokasi: {self.lokasi}"
    
    def hitung_total(self, jumlah):
        if jumlah > self.stok:
            return "Stok tidak mencukupi."
        
        total_harga = self.harga * jumlah
        diskon = 0
        keterangan_diskon = ""
        
        if total_harga > 500000:
            diskon = 0.08
            keterangan_diskon = " (Diskon 8%)"
        
        total_bayar = total_harga * (1 - diskon)
        return (f"Total harga untuk {jumlah} tiket Wisata{keterangan_diskon} "
                f"adalah Rp {total_bayar:,.0f}")
    
tiketkonservip=TiketKonser("Konser TripleS", 5000000, 150, "VIP")
tiketkonserreguler=TiketKonser("Konser Jondre", 250000, 1000, "Reguler")
tiketbioskop=TiketBioskop("Malam: Suami Kamu dari Zaman Megalitikum", 50000, 60, "Studio 1")
tiketwisata=TiketWisata("Tanah Lot", 30000, 500, "Bali")

print("\n" + "="*50 + "\n")

print("Daftar Tiket dan Total Harga:\n")
print(tiketkonservip.tampilkan_info())
print(tiketkonserreguler.tampilkan_info())
print(tiketbioskop.tampilkan_info())
print(tiketwisata.tampilkan_info())

print("\n" + "="*50 + "\n")

print("Pembelian Tiket:\n")
print("\nPembelian 1 (Raditya - Konser VIP):")
print(tiketkonservip.hitung_total(4))
print("\nPembelian 2 (Noordin - Konser Reguler):")
print(tiketkonserreguler.hitung_total(8))
print("\nPembelian 3 (Rusdiana - Bioskop):")
print(tiketbioskop.hitung_total(10))
print("\nPembelian 4 (PT CenatzCenutz Tbk. - Wisata):")
print(tiketwisata.hitung_total(350))
print("\nPembelian 5 (Tiwul - Konser Reguler):")
print(tiketkonserreguler.hitung_total(2))