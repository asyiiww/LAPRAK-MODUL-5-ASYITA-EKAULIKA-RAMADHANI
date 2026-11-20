def Biodata(tahunLahir, nama, asal):
    tahun_sekarang = 2020
    umur = tahun_sekarang - tahunLahir
    print(f"Perkenalkan Nama Saya : {nama}")
    print(f"Umur Saya : {umur}")
    print(f"Saya Adalah Angkatan : {tahun_sekarang}")
    print(f"Asal Saya Dari : {asal}")

def main():
    tahunLahir = int(input())
    nama = input().strip()
    asal = input().strip()
    Biodata(tahunLahir, nama, asal)

if __name__ == "__main__":
    main()