from art import logo
import random

print(logo)
print("Sayı tahmin etmeye hoş geldiniz")

def chech_answer(cevap):
    if answer == "kolay":
        print("10 adet tahmin hakkınız var:")
        for i in range(0, 10):
            tahmin = int(input("Tahmininiz: "))
            if tahmin != cevap:
                print(f"Yanlış tahmin tekrar dene, kalan hak{10-(i+1)}")
                if tahmin > cevap:
                    print("lower")
                if tahmin < cevap:
                    print("higher")
            elif tahmin == cevap:
                print("Tahmininiz doğru")
                break
            else:
                print("hakkınız bitti:")
    if answer == "zor":
        print("5 adet tahmin hakkınız var: ")
        for i in range(0, 5):
            tahmin = int(input("Tahmininiz: "))
            if tahmin != sayi:
                print(f"Yanlış tahmin tekrar dene, kalan hak {5-(i+1)}")
                if tahmin > sayi:
                    print("lower")
                if tahmin < sayi:
                    print("higher")
            elif tahmin == sayi:
                print("Tahmininiz doğru")
                break
            else:
                print("hakkınız bitti:")
                break



while True:
    sayi = random.randint(1,100)
    print("1-100 arasında bir sayı tahmin ediyorum, acaba ne???")
    answer= input("Bir zorlu seçin kolay veya zor: ")
    chech_answer(sayi)
    devam = input("devam etmek istiyorsanız evet istemiyorsanız hayır yazınız: ")
    if devam == "evet":
        continue
    elif devam == "hayır":
        break



