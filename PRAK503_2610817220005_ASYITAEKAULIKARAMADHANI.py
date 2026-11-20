def maksimal(a, b):
    if a > b:
        return a
    return b

def minimal(a, b):
    if a < b:
        return a
    return b

def main():
    batas = 0
    maks = -100000
    minim = 100000
    bilangan = int(input())
    antrean = []
    while batas < bilangan:
        while len(antrean) == 0:
            antrean = input().split()
        nilai = int(antrean.pop(0))
        maks = maksimal(maks, nilai)
        minim = minimal(minim, nilai)
        batas += 1
    print(maks, minim)

if __name__ == "__main__":
    main()