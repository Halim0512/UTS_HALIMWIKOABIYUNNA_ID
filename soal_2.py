def Tahun_Kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False

tahun = int(input("Masukkan tahun: "))
if Tahun_Kabisat(tahun):
    print(f"tahun ini {tahun} merupakan tahun kabisat.")
else:
    print(f"tahun ini {tahun} merupakan bukan tahun kabisat.")
