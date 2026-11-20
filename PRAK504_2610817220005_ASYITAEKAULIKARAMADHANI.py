def reverse(n):
    balik = 0
    while n > 0:
        balik = balik * 10 + (n % 10)
        n = n // 10
    return balik

def main():
    A, B = map(int, input().split())
    A = reverse(A)
    B = reverse(B)
    C = A + B 
    print(reverse(C))

if __name__ == "__main__":
    main()