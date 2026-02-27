# List
buah = ["apel", "mangga", "jeruk", "apel"]

# Menambah data (append)
buah.append("melon")

# Mengubah data berdasarkan index
buah[1] = "pisang"

print("Isi List:", buah)
print("Panjang List:", len(buah))

# Tuple
IPK = (2.3, 4.0, 3.5)

# Mengakses data
print("Nilai Akhir:", IPK[1])

# Tuple tidak bisa di-edit (immutable)
# IPK[0] = 2.3  <-- Ini akan error

# Set
id_user = {101, 102, 103, 101}  # 101 double

# Menambah data
id_user.add(104)

print("Isi Set :", id_user)
# Output tidak akan menampilkan 101 dua kali

# Dictionary
mahasiswa = {"nama": "Habib syikbi", "nim": "22010045", "prodi": "Informatika"}

# Mengakses value lewat key
print("Nama Mahasiswa:", mahasiswa["nama"])

# Mengupdate value
mahasiswa["prodi"] = "Sistem Informasi"

print("Data Lengkap:", mahasiswa)
