class Kursi:

  def __init__(self):
    """
      Tempat membuat kursi kosong
    """

    self.daftar_kursi = {"A1" : "Kosong",
                          "A2" : "Kosong",
                          "A3" : "Kosong"}
    
  def lihat_kursi(self):
    """
      Tempat melihat kursi
    """
    for nomor, status in self.daftar_kursi.items():
      print(f"{nomor} -- {status}")

  def pesan_kursi(self, nomor_pilihan):

    """
      Fungsi untuk memesan Kursi
    """
    if nomor_pilihan in self.daftar_kursi:
      if self.daftar_kursi[nomor_pilihan] == "Kosong":
        self.daftar_kursi[nomor_pilihan] = "Terisi"
        print(f"Berhasil! Kursi {nomor_pilihan} milik anda")
        return True
      else:
        print(f"Kursi {nomor_pilihan} sudah ada yang punya")
        return False
    else:
      print(f"Kursi {nomor_pilihan} tidak ada")
      return False
  
    
class Film:
  def __init__(self):
    self.daftar_film = ["Anaconda", "Crocodile", "Avengers"]

  def lihat_film(self):
    for film in self.daftar_film:
      print(f"Film : {film}")



film = Film()
pilih_kursi = Kursi()

# melihat film
print("Film Tersedia : ")
film.lihat_film()

# melihat kursi
print("\nKursi Tersedia : ")
pilih_kursi.lihat_kursi()

# Pesan Kursi
pesan_kursi = (input("\nMasukan Kursi yang ingin dipilih : "))
pilih_kursi.pesan_kursi(pesan_kursi)

print("\nSetelah Pesan")
pilih_kursi.lihat_kursi()

# # 5. Coba pilih kursi yang sama (A1) lagi
print("\n--- User Coba Pilih A1 Lagi ---")
pilih_kursi.pesan_kursi("A1")