level_diskon = (
    (500000, 15),  # belanja >= 500.000 -> diskon 15%
    (300000, 10),  # belanja >= 300.000 -> diskon 10%
    (100000, 5),  # belanja >= 100.000 -> diskon 5%
    (0, 0),  # default -> tidak ada diskon
)

hasil = tuple()


def hitung_diskon(total_belanja, level_diskon, index=0):
    if total_belanja > 1:
        hasil.append(total)
        if index < len(level_diskon):
            batas_belanja, diskon = level_diskon[index]
            if total_belanja >= batas_belanja:
                total = total_belanja * (1 - diskon / 100)
                hitung_diskon(total, level_diskon, index + 1)
            else:
                hitung_diskon(total_belanja, level_diskon, index + 1)
    return hasil
