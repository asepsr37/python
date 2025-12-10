"""
Output:

Kamar - Type room - price - Status
[Kamar 101] - Standard  - Rp 200.000 - [Tersedia]

"""

class Room:
  def __init__(self, room_number, type_room, price_room):
    """
      Fungsi ini digunakan untuk meambuat sebuah kamar di sebuah hotel
      room_number = Nomor kamar
      type_room = Tipe Kamar
      price_room = harga kamar
    """
    self.room_number = room_number
    self.type_room = type_room
    self.price_room = price_room
    self.is_available = True # Jadi saat membuat Room otomatis Kosong atau tersedia

  def booking_room(self):
    """"
    Fungsi ini untuk Check Room apakah tersedia atau tidak?
    Jadi Fungsi ini digunakan jika room sudah dibuat
    """
    if self.is_available: # Apakah kamar kosong (True) ?
      self.is_available = False # Jika kosong (True), ubah menjadi False (Tidak Kosong/Terisi)
      return True # Berhasil Booking atau Room terisi
    return False # Jika Kamar tidak Kosong atau terisi maka gagal booking
  
  def release_room(self):
    """
    Fungsi  ini untuk mngosongkan room jika Tamu sudah pergi, jadi room bisa dipesan lagi
    """
    self.is_available = True

  def __str__(self):
    """
    Fungsi ini untuk menampilkan dilayar apa saja room yang teredia
    """
    if self.is_available:
      status = "Tersedia"
    else:
      status = "Terisi"

    return f"[Kamar {self.room_number}] -- {self.type_room}  -- {self.price_room} -- [{status}]"

class Guest:
  def __init__(self, guest_id, name, guest_email):
    """
    Fungsi Untuk menyimpan data Tamu
    """

    self.guest_id = guest_id
    self.name = name
    self.guest_email = guest_email

  def __str__(self):
    f"[ID : {self.guest_id}] -- {self.name} -- {self.guest_email}"

class Reservation:
  """
  Class ini untuk transaksi antara Guest dan Room
  """
  def __init__(self, reservation_id, guest, room, night):
    """
    Fungsi untuk mencatat sebuah transaksi yang dilakukan oleh guest
    """
    self.reservation_id = reservation_id
    self.guest = guest
    self.room = room
    self.night = night

    # Harga total 
    self.total_price = room.price_room * night
    self.status = "pending"

  def process_payment(self):
    """
    Fungsi ini untuk mengubah status yang tadinya pending menjadi paid
    """
    self.status = "paid"
    print(f"Pembayaran diterima sebesar Rp{self.total_price}.... Reservasi Confirmed.")

  def __str__(self):
   return (f"Reservasi #{self.reservation_id}\n"
          f"Tamu: {self.guest.name}\n"
          f"Kamar: {self.room.room_number} ({self.room.type_room})\n"
          f"Total: Rp{self.total_price} ({self.status})")

class Hotel:
  """
  Pada class Hotel dilakukan sebuah penetapan alur dalam proses reservasi hotel
  """

  def __init__(self, name):
    """
    Fungsi ini untuk menyimpan sebuah data
    self.rooms dan selef.reservations akan dibuat list, karena satu hotel pasti punya banyak room dan reservasi
    """
    self.name = name
    self.rooms = []
    self.reservations = []

  def add_room(self, room):
    """
    Fungsi ini untuk memasukan kkamar dalam sebuah hotel
    """
    self.rooms.append(room)
  
  def show_available_room(self):
    """
    Fungsi Mengecek kamar yang tersedia
    """

    print(f"Kamar yang tersedia {self.name} ---")
    available_found = False # Room tidak tersedia

    for room in self.rooms:
      if room.is_available: # cek room apakah tersedia
        print(room) # maka jika tersedia tampilkan
        available_found = True # buat room tersedia
      
      if not available_found: # Jika Room tidak tersedia
        print("Maaf, semua kamar penuh")

  def make_reservation(self, guest, room_number, nights):
    
    # 1. Cari kamar berdasarkan nomor
    selected_room = None
    for room in self.rooms:
      if room.room_number == room_number:
        selected_room = room
        break

   # 2. Validasi Ketersedian Room
    if selected_room is None:
      print("Kamar tidak ditemukan....")
      return
    if not selected_room.is_available:
      print(f"Kamar {room_number} sudah tersisi")
      return
    
    # 3. Booking untuk ubah status kamar
    selected_room.booking_room()

    # 4. Buat objek reservasi baru
    new_id = f"RES-{len(self.reservations) + 1:03d}"
    new_reservation = Reservation(new_id, guest, selected_room, nights) # pakai class Reservation

    # 5. Simpan ke daftar reservasi Hote
    self.reservations.append(new_reservation)

    print(f"Berhasil membuat untuk reservasi {guest.name}")
    return new_reservation
  

"""
Contoh Penerapan
"""
# 1. Buat Hotel dan Kamar
my_hotel = Hotel("Hotel Indah")

# Menambahkan kamar ke hotel
r1 = Room(101, "Standard", 300000)
r2 = Room(102, "Standard", 350000)
r3 = Room(202, "Deluxe", 500000)

my_hotel.add_room(r1)
my_hotel.add_room(r2)
my_hotel.add_room(r3)

# 2. Tampilkan kamar kosong
my_hotel.show_available_room()

# 3. Tamu reservasi
guest1 = Guest("G001", "Budi Santoso", "budi@email.com")
# tamu reservasi untuk kamar 101, 2 malam
rest1 = my_hotel.make_reservation(guest1, 101, 2) 

# 4. Cek detail reservasi
if rest1:
  print(rest1) # status pending
  rest1.process_payment() # Bayar
  print(f"Status Sekarang: {rest1.status}")

# 5. ccek ketersedian kamar
my_hotel.show_available_room()

# 6. Coba booking kamar yang sama
guest2 = Guest("G002", "Siti Aminah", "siti@email.com")
my_hotel.make_reservation(guest2, 101, 1)

