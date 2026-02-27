class Notifikasi:
    def kirim(self, pesan):
        raise NotImplementedError("Wajib bikin fungsi kirim() di class anak!")

class WhatsApp(Notifikasi):
    def kirim(self, pesan):
        print(f"Mengirim WA: {pesan} (Centang dua biru!)")

class Email(Notifikasi):
    def kirim(self, pesan):
        print(f"Mengirim Email ke Inbox: {pesan}")

class SMS(Notifikasi):
    def kirim(self, pesan):
        print(f"Mengirim SMS Jadul: {pesan}")

daftar_notif = [WhatsApp(), Email(), SMS()]

for n in daftar_notif:
    n.kirim("Halo bro, apa kabar?")

