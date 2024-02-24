# Achmad Rizqy Pranata - 2209116086
# Program Pembelian Game Digital (Steam)

class GameSteam:
    def __init__(self):
        self.games = {}

    def tambah_game(self, id_game, judul, genre, harga, tipe):
        if id_game not in self.games:
            self.games[id_game] = {'judul': judul, 'genre': genre, 'harga': harga, 'tipe': tipe}
            print("Game berhasil ditambahkan ke Steam.")
        else:
            print("ID game sudah ada.")

    def tampilkan_game(self):
        if self.games:
            print("Daftar Game dan DLC di Steam:")
            for id_game, info_game in self.games.items():
                print(f"ID: {id_game}, Judul: {info_game['judul']}, Genre: {info_game['genre']}, Harga: {info_game['harga']}, Tipe: {info_game['tipe']}")
        else:
            print("Steam belum memiliki game atau DLC.")

    def perbarui_game(self, id_game, judul=None, genre=None, harga=None, tipe=None):
        if id_game in self.games:
            info_game = self.games[id_game]
            if judul:
                info_game['judul'] = judul
            if genre:
                info_game['genre'] = genre
            if harga:
                info_game['harga'] = harga
            if tipe:
                info_game['tipe'] = tipe
            print("Data game atau DLC berhasil diperbarui.")
        else:
            print("ID game tidak ditemukan.")

    def hapus_game(self, id_game):
        if id_game in self.games:
            del self.games[id_game]
            print("Game atau DLC berhasil dihapus dari Steam.")
        else:
            print("ID game tidak ditemukan.")

def main():
    game_steam = GameSteam()

    while True:
        print("\nPilihan Menu:")
        print("1. Tambah Game/DLC")
        print("2. Tampilkan Game/DLC")
        print("3. Perbarui Data Game/DLC")
        print("4. Hapus Game/DLC")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            id_game = input("Masukkan ID game: ")
            judul = input("Masukkan judul game: ")
            genre = input("Masukkan genre game: ")
            harga = float(input("Masukkan harga game: "))
            tipe = input("Masukkan tipe (Games/DLC): ")
            game_steam.tambah_game(id_game, judul, genre, harga, tipe)
        elif pilihan == '2':
            game_steam.tampilkan_game()
        elif pilihan == '3':
            id_game = input("Masukkan ID game yang akan diperbarui: ")
            judul = input("Masukkan judul baru (biarkan kosong jika tidak ingin mengubah): ")
            genre = input("Masukkan genre baru (biarkan kosong jika tidak ingin mengubah): ")
            harga = float(input("Masukkan harga baru (biarkan kosong jika tidak ingin mengubah): "))
            tipe = input("Masukkan tipe game baru (biarkan kosong jika tidak ingin mengubah): ")
            game_steam.perbarui_game(id_game, judul, genre, harga, tipe)
        elif pilihan == '4':
            id_game = input("Masukkan ID game/DLC yang akan dihapus: ")
            game_steam.hapus_game(id_game)
        elif pilihan == '5':
            print("Terima kasih telah memperbaiki data ku (｡˃ ᵕ < ) -Steam ")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
