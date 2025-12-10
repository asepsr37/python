class Studio:

  def __init__(self):
    self.daftar_kursi = {"A1" : "Kosong",
                         "A2" : "Kosong",
                         "A3" : "Kosong"}

    self.daftar_film = {"1" : "Anaconda",
                        "2" : "Lake Placid",
                        "3" : "Deep Blue Sea"}

    self.studio_film = {"1" : "Studio 1",
                       "2" : "Studio 2",
                       "3" : "Studio 3"}

  def fungsi_penayangan_film(self):
    for nomor, (kode, judul) in enumerate(self.daftar_film.items(), start=1):
      studio = self.studio_film.get(kode)
      print(f"{nomor}. {judul} -- {studio}")

  def melihat_kursi(self):
    for x, y in self.daftar_kursi.items():
      print(f"Kursi : {x} -- {y}")

  def pesan_kursi(self, nomor_pilihan):
    if nomor_pilihan in self.daftar_kursi:
      if self.daftar_kursi[nomor_pilihan] == "Kosong":
        self.daftar_kursi[nomor_pilihan] = "Terisi"
        print(f"Pesan Kursi {nomor_pilihan} Berhasil")
        return True
      else:
        print(f"Kursi {nomor_pilihan} Telah terisi, silahkan pilih kursi lain")
        return False
    else:
      return False

class Customer:

  def __init__(self, studio):
    self.studio = studio

  def customer_pesan_kursi(self):
      while True:
        customer_pesan_kursi = input("\nMasukan Kursi yang ingin dipesan : ")

        if studio.pesan_kursi(customer_pesan_kursi):
          continue
        elif customer_pesan_kursi == "out":
          print("Keluar Menu")
          break
        else:
          print("Silahkan masukan Pilihan yang benar")

  def customer_pesan(self):
    customer_pesan_film = input("\nMasukan film yang ingin dipesan : ")
    studio.melihat_kursi()

    if customer_pesan_film == "1":
      self.customer_pesan_kursi()

    elif customer_pesan_film == "2":
      self.customer_pesan_kursi()

    elif customer_pesan_film == "3":
      self.customer_pesan_kursi()
    else:
      print("Masukan pilihan yang benar")

studio = Studio()
customer = Customer(studio)

# Film
print("-- Film Yang Sedang Tayang : --\n")
studio.fungsi_penayangan_film()

customer.customer_pesan()
studio.melihat_kursi()