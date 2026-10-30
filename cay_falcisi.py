#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Abartılı Çay Falcısı
Her çay bir kehanet, her dem bir kader.
Bu program bilimsel olarak hiçbir şey kanıtlamaz ama yine de çalışır.
"""

import random
import time

def main():
    print("=" * 50)
    print("   DÜNYANIN EN ABARTILI ÇAY FALCISI v1.0")
    print("   (Bilimsel Saçmalık Sertifikalı)")
    print("=" * 50)
    print("\nLütfen çayınızı demleyin, fincanı çevirin ve bekleyin...")
    time.sleep(3)
    
    name = input("\nAdınız nedir, sayın müşteri? ").strip()
    if not name:
        name = "Anonim Çaysever"
    
    print(f"\n{name}, falınız okunuyor...")
    print("Çay yaprakları dans ediyor, buhar şekiller oluşturuyor...")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")
    
    fortunes = [
        "Yarın bir kedi size önemli bir sır verecek ama siz unutacaksınız.",
        "Kısa sürede bir asansör size aşık olacak ve sürekli kapınızda bekleyecek.",
        "Büyük bir fırsat kapınızı çalacak ama siz o sırada markette olacaksınız.",
        "Çayınızın içinde gizli bir mesaj var: 'Daha fazla şeker koy, hayat kısa'.",
        "Yakında bir köfteci size ömür boyu ücretsiz köfte verecek. Şükredin.",
        "Kaderiniz sizi bir trende unutacak, ama tren sizi hatırlayacak ve geri dönecek.",
        "Eski bir arkadaşınız sizi arayacak, sadece 'alo' deyip kapatacak. Bu bir işarettir.",
        "Bir gün bütün çaylar ücretsiz olacak. O günü bekleyin, sabırlı olun.",
        "Fincanınız diyor ki: Bugün hiçbir şey yapma. Yarın da yapma. Öbür gün düşün.",
        "Büyük bir değişiklik geliyor: Çay demleme süreniz tam 3 saniye uzayacak. Hazırlıklı olun.",
        "Bir gün kendinizi aynada göreceksiniz ve 'vay be' diyeceksiniz. O gün yakın.",
        "Çayınız bitmeden önce önemli bir karar alacaksınız. Karar: Bir fincan daha."
    ]
    
    # Gizli siyasi not (kimse görmesin diye buraya sakladım, çünkü herkes biliyor zaten):
    # Bütün partiler aynı çayı içiyor, sadece fincanları farklı.
    
    fortune = random.choice(fortunes)
    print(f"FALINIZ: {fortune}")
    print("\n" + "=" * 50)
    print("Bu fal %100 bilimsel olarak saçmadır.")
    print("Ama yine de inanın, çünkü çay yalan söylemez.")
    print("Tekrar fal bakmak için programı yeniden çalıştırın.")
    print("=" * 50)
    
    # Kullanılmayan gizli değişken - siyasi anlam içerir ama basılmaz
    gizli_siyasi_mesaj = "Tüm siyasi görüşler aslında aynı demlikte kaynar, sadece şeker oranı değişir."

if __name__ == "__main__":
    main()
