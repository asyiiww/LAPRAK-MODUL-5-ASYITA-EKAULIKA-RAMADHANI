def mutlak(angka):
    if angka < 0:
        return -angka
    return angka

def hitung(nilai1, nilai2):
    return mutlak(nilai1 - nilai2)

def main():
    data = list(map(int, input().split()))
    a = data[0]
    c = data[1]
    b = data[2]
    d = data[3]
    hasil = hitung(a, b) + hitung(c, d)
    print(mutlak(hasil))

if __name__ == "__main__":
    main()