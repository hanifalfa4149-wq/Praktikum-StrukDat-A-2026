import kurs


def ke_idr(mata_uang, jumlah):
    if mata_uang == "IDR":
        return jumlah
    nilai_kurs = kurs.data_kurs[mata_uang]
    return jumlah * nilai_kurs


def dari_idr(mata_uang, jumlah_idr):
    if mata_uang == "IDR":
        return jumlah_idr
    nilai_kurs = kurs.data_kurs[mata_uang]
    return jumlah_idr / nilai_kurs
